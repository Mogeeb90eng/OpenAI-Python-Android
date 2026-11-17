package com.mogeeb.openaiandroid;

import android.app.Activity;
import android.os.Bundle;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends Activity {
    private TextView output;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(32, 40, 32, 32);

        TextView title = new TextView(this);
        title.setText("OpenAI Python SDK for Android");
        title.setTextSize(22);
        layout.addView(title);

        Button test = new Button(this);
        test.setText("Check SDK installation");
        layout.addView(test);

        output = new TextView(this);
        output.setText("Press the button to test the embedded Python SDK.");
        output.setTextSize(16);
        output.setPadding(0, 24, 0, 0);

        ScrollView scroll = new ScrollView(this);
        scroll.addView(output);
        layout.addView(scroll, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, 0, 1));

        test.setOnClickListener(v -> runSdkCheck());
        setContentView(layout);
    }

    private void runSdkCheck() {
        try {
            String result = Python.getInstance()
                    .getModule("sdk_check")
                    .callAttr("check")
                    .toString();
            output.setText(result);
        } catch (Exception e) {
            output.setText("SDK test failed:\n" + e);
        }
    }
}
