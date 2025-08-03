# OpenAudio SDK

A powerful, professional-grade Text-to-Speech SDK for Python with high-quality voice synthesis.

## Features

- 🎯 **Simple API** - Clean, intuitive interface for TTS generation
- 🎭 **Multiple Voices** - 6 distinct voice profiles for different use cases
- 🌍 **Multi-Language Support** - Generate speech in multiple languages
- 💾 **Flexible Output** - Save to file or get audio data in memory
- ⚡ **High Performance** - Fast, efficient audio generation
- 🔧 **Customizable** - Control voice parameters and tone

## Installation

```bash
# Clone the repository
git clone https://github.com/amrhym/openaudio.git
cd openaudio

# Install the SDK
pip install .
```

## Quick Start

```python
from openaudio import OpenAudioClient

# Initialize client
client = OpenAudioClient(api_key="your_api_key")

# Generate speech and save to file
client.generate_speech_to_file(
    text="Hello, world! This is OpenAudio SDK.",
    output_path="output.wav"
)
```

## Available Voices

| Voice | Description | Best For |
|-------|-------------|----------|
| `O1` | Soft, melodic voice | Audiobooks, meditation |
| `O2` | Deep, resonant voice | Narration, documentaries |
| `O3` | Strong, authoritative voice | News, announcements |
| `O4` | Balanced, natural voice (default) | General purpose |
| `O5` | Warm, expressive voice | Storytelling, education |
| `O6` | Playful, energetic voice | Children's content, ads |

## Usage Examples

### Basic Text-to-Speech

```python
from openaudio import OpenAudioClient

client = OpenAudioClient(api_key="your_api_key")

# Generate with default voice
client.generate_speech_to_file(
    text="Welcome to OpenAudio SDK",
    output_path="welcome.wav"
)
```

### Using Different Voices

```python
from openaudio import OpenAudioClient, VoiceOptions, Voice

client = OpenAudioClient(api_key="your_api_key")

# Use O6 voice for energetic tone
voice_options = VoiceOptions(voice=Voice.O6)
client.generate_speech_to_file(
    text="This is an exciting announcement!",
    output_path="announcement.wav",
    voice_options=voice_options
)
```

### System Prompts for Tone Control

```python
# Add specific tone or emotion
client.generate_speech_to_file(
    text="Have a wonderful day!",
    output_path="greeting.wav",
    system_prompt="Say cheerfully"
)
```

### In-Memory Audio Generation

```python
# Get audio data without saving to file
response = client.generate_speech(
    text="This audio is generated in memory",
    voice_options=VoiceOptions(voice=Voice.O1)
)

print(f"Audio size: {len(response.audio_data)} bytes")
print(f"Format: {response.format.value}")
```

### Multi-Language Support

```python
# Generate speech in different languages
texts = [
    ("Hello, how are you?", "en"),
    ("Bonjour, comment allez-vous?", "fr"),
    ("Hola, ¿cómo estás?", "es"),
    ("مرحبا، كيف حالك؟", "ar"),
    ("你好，你好吗？", "zh")
]

for text, lang in texts:
    client.generate_speech_to_file(
        text=text,
        output_path=f"greeting_{lang}.wav"
    )
```

## API Reference

### OpenAudioClient

```python
OpenAudioClient(api_key: Optional[str] = None)
```

Main client for interacting with the OpenAudio SDK.

#### Methods

##### generate_speech
```python
generate_speech(
    text: str,
    voice_options: Optional[VoiceOptions] = None,
    output_format: AudioFormat = AudioFormat.WAV,
    system_prompt: Optional[str] = None
) -> AudioResponse
```

Generate speech audio in memory.

##### generate_speech_to_file
```python
generate_speech_to_file(
    text: str,
    output_path: Union[str, Path],
    voice_options: Optional[VoiceOptions] = None,
    output_format: AudioFormat = AudioFormat.WAV,
    system_prompt: Optional[str] = None
) -> str
```

Generate speech and save directly to file.

### VoiceOptions

```python
@dataclass
class VoiceOptions:
    voice: Voice = Voice.O4  # Default voice
    speed: float = 1.0      # Range: 0.25 to 4.0
    pitch: float = 1.0      # Range: 0.5 to 2.0
    volume: float = 1.0     # Range: 0.0 to 1.0
```

Configure voice parameters for speech generation.

### Voice Enum

```python
class Voice(Enum):
    O1 = "o1"  # Soft, melodic
    O2 = "o2"  # Deep, resonant
    O3 = "o3"  # Strong, authoritative
    O4 = "o4"  # Balanced, natural (default)
    O5 = "o5"  # Warm, expressive
    O6 = "o6"  # Playful, energetic
```

## Error Handling

```python
from openaudio import OpenAudioClient, OpenAudioError, InvalidInputError

try:
    client = OpenAudioClient(api_key="your_api_key")
    client.generate_speech_to_file("Hello", "output.wav")
except InvalidInputError as e:
    print(f"Invalid input: {e}")
except OpenAudioError as e:
    print(f"SDK error: {e}")
```

## Performance Tips

1. **Reuse Client Instance** - Create one client and reuse it for multiple requests
2. **Batch Processing** - Process multiple texts in sequence using the same client
3. **Voice Selection** - Choose appropriate voices for your content type
4. **Error Handling** - Always implement proper error handling for production use

## Requirements

- Python 3.8 or higher
- API key for authentication

## Support

For issues, questions, or contributions, please visit our [GitHub repository](https://github.com/amrhym/openaudio).

## License

This project is proprietary software. All rights reserved.

---

**OpenAudio SDK** - Professional Text-to-Speech Solution