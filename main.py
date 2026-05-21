#!/usr/bin/env python3
"""
Real-time Game Voice Translator
Translates game voice/audio to multiple languages in real-time
"""

import os
import sys
from dotenv import load_dotenv
from translator import GameVoiceTranslator
from audio_recorder import AudioRecorder
import time
import numpy as np
import wave

load_dotenv()

class RealTimeGameTranslator:
    """Main application for real-time game voice translation"""
    
    def __init__(self, source_lang="English", target_lang="Chinese"):
        self.translator = GameVoiceTranslator(source_lang, target_lang)
        self.recorder = AudioRecorder()
        self.is_running = False
        
    def save_audio_buffer(self, audio_buffer, filename="game_audio.wav"):
        """Save audio buffer to WAV file"""
        sample_rate = 16000
        try:
            with wave.open(filename, 'wb') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(sample_rate)
                # Convert float32 to int16
                audio_int16 = (audio_buffer * 32767).astype(np.int16)
                wav_file.writeframes(audio_int16.tobytes())
            return filename
        except Exception as e:
            print(f"Error saving audio: {e}")
            return None
            
    def start_translation(self, duration=5):
        """
        Start recording and translating game voice
        
        Args:
            duration: Recording duration in seconds
        """
        print(f"🎮 Game Voice Translator Started")
        print(f"Recording for {duration} seconds...")
        print("Speak now!\n")
        
        self.recorder.start_recording()
        time.sleep(duration)
        self.recorder.stop_recording()
        
        # Get audio buffer
        audio_buffer = self.recorder.get_audio_buffer()
        
        if len(audio_buffer) == 0:
            print("❌ No audio recorded")
            return None
            
        # Save audio to WAV file
        audio_file = self.save_audio_buffer(audio_buffer)
        
        if not audio_file:
            print("❌ Failed to save audio")
            return None
            
        # Translate
        result = self.translator.process_game_audio(audio_file)
        
        # Clean up
        if os.path.exists(audio_file):
            os.remove(audio_file)
            
        return result
        
    def interactive_mode(self):
        """Run in interactive mode for multiple translations"""
        print("\n" + "="*50)
        print("🎮 Game Voice Translator - Interactive Mode")
        print("="*50)
        print("Commands:")
        print("  'record' - Record and translate game voice (5s)")
        print("  'lang' - Change target language")
        print("  'quit' - Exit")
        print("="*50 + "\n")
        
        while True:
            command = input("Enter command: ").strip().lower()
            
            if command == "quit":
                print("Goodbye! 👋")
                break
                
            elif command == "record":
                result = self.start_translation(duration=5)
                if result:
                    print(f"\n✅ Translation Complete!")
                    print(f"Source ({result['source_language']}): {result['original']}")
                    print(f"Target ({result['target_language']}): {result['translated']}\n")
                    
            elif command == "lang":
                lang = input("Enter target language (e.g., Chinese, Spanish, Japanese): ").strip()
                self.translator.target_lang = lang
                print(f"Target language changed to: {lang}\n")
                
            else:
                print("Unknown command. Try again.\n")

def main():
    """Main entry point"""
    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key")
        print("See .env.example for reference")
        sys.exit(1)
        
    # Initialize translator
    translator = RealTimeGameTranslator(
        source_lang="English",
        target_lang="Chinese"
    )
    
    # Run interactive mode
    translator.interactive_mode()

if __name__ == "__main__":
    main()
