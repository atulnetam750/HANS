"""HANS — a small, extensible AI/automation assistant foundation."""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime


@dataclass
class HansConfig:
    name: str = "HANS"
    language: str = "hi"
    n8n_webhook_url: str | None = None

    @classmethod
    def from_env(cls) -> "HansConfig":
        return cls(
            name=os.getenv("HANS_NAME", "HANS"),
            language=os.getenv("HANS_LANGUAGE", "hi"),
            n8n_webhook_url=os.getenv("N8N_WEBHOOK_URL") or None,
        )


def local_command(command: str) -> str:
    """Handle commands that do not require an external AI provider."""
    text = command.strip().lower()
    if text in {"hello", "hi", "namaste", "नमस्ते"}:
        return "नमस्ते! मैं HANS हूँ।"
    if "time" in text or "समय" in text:
        return datetime.now().strftime("Current time: %H:%M:%S")
    if "date" in text or "तारीख" in text:
        return datetime.now().strftime("Today's date: %Y-%m-%d")
    if text in {"help", "मदद"}:
        return "Commands: help, time, date, status, exit"
    if text == "status":
        return "HANS core is running. External AI and n8n integrations are optional."
    return "मैंने command सुना: " + command


def main() -> None:
    config = HansConfig.from_env()
    print(f"{config.name} AI Assistant — development build")
    print("Hindi-friendly automation assistant. Type 'help' for commands.")

    while True:
        try:
            command = input("You > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nHANS > Goodbye!")
            break

        if not command:
            continue
        if command.lower() in {"exit", "quit", "bye", "बंद"}:
            print("HANS > Goodbye!")
            break
        print("HANS >", local_command(command))


if __name__ == "__main__":
    main()
