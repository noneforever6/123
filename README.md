# 🎮 Real-time Game Voice Translator

A Python-based real-time translation software that translates game voice/audio to multiple languages using OpenAI's Whisper and GPT models.

## Features

✨ **Key Features:**
- 🎤 Real-time audio recording from microphone
- 🗣️ Speech-to-text transcription using OpenAI Whisper
- 🌐 Multi-language translation using GPT
- 🎮 Optimized for game voice translation
- 💬 Interactive command-line interface
- ⚡ Fast and accurate translations

## Requirements

- Python 3.8+
- OpenAI API key
- Microphone (for audio input)
- PyAudio library

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/noneforever6/123.git
cd 123
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup OpenAI API Key
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx
SOURCE_LANGUAGE=en
TARGET_LANGUAGE=zh
```

Get your API key from: https://platform.openai.com/api-keys

## Usage

### Run the application
```bash
python main.py
```

### Interactive Mode Commands
- `record` - Record and translate game voice (5 seconds)
- `lang` - Change target language
- `quit` - Exit the application

### Example
```
🎮 Game Voice Translator Started
Recording for 5 seconds...
Speak now!

🎤 Transcribing audio...
Original: The enemy is approaching from the north

🌐 Translating...
Translated: 敌人从北方接近

✅ Translation Complete!
```

## Module Overview

### `translator.py`
Main translation module with OpenAI integration:
- `GameVoiceTranslator` - Main class for handling translations
- `transcribe_audio()` - Convert audio to text using Whisper
- `translate_text()` - Translate text using GPT
- `process_game_audio()` - Complete pipeline

### `audio_recorder.py`
Real-time audio recording:
- `AudioRecorder` - Handles microphone input
- `start_recording()` - Begin recording
- `get_audio_buffer()` - Retrieve recorded audio
- `stop_recording()` - End recording

### `main.py`
Main application interface:
- `RealTimeGameTranslator` - Application controller
- `interactive_mode()` - Interactive CLI
- `start_translation()` - Begin translation process

## Supported Languages

Works with any language supported by OpenAI's Whisper and GPT models:
- English, Chinese, Spanish, French, German, Japanese, Korean, Russian, Portuguese, Italian, Dutch, Polish, Turkish, Indonesian, Thai, Vietnamese, and more

## Configuration

Edit `.env` to customize:
```
OPENAI_API_KEY=your_api_key
SOURCE_LANGUAGE=en          # Source language
TARGET_LANGUAGE=zh          # Target language
```

## Performance Tips

1. **GPU Support**: Enable GPU acceleration for faster processing
2. **API Costs**: Monitor API usage as Whisper and GPT are pay-per-use
3. **Audio Quality**: Use a good quality microphone for better transcription accuracy
4. **Language Codes**: Specify language codes for better accuracy (e.g., "en" for English)

## Troubleshooting

### Issue: "OPENAI_API_KEY not found"
**Solution**: Make sure your `.env` file exists and contains a valid API key

### Issue: "No module named 'pyaudio'"
**Solution**: Install PyAudio
```bash
pip install pyaudio
```

On macOS:
```bash
brew install portaudio
pip install pyaudio
```

### Issue: "No audio recorded"
**Solution**: 
- Check microphone is connected and working
- Check audio permissions in system settings
- Try adjusting buffer size in `AudioRecorder`

### Issue: Low translation accuracy
**Solution**:
- Speak clearly and slowly
- Use a better microphone
- Specify source language in `transcribe_audio()`
- Increase recording duration

## API Usage & Costs

This project uses OpenAI APIs:
- **Whisper API**: ~$0.02 per minute of audio
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens

Monitor your usage at: https://platform.openai.com/usage

## Advanced Usage

### Custom Language Pairs
```python
translator = GameVoiceTranslator(
    source_lang="Japanese",
    target_lang="English"
)
```

### Batch Processing
```python
translator = GameVoiceTranslator()
for audio_file in audio_files:
    result = translator.process_game_audio(audio_file)
```

## Future Enhancements

- [ ] Real-time streaming translation
- [ ] Text-to-speech for translated audio
- [ ] Game overlay integration
- [ ] Multiple language simultaneous translation
- [ ] Audio file batch processing
- [ ] Translation history and caching
- [ ] Web UI dashboard

## License

MIT License - feel free to use and modify

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please create a GitHub issue in the repository.

---

Made with ❤️ for gamers
