#!/usr/bin/env python
"""
OpenAudio SDK - Quick Start Example
Run this script to test the SDK quickly
"""

import os
import sys

# Check if openaudio is installed
try:
    from openaudio import OpenAudioClient, VoiceOptions, Voice
except ImportError:
    print("OpenAudio SDK is not installed.")
    print("Install it with: pip install openaudio")
    sys.exit(1)

def main():
    print("=" * 50)
    print("OpenAudio SDK - Quick Start")
    print("=" * 50)
    
    # Get API key
    api_key = os.getenv("OPENAUDIO_API_KEY")
    
    if not api_key:
        print("\nNo API key found in environment.")
        print("Please enter your API key (get one from https://aistudio.google.com/apikey):")
        api_key = input("API Key: ").strip()
    
    if not api_key:
        print("Error: API key is required")
        sys.exit(1)
    
    try:
        # Initialize client
        print("\nInitializing OpenAudio client...")
        client = OpenAudioClient(api_key=api_key)
        
        # Test 1: Basic TTS
        print("\n1. Testing basic text-to-speech...")
        client.generate_speech_to_file(
            text="Hello! This is a test of the OpenAudio SDK. It's working perfectly!",
            output_path="test_basic.wav"
        )
        print("   ✓ Generated: test_basic.wav")
        
        # Test 2: Different voice
        print("\n2. Testing with O6 (playful) voice...")
        client.generate_speech_to_file(
            text="This is the playful O6 voice. Isn't it fun?",
            output_path="test_voice_o6.wav",
            voice_options=VoiceOptions(voice=Voice.O6)
        )
        print("   ✓ Generated: test_voice_o6.wav")
        
        # Test 3: System prompt for tone
        print("\n3. Testing cheerful tone...")
        client.generate_speech_to_file(
            text="Have a wonderful day!",
            output_path="test_cheerful.wav",
            system_prompt="Say cheerfully"
        )
        print("   ✓ Generated: test_cheerful.wav")
        
        # Test 4: Multiple languages
        print("\n4. Testing multiple languages...")
        languages = [
            ("Hello, how are you?", "test_english.wav"),
            ("Bonjour, comment allez-vous?", "test_french.wav"),
            ("Hola, ¿cómo estás?", "test_spanish.wav")
        ]
        
        for text, filename in languages:
            client.generate_speech_to_file(text=text, output_path=filename)
            print(f"   ✓ Generated: {filename}")
        
        print("\n" + "=" * 50)
        print("SUCCESS! All tests passed!")
        print("=" * 50)
        print("\nGenerated audio files:")
        print("  - test_basic.wav")
        print("  - test_voice_o6.wav")
        print("  - test_cheerful.wav")
        print("  - test_english.wav")
        print("  - test_french.wav")
        print("  - test_spanish.wav")
        
        print("\nYou can now use the SDK in your projects!")
        print("\nExample code:")
        print("-" * 30)
        print('from openaudio import OpenAudioClient')
        print(f'client = OpenAudioClient(api_key="{api_key[:10]}...")')
        print('client.generate_speech_to_file("Your text", "output.wav")')
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("1. Check your API key is correct")
        print("2. Ensure you have internet connection")
        print("3. Try reinstalling: pip install --upgrade openaudio")
        sys.exit(1)

if __name__ == "__main__":
    main()