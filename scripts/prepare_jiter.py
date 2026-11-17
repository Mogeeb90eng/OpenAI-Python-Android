import hashlib
import io
import json
import re
import urllib.request
import zipfile
from pathlib import Path

VERSION = "0.16.0"
WHEEL_NAME = f"jiter_android-{VERSION}-cp313-cp313-android_31_arm64_v8a.whl"
URL = f"https://files.pythonhosted.org/packages/"

# Resolve the exact wheel URL from the official PyPI JSON metadata.
meta_url = f"https://pypi.org/pypi/jiter-android/{VERSION}/json"
with urllib.request.urlopen(meta_url) as response:
    metadata = json.load(response)

wheel = next(
    item for item in metadata["urls"]
    if item["filename"] == WHEEL_NAME
)
with urllib.request.urlopen(wheel["url"]) as response:
    wheel_bytes = response.read()

out_dir = Path("wheels")
out_dir.mkdir(exist_ok=True)
out_name = f"jiter-{VERSION}-cp313-cp313-android_31_arm64_v8a.whl"

with zipfile.ZipFile(io.BytesIO(wheel_bytes), "r") as src:
    entries = {name: src.read(name) for name in src.namelist()}

dist_info = next(
    name.split("/")[0] for name in entries
    if name.endswith(".dist-info/METADATA")
)
new_dist_info = f"jiter-{VERSION}.dist-info"

rewritten = {}
for name, data in entries.items():
    new_name = name.replace(dist_info, new_dist_info, 1)
    if new_name.endswith(".dist-info/METADATA"):
        text = data.decode("utf-8")
        text = re.sub(r"(?m)^Name: jiter-android$", "Name: jiter", text)
        data = text.encode("utf-8")
    rewritten[new_name] = data

record_name = f"{new_dist_info}/RECORD"
rows = []
for name, data in rewritten.items():
    if name == record_name:
        continue
    digest = hashlib.sha256(data).digest()
    import base64
    encoded = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
    rows.append(f"{name},sha256={encoded},{len(data)}")
rows.append(f"{record_name},,")
rewritten[record_name] = ("\n".join(rows) + "\n").encode()

with zipfile.ZipFile(out_dir / out_name, "w", zipfile.ZIP_DEFLATED) as dst:
    for name, data in rewritten.items():
        dst.writestr(name, data)

print(f"Prepared Android jiter wheel: {out_dir / out_name}")
