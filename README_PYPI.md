# OpenAudio SDK

Professional Text-to-Speech SDK for Python with high-quality voice synthesis.

## Installation

```bash
pip install openaudio
```

## Quick Start

```python
from openaudio import OpenAudioClient


client = OpenAudioClient(api_key="YOUR_API_KEY")

# Generate speech
client.generate_speech_to_file(
    text="Hello, world! This is OpenAudio SDK.",
    output_path="hello.wav"
)
```

## Features

- 🎯 **Simple API** - Clean, intuitive interface
- 🎭 **6 Voice Options** - Different voices for different needs
- 🌍 **Multi-Language** - Supports 100+ languages
- 💾 **Flexible Output** - Save to file or get in-memory
- ⚡ **High Performance** - Fast, efficient generation
- 🔧 **Customizable** - Control voice, speed, pitch, and tone

## Available Voices

- **O1** - Soft, melodic voice
- **O2** - Deep, resonant voice  
- **O3** - Strong, authoritative voice
- **O4** - Balanced, natural voice (default)
- **O5** - Warm, expressive voice
- **O6** - Playful, energetic voice

## Examples

### Different Voices

```python
from openaudio import OpenAudioClient, VoiceOptions, Voice

client = OpenAudioClient(api_key="YOUR_API_KEY")

# Use different voices
voice_options = VoiceOptions(voice=Voice.O6)
client.generate_speech_to_file(
    text="This is the playful O6 voice!",
    output_path="playful.wav",
    voice_options=voice_options
)
```

### Control Tone

```python
# Add emotion or tone
client.generate_speech_to_file(
    text="Have a wonderful day!",
    output_path="cheerful.wav",
    system_prompt="Say cheerfully"
)
```

### Multiple Languages

```python
# Generate in any language
texts = [
    ("Hello", "en.wav"),
    ("Bonjour", "fr.wav"),
    ("Hola", "es.wav"),
    ("你好", "zh.wav"),
    ("مرحبا", "ar.wav")
]

for text, filename in texts:
    client.generate_speech_to_file(text, filename)
```

### In-Memory Generation

```python
# Get audio data without saving to file
response = client.generate_speech(
    text="This is in memory",
    voice_options=VoiceOptions(voice=Voice.O1)
)

print(f"Audio size: {len(response.audio_data)} bytes")
```


## Documentation

Full documentation and examples: https://github.com/amrhym/openaudio

## License

MIT License