# OpenAudio SDK - Setup & Usage Guide

## 🚀 Quick Start

### 1. Installation

Install the OpenAudio SDK using pip:

```bash
pip install openaudio
```

### 2. Get an API Key

To use the OpenAudio SDK, you'll need an API key:

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy your API key (it starts with `AIza...`)

> **Note**: Keep your API key secure and never commit it to version control.

### 3. Basic Usage

```python
from openaudio import OpenAudioClient

# Initialize the client with your API key
client = OpenAudioClient(api_key="YOUR_API_KEY_HERE")

# Generate speech and save to file
client.generate_speech_to_file(
    text="Hello, world! Welcome to OpenAudio SDK.",
    output_path="hello.wav"
)
```

## 📖 Detailed Setup

### Environment Setup (Recommended)

1. **Create a virtual environment:**
```bash
python -m venv openaudio-env
source openaudio-env/bin/activate  # On Windows: openaudio-env\Scripts\activate
```

2. **Install the SDK:**
```bash
pip install openaudio
```

3. **Set up environment variables (optional but recommended):**

Create a `.env` file:
```bash
OPENAUDIO_API_KEY=your_api_key_here
```

Then in your Python code:
```python
import os
from openaudio import OpenAudioClient

api_key = os.getenv("OPENAUDIO_API_KEY")
client = OpenAudioClient(api_key=api_key)
```

## 💻 Usage Examples

### Example 1: Simple Text-to-Speech

```python
from openaudio import OpenAudioClient

# Initialize client
client = OpenAudioClient(api_key="YOUR_API_KEY")

# Generate speech with default settings
client.generate_speech_to_file(
    text="This is a simple text to speech example.",
    output_path="simple_example.wav"
)

print("Audio saved to simple_example.wav")
```

### Example 2: Using Different Voices

```python
from openaudio import OpenAudioClient, VoiceOptions, Voice

client = OpenAudioClient(api_key="YOUR_API_KEY")

# Available voices
voices = {
    Voice.O1: "Soft, melodic voice",
    Voice.O2: "Deep, resonant voice",
    Voice.O3: "Strong, authoritative voice",
    Voice.O4: "Balanced, natural voice (default)",
    Voice.O5: "Warm, expressive voice",
    Voice.O6: "Playful, energetic voice"
}

# Generate with each voice
for voice, description in voices.items():
    voice_options = VoiceOptions(voice=voice)
    filename = f"voice_{voice.value}.wav"
    
    client.generate_speech_to_file(
        text=f"This is the {description}",
        output_path=filename,
        voice_options=voice_options
    )
    print(f"Generated {filename}")
```

### Example 3: Controlling Tone with System Prompts

```python
from openaudio import OpenAudioClient

client = OpenAudioClient(api_key="YOUR_API_KEY")

# Different tones for the same text
tones = [
    ("cheerfully", "cheerful.wav"),
    ("sadly", "sad.wav"),
    ("excitedly", "excited.wav"),
    ("calmly", "calm.wav")
]

text = "The weather is beautiful today"

for tone, filename in tones:
    client.generate_speech_to_file(
        text=text,
        output_path=filename,
        system_prompt=f"Say {tone}"
    )
    print(f"Generated {filename} with {tone} tone")
```

### Example 4: In-Memory Audio Generation

```python
from openaudio import OpenAudioClient, VoiceOptions, Voice
import wave
import io

client = OpenAudioClient(api_key="YOUR_API_KEY")

# Generate audio in memory (without saving to file)
response = client.generate_speech(
    text="This audio is generated in memory",
    voice_options=VoiceOptions(voice=Voice.O1)
)

# Work with the audio data
print(f"Generated {len(response.audio_data)} bytes of audio")
print(f"Format: {response.format.value}")

# You can save it manually if needed
with open("memory_audio.wav", "wb") as f:
    f.write(response.audio_data)
```

### Example 5: Multi-Language Support

```python
from openaudio import OpenAudioClient, VoiceOptions, Voice

client = OpenAudioClient(api_key="YOUR_API_KEY")

# Generate speech in different languages
texts = [
    ("Hello, how are you?", "english.wav"),
    ("Bonjour, comment allez-vous?", "french.wav"),
    ("Hola, ¿cómo estás?", "spanish.wav"),
    ("你好，你好吗？", "chinese.wav"),
    ("مرحبا، كيف حالك؟", "arabic.wav"),
    ("Здравствуйте, как дела?", "russian.wav"),
    ("こんにちは、元気ですか？", "japanese.wav")
]

for text, filename in texts:
    client.generate_speech_to_file(
        text=text,
        output_path=filename,
        voice_options=VoiceOptions(voice=Voice.O4)  # Default voice
    )
    print(f"Generated {filename}: {text}")
```

### Example 6: Batch Processing

```python
from openaudio import OpenAudioClient
import csv

client = OpenAudioClient(api_key="YOUR_API_KEY")

# Process multiple texts from a CSV file
def process_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            text = row['text']
            output_file = row['output_file']
            
            client.generate_speech_to_file(
                text=text,
                output_path=output_file
            )
            print(f"Processed: {output_file}")

# Example CSV format:
# text,output_file
# "Welcome to our service","welcome.wav"
# "Thank you for calling","thank_you.wav"
```

### Example 7: Error Handling

```python
from openaudio import (
    OpenAudioClient, 
    OpenAudioError, 
    InvalidInputError,
    AuthenticationError
)

try:
    # Initialize client
    client = OpenAudioClient(api_key="YOUR_API_KEY")
    
    # Generate speech
    client.generate_speech_to_file(
        text="Hello world",
        output_path="output.wav"
    )
    print("Success!")
    
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
    print("Please check your API key")
    
except InvalidInputError as e:
    print(f"Invalid input: {e}")
    
except OpenAudioError as e:
    print(f"SDK error: {e}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 🎛️ Advanced Configuration

### Voice Options

```python
from openaudio import VoiceOptions, Voice

# Create custom voice options
voice_options = VoiceOptions(
    voice=Voice.O5,     # Voice selection
    speed=1.0,          # Speed (0.25 to 4.0)
    pitch=1.0,          # Pitch (0.5 to 2.0)  
    volume=1.0          # Volume (0.0 to 1.0)
)

client.generate_speech_to_file(
    text="Custom voice settings",
    output_path="custom.wav",
    voice_options=voice_options
)
```

### Working with Audio Format

```python
from openaudio import AudioFormat

# Currently supports WAV format
response = client.generate_speech(
    text="Audio format example",
    output_format=AudioFormat.WAV
)
```

## 🔧 Troubleshooting

### Common Issues

1. **Import Error:**
```bash
# Make sure the package is installed
pip install --upgrade openaudio
```

2. **Authentication Error:**
```python
# Check your API key is correct
# API key should start with "AIza..."
client = OpenAudioClient(api_key="AIza...")
```

3. **No Audio Output:**
```python
# Ensure text is not empty
# Check file permissions for output path
```

4. **Rate Limiting:**
```python
import time

# Add delays between requests if processing many files
for text in texts:
    client.generate_speech_to_file(text, f"output_{i}.wav")
    time.sleep(1)  # Wait 1 second between requests
```

## 📋 API Reference

### OpenAudioClient

```python
client = OpenAudioClient(api_key: Optional[str] = None)
```

### Methods

#### generate_speech_to_file
```python
client.generate_speech_to_file(
    text: str,                              # Text to convert
    output_path: str,                        # Output file path
    voice_options: Optional[VoiceOptions],  # Voice settings
    output_format: AudioFormat,             # Audio format (WAV)
    system_prompt: Optional[str]            # Tone control
) -> str  # Returns output path
```

#### generate_speech
```python
client.generate_speech(
    text: str,                              # Text to convert
    voice_options: Optional[VoiceOptions],  # Voice settings
    output_format: AudioFormat,             # Audio format
    system_prompt: Optional[str]            # Tone control
) -> AudioResponse  # Returns audio data in memory
```

### Voice Options

| Voice | Code | Description |
|-------|------|-------------|
| O1 | `Voice.O1` | Soft, melodic |
| O2 | `Voice.O2` | Deep, resonant |
| O3 | `Voice.O3` | Strong, authoritative |
| O4 | `Voice.O4` | Balanced, natural (default) |
| O5 | `Voice.O5` | Warm, expressive |
| O6 | `Voice.O6` | Playful, energetic |

## 📦 Requirements

- Python 3.8 or higher
- Internet connection
- Valid API key

## 🔐 Security Best Practices

1. **Never hardcode API keys:**
```python
# BAD
client = OpenAudioClient(api_key="AIza123...")

# GOOD
import os
client = OpenAudioClient(api_key=os.getenv("OPENAUDIO_API_KEY"))
```

2. **Use .gitignore:**
```bash
# Add to .gitignore
.env
*.wav
api_key.txt
```

3. **Rotate keys regularly**
4. **Use environment-specific keys for dev/prod**

## 🆘 Support

- GitHub Issues: https://github.com/amrhym/openaudio/issues
- PyPI Package: https://pypi.org/project/openaudio/

## 📄 License

MIT License - See LICENSE file for details.