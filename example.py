"""
Example usage of OpenAudio SDK
This demonstrates how to use the SDK without exposing any Gemini implementation details
"""

from openaudio import OpenAudioClient, VoiceOptions, Voice, AudioFormat

def main():
    # Initialize the OpenAudio client
    # API key can be passed or use default environment variable
    client = OpenAudioClient()
    
    # Example 1: Simple text-to-speech with default voice
    print("Example 1: Simple TTS with default voice")
    client.generate_speech_to_file(
        text="Hello! Welcome to OpenAudio SDK. This is a simple text to speech example.",
        output_path="example1_default.wav"
    )
    print("✓ Saved to example1_default.wav\n")
    
    # Example 2: Using different voices
    print("Example 2: Using different voices")
    voice_options = VoiceOptions(voice=Voice.O6)
    client.generate_speech_to_file(
        text="This is using the O6 voice. Each voice has its own unique characteristics.",
        output_path="example2_o6_voice.wav",
        voice_options=voice_options
    )
    print("✓ Saved to example2_o6_voice.wav\n")
    
    # Example 3: With system prompt for specific tone
    print("Example 3: Using system prompt for cheerful tone")
    client.generate_speech_to_file(
        text="Have a wonderful day!",
        output_path="example3_cheerful.wav",
        system_prompt="Say cheerfully"
    )
    print("✓ Saved to example3_cheerful.wav\n")
    
    # Example 4: Getting audio data in memory
    print("Example 4: Getting audio data in memory")
    response = client.generate_speech(
        text="This audio is generated in memory without saving to a file.",
        voice_options=VoiceOptions(voice=Voice.O1)
    )
    print(f"✓ Generated {len(response.audio_data)} bytes of audio data")
    print(f"  Format: {response.format.value}")
    print(f"  Text: {response.text}\n")
    
    # Example 5: Multiple languages
    print("Example 5: Multiple languages")
    texts = [
        ("Hello, how are you?", "english.wav"),
        ("Bonjour, comment allez-vous?", "french.wav"),
        ("Hola, ¿cómo estás?", "spanish.wav"),
        ("مرحبا، كيف حالك؟", "arabic.wav"),
    ]
    
    for text, filename in texts:
        client.generate_speech_to_file(
            text=text,
            output_path=filename,
            voice_options=VoiceOptions(voice=Voice.O2)
        )
        print(f"✓ Generated {filename}: {text}")
    
    print("\nAll examples completed successfully!")

if __name__ == "__main__":
    main()