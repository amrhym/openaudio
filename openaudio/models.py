"""
Data models for OpenAudio SDK
"""

from enum import Enum
from typing import Optional
from dataclasses import dataclass


class AudioFormat(Enum):
    """Supported audio output formats"""
    MP3 = "mp3"
    WAV = "wav"
    OGG = "ogg"
    FLAC = "flac"
    AAC = "aac"


class Voice(Enum):
    """Available TTS voices"""
    O1 = "o1"
    O2 = "o2"
    O3 = "o3"
    O4 = "o4"
    O5 = "o5"
    O6 = "o6"


@dataclass
class VoiceOptions:
    """Options for TTS voice configuration"""
    voice: Voice = Voice.O4
    speed: float = 1.0
    pitch: float = 1.0
    volume: float = 1.0
    
    def __post_init__(self):
        if not 0.25 <= self.speed <= 4.0:
            raise ValueError("Speed must be between 0.25 and 4.0")
        if not 0.5 <= self.pitch <= 2.0:
            raise ValueError("Pitch must be between 0.5 and 2.0")
        if not 0.0 <= self.volume <= 1.0:
            raise ValueError("Volume must be between 0.0 and 1.0")


@dataclass
class AudioResponse:
    """Response from TTS generation"""
    audio_data: bytes
    format: AudioFormat
    duration: Optional[float] = None
    text: Optional[str] = None