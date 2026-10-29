from __future__ import annotations

import json
from typing import Any, Dict
from urllib import error, request


class ModelNotAvailableError(RuntimeError):
    """Raised when the local model runtime cannot be reached."""


class ModelRequestError(RuntimeError):
    """Raised when the local model responds with a problem."""


class LocalAIModel:
    """Talk to a local Ollama server using a simple HTTP API."""

    def __init__(self, model_name: str = "llama3.2:3b", base_url: str = "http://localhost:11434", timeout: int = 30) -> None:
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def is_available(self) -> bool:
        """Check whether the Ollama server is responding."""
        try:
            api_request = request.Request(
                f"{self.base_url}/api/tags",
                headers={"Accept": "application/json"},
            )
            with request.urlopen(api_request, timeout=self.timeout) as response:
                return response.status == 200
        except (error.URLError, TimeoutError, OSError):
            return False

    def generate(self, prompt: str) -> str:
        """Send a prompt to the local model and return the generated text."""
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        if not self.is_available():
            raise ModelNotAvailableError(
                "The local model runtime is not available. Start Ollama and run 'ollama pull llama3.2:3b'."
            )

        payload: Dict[str, Any] = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
        }

        encoded_data = json.dumps(payload).encode("utf-8")
        api_request = request.Request(
            f"{self.base_url}/api/generate",
            data=encoded_data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with request.urlopen(api_request, timeout=self.timeout) as response:
                result = json.loads(response.read().decode("utf-8"))
        except error.HTTPError as exc:
            raise ModelRequestError(f"The model request failed with HTTP status {exc.code}.") from exc
        except error.URLError as exc:
            raise ModelNotAvailableError(
                "The local model runtime could not be reached. Please start Ollama and try again."
            ) from exc

        if "error" in result:
            error_message = result["error"]
            if "not found" in error_message.lower() or "model" in error_message.lower():
                raise ModelNotAvailableError(
                    f"The model '{self.model_name}' is not installed. Run 'ollama pull {self.model_name}'."
                )
            raise ModelRequestError(error_message)

        model_response = result.get("response", "").strip()
        if not model_response:
            raise ModelRequestError("The model returned an empty response.")

        return model_response
