import importlib.metadata
import openai
import httpx2
import pydantic
import anyio
import jiter

def check():
    lines = [
        "Python SDK import test: SUCCESS",
        f"OpenAI SDK: {openai.__version__}",
        f"HTTPX2: {getattr(httpx2, '__version__', 'imported')}",
        f"Pydantic: {pydantic.__version__}",
        f"AnyIO: {importlib.metadata.version('anyio')}",
        f"Jiter module: {jiter.__file__}",
        "",
        "The OpenAI Python package is bundled in this APK.",
        "This test does not send an API request."
    ]
    return "\n".join(lines)
