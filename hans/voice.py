"""Optional voice helpers for HANS.

Voice dependencies are intentionally optional so the text assistant stays lightweight.
"""

from __future__ import annotations


def text_to_speech(text: str, language: str = "hi", output_file: str = "hans_output.mp3") -> str:
    """Generate speech with gTTS when the optional dependency is installed."""
    from gtts import gTTS

    gTTS(text=text, lang=language).save(output_file)
    return output_file
