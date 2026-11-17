import importlib.metadata
import openai
import httpx2
import pydantic
import anyio
import jiter

def check():
lines = [
"Python SDK import test: SUCCESS",
f"OpenAI SDK: {openai.version}",
f"HTTPX2: {getattr(httpx2, 'version', 'imported')}",
f"Pydantic: {pydantic.version}",
f"AnyIO: {importlib.metadata.version('anyio')}",
f"Jiter module: {jiter.file}",
"",
"OpenAI Python SDK successfully loaded.",
"This test does not send an API request."
]
return "\n".join(lines)
