## ============================================================
## OLLAMA.PY - Local Ollama brain
## ============================================================
## Free. Local. No API cost. Needs ollama installed.
## ============================================================

import subprocess
import sys
import re
from .base import BaseBrain


class OllamaBrain(BaseBrain):
    """Local Ollama model client."""

    def __init__(self, model: str = "mistral"):
        self.model = model

    @property
    def name(self) -> str:
        return f"ollama:{self.model}"

    def chat(self, context: str, stream: bool = True) -> str:
        if not context or not context.strip():
            return ""

        try:
            process = subprocess.Popen(
                ["ollama", "run", self.model],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=False,
                bufsize=0
            )

            process.stdin.write((context + "\n").encode())
            process.stdin.flush()
            process.stdin.close()

            response = ""
            while True:
                char = process.stdout.read(1)
                if not char:
                    break
                decoded = char.decode('utf-8', errors='replace')
                response += decoded
                if stream:
                    sys.stdout.write(decoded)
                    sys.stdout.flush()

            process.wait()
            return response.strip()

        except FileNotFoundError:
            print("[Error: Ollama not installed]")
            return ""
        except Exception as e:
            print(f"[Ollama error: {e}]")
            return ""

    def check(self) -> bool:
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return self.model in result.stdout
        except:
            return False

    def list_models(self) -> str:
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout
        except:
            return "Error: Ollama not available"
