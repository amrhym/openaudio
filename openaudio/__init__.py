"""
OpenAudio SDK - A modern text-to-speech SDK for Python
"""

from .client import OpenAudioClient
from .exceptions import OpenAudioError, AuthenticationError, InvalidInputError
from .models import VoiceOptions, AudioFormat, Voice, AudioResponse

__version__ = "1.0.0"
__all__ = [
    "OpenAudioClient",
    "OpenAudioError",
    "AuthenticationError",
    "InvalidInputError",
    "VoiceOptions",
    "AudioFormat",
    "Voice",
    "AudioResponse"
]