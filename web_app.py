from flask import Flask, render_template, request, jsonify
import pyttsx3
from googletrans import Translator
import threading
import asyncio
from inspect import iscoroutinefunction

app = Flask(__name__)

class EnglishToKannadaTranslator:
    def __init__(self):
        """Initialize the translator and text-to-speech engine."""
        self.translator = Translator()
        self.engine = pyttsx3.init()
        
        # Configure text-to-speech engine
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume (0-1)
    
    def translate_to_kannada(self, english_text):
        """Translate English text to Kannada.

        Works with both async and sync `Translator.translate` implementations.
        Returns the translated string or `None` on error.
        """
        try:
            translate_fn = self.translator.translate

            if iscoroutinefunction(translate_fn):
                loop = asyncio.new_event_loop()
                try:
                    translation = loop.run_until_complete(translate_fn(english_text, src='en', dest='kn'))
                finally:
                    loop.close()
            else:
                translation = translate_fn(english_text, src='en', dest='kn')

            # translation may be an object with .text or a dict/list
            if isinstance(translation, list):
                translation = translation[0]

            text = None
            if hasattr(translation, 'text'):
                text = translation.text
            elif isinstance(translation, dict):
                text = translation.get('text')

            return text
        except Exception as e:
            print(f"Translation error: {e}")
            return None
    
    def speak_kannada(self, kannada_text):
        """Speak the Kannada text using text-to-speech."""
        try:
            self.engine.say(kannada_text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")

# Initialize translator
translator = EnglishToKannadaTranslator()

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    """Translate English text to Kannada."""
    data = request.json
    english_text = data.get('text', '').strip()
    
    if not english_text:
        return jsonify({'error': 'Please enter some text'}), 400
    
    try:
        kannada_text = translator.translate_to_kannada(english_text)
        
        if kannada_text:
            return jsonify({
                'success': True,
                'english': english_text,
                'kannada': kannada_text
            })
        else:
            return jsonify({'error': 'Translation failed. Try again.'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/speak', methods=['POST'])
def speak():
    """Speak the Kannada text."""
    data = request.json
    kannada_text = data.get('text', '').strip()
    
    if not kannada_text:
        return jsonify({'error': 'No text to speak'}), 400
    
    try:
        # Run speech in a separate thread to avoid blocking
        thread = threading.Thread(target=translator.speak_kannada, args=(kannada_text,))
        thread.daemon = True
        thread.start()
        
        return jsonify({'success': True, 'message': 'Speaking...'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
