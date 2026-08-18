"""Small helper for sending JSON payloads to an n8n webhook."""

from __future__ import annotations

from typing import Any


def trigger_webhook(url: str, payload: dict[str, Any], timeout: int = 15) -> dict[str, Any]:
    """POST a JSON payload to an n8n webhook.

    Import requests lazily so the HANS core can still run without integrations.
    """
    import requests

    response = requests.post(url, json=payload, timeout=timeout)
    response.raise_for_status()
    try:
        return response.json()
    except ValueError:
        return {"status_code": response.status_code, "text": response.text}
