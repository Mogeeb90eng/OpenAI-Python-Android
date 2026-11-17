# OpenAI-Python-Android

Android wrapper for testing the official OpenAI Python SDK inside an APK.

## Build

The GitHub Actions workflow builds an ARM64 APK using Chaquopy and Python 3.13.
Run it from **Actions → Build Android APK → Run workflow**.

The first build is a compatibility test. The APK checks that the OpenAI SDK and
its runtime dependencies can be imported on Android. It does not contain an API
key and does not send API requests.

## Important

- This starter targets Android API 31+ and `arm64-v8a`.
- It bundles OpenAI Python SDK 3.3.0.
- The workflow prepares an Android ARM64 Jiter wheel for Python 3.13.
- Never commit an OpenAI API key to this repository.
