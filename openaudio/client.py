"""
OpenAudio Client - Core TTS functionality
"""

import wave
import io
from typing import Optional, Union
from pathlib import Path

from .exceptions import OpenAudioError, AuthenticationError, InvalidInputError, APIError
from .models import VoiceOptions, AudioFormat, AudioResponse, Voice
from ._core import _create_client, _generate_content


class OpenAudioClient:
    """Main client for OpenAudio TTS SDK"""
    
    DEFAULT_SAMPLE_RATE = 24000
    DEFAULT_CHANNELS = 1
    DEFAULT_SAMPLE_WIDTH = 2
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize OpenAudio client
        
        Args:
            api_key: Optional API key for authentication
            model: Optional model override (ignored, for compatibility)
        """
        try:
            self._client = _create_client(api_key)
        except Exception as e:
            raise AuthenticationError(f"Failed to initialize client: {str(e)}")
    
    def _get_voice_name(self, voice: Voice) -> str:
        """Get voice name mapped to internal API"""
        # Map our voice names to actual API voice names
        voice_map = {
            "o1": "Aoede",
            "o2": "Charon",
            "o3": "Fenrir",
            "o4": "Kore",
            "o5": "Orpheus",
            "o6": "Puck"
        }
        return voice_map.get(voice.value, "Kore")
    
    def _create_wave_data(self, pcm_data: bytes) -> bytes:
        """Convert PCM data to WAV format"""
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wf:
            wf.setnchannels(self.DEFAULT_CHANNELS)
            wf.setsampwidth(self.DEFAULT_SAMPLE_WIDTH)
            wf.setframerate(self.DEFAULT_SAMPLE_RATE)
            wf.writeframes(pcm_data)
        return wav_buffer.getvalue()
    
    def generate_speech(self,
                       text: str,
                       voice_options: Optional[VoiceOptions] = None,
                       output_format: AudioFormat = AudioFormat.WAV,
                       system_prompt: Optional[str] = None) -> AudioResponse:
        """
        Generate speech from text
        
        Args:
            text: Text to convert to speech
            voice_options: Voice configuration options
            output_format: Output audio format
            system_prompt: Optional system instruction
        
        Returns:
            AudioResponse containing audio data
        """
        if not text:
            raise InvalidInputError("Text input cannot be empty")
        
        voice_options = voice_options or VoiceOptions()
        
        try:
            # Use obfuscated core
            pcm_data = _generate_content(
                self._client,
                text,
                self._get_voice_name(voice_options.voice),
                system_prompt
            )
            
            if not pcm_data:
                raise APIError("No audio data received")
            
            audio_data = self._create_wave_data(pcm_data)
            
            return AudioResponse(
                audio_data=audio_data,
                format=output_format,
                text=text
            )
            
        except Exception as e:
            if isinstance(e, OpenAudioError):
                raise
            raise APIError(f"Failed to generate speech: {str(e)}")
    
    def generate_speech_to_file(self,
                              text: str,
                              output_path: Union[str, Path],
                              voice_options: Optional[VoiceOptions] = None,
                              output_format: AudioFormat = AudioFormat.WAV,
                              system_prompt: Optional[str] = None) -> str:
        """
        Generate speech and save to file
        
        Args:
            text: Text to convert to speech
            output_path: Path to save audio file
            voice_options: Voice configuration options
            output_format: Output audio format
            system_prompt: Optional system instruction
        
        Returns:
            Path to saved file
        """
        if not text:
            raise InvalidInputError("Text input cannot be empty")
        
        voice_options = voice_options or VoiceOptions()
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # Use obfuscated core
            pcm_data = _generate_content(
                self._client,
                text,
                self._get_voice_name(voice_options.voice),
                system_prompt
            )
            
            # Save to file
            with wave.open(str(output_path), 'wb') as wf:
                wf.setnchannels(self.DEFAULT_CHANNELS)
                wf.setsampwidth(self.DEFAULT_SAMPLE_WIDTH)
                wf.setframerate(self.DEFAULT_SAMPLE_RATE)
                wf.writeframes(pcm_data)
            
            return str(output_path)
            
        except Exception as e:
            if isinstance(e, OpenAudioError):
                raise
            raise APIError(f"Failed to generate speech: {str(e)}")