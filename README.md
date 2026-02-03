# English to Kannada Translator with Speech

A modern web application that translates English text to Kannada and provides text-to-speech functionality.

## Features

✨ **Core Features:**
- 🌐 Real-time English to Kannada translation
- 🔊 Text-to-speech pronunciation in Kannada
- 📋 Copy translation to clipboard
- ✅ Clean and modern web interface
- 📱 Responsive design (works on desktop and mobile)
- ⚡ Fast and lightweight

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Steps

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```powershell
   python web_app.py
   ```

3. **Open in browser:**
   - Navigate to `http://localhost:5000`
   - The web interface will load automatically

## Usage

1. **Enter English Text:**
   - Type or paste English text in the input area (max 500 characters)
   - Character count displays in real-time

2. **Translate:**
   - Click the "Translate" button
   - Or press `Ctrl+Enter` for quick translation

3. **Hear the Pronunciation:**
   - Click the "Speak" button to hear the Kannada pronunciation
   - Uses text-to-speech synthesis

4. **Copy Translation:**
   - Click the "Copy" button to copy the Kannada text to clipboard

## Project Structure

```
translator1/
├── web_app.py              # Flask backend application
├── app.py                  # Original CLI translator
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Main web interface
└── static/
    ├── style.css          # Styling and responsive design
    └── script.js          # Frontend functionality
```

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Translation:** Google Translate API (googletrans)
- **Text-to-Speech:** pyttsx3 (offline TTS engine)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)

## API Endpoints

### POST /translate
Translate English text to Kannada

**Request:**
```json
{
  "text": "Hello, how are you?"
}
```

**Response:**
```json
{
  "success": true,
  "english": "Hello, how are you?",
  "kannada": "ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?"
}
```

### POST /speak
Play text-to-speech for Kannada text

**Request:**
```json
{
  "text": "ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Speaking..."
}
```

## Keyboard Shortcuts

- **Ctrl+Enter:** Translate the current text
- **Tab:** Navigate between elements

## Troubleshooting

**Issue: Module not found error**
- Solution: Make sure all dependencies are installed: `pip install -r requirements.txt`

**Issue: Port 5000 already in use**
- Solution: Edit `web_app.py` and change the port number in the last line

**Issue: Text-to-speech not working**
- Solution: Install pyttsx3 separately: `pip install pyttsx3 --upgrade`

## Limitations

- Translation quality depends on Google Translate API
- Text-to-speech works offline but may have limited Kannada voice support on some systems
- Maximum input length: 500 characters

## Future Enhancements

- [ ] Add reverse translation (Kannada to English)
- [ ] Support multiple languages
- [ ] History of translations
- [ ] User preferences/settings
- [ ] Dark mode toggle
- [ ] Translation accuracy statistics
- [ ] Offline mode with local translation models

## License

This project is open source and available under the MIT License.

## Author

Created: February 2026

---

**Enjoy translating! 🚀**