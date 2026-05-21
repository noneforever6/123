import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class GameVoiceTranslator:
    """Translate game voice/text using OpenAI API"""
    
    def __init__(self, source_lang="English", target_lang="Chinese"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.source_lang = source_lang
        self.target_lang = target_lang
        
    def transcribe_audio(self, audio_file_path):
        """
        Convert audio file to text using OpenAI Whisper
        
        Args:
            audio_file_path: Path to audio file (mp3, mp4, mpeg, mpga, m4a, wav, webm)
            
        Returns:
            Transcribed text
        """
        try:
            with open(audio_file_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language="en"  # Can be adjusted based on source language
                )
            return transcript.text
        except Exception as e:
            print(f"Transcription error: {e}")
            return None
            
    def translate_text(self, text, target_lang=None):
        """
        Translate text to target language using OpenAI GPT
        
        Args:
            text: Text to translate
            target_lang: Target language (default: initialized target_lang)
            
        Returns:
            Translated text
        """
        if target_lang is None:
            target_lang = self.target_lang
            
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a translator. Translate the following text to {target_lang}. Only provide the translation, no explanation."
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                temperature=0.3,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Translation error: {e}")
            return None
            
    def process_game_audio(self, audio_file_path):
        """
        Complete pipeline: transcribe audio -> translate -> return result
        
        Args:
            audio_file_path: Path to game audio file
            
        Returns:
            Dictionary with original text and translation
        """
        # Step 1: Transcribe audio
        print("🎤 Transcribing audio...")
        original_text = self.transcribe_audio(audio_file_path)
        
        if not original_text:
            return None
            
        print(f"Original: {original_text}")
        
        # Step 2: Translate text
        print("🌐 Translating...")
        translated_text = self.translate_text(original_text)
        
        if not translated_text:
            return None
            
        print(f"Translated: {translated_text}")
        
        return {
            "original": original_text,
            "translated": translated_text,
            "source_language": self.source_lang,
            "target_language": self.target_lang
        }
