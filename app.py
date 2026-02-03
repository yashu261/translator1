import pyttsx3
from googletrans import Translator
import os

class EnglishToKannadaTranslator:
    def __init__(self):
        """Initialize the translator and text-to-speech engine."""
        self.translator = Translator()
        self.engine = pyttsx3.init()
        
        # Configure text-to-speech engine
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume (0-1)
    
    def translate_to_kannada(self, english_text):
        """
        Translate English text to Kannada.
        
        Args:
            english_text (str): Text in English
            
        Returns:
            str: Translated text in Kannada
        """
        try:
            translation = self.translator.translate(english_text, src_language='en', dest_language='kn')
            return translation['text']
        except Exception as e:
            print(f"Translation error: {e}")
            return None
    
    def speak_kannada(self, kannada_text):
        """
        Speak the Kannada text using text-to-speech.
        
        Args:
            kannada_text (str): Text in Kannada to be spoken
        """
        try:
            self.engine.say(kannada_text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")
    
    def translate_and_speak(self, english_text):
        """
        Translate English text to Kannada and speak it.
        
        Args:
            english_text (str): Text in English
        """
        print(f"\n📝 English Text: {english_text}")
        
        # Translate
        kannada_text = self.translate_to_kannada(english_text)
        
        if kannada_text:
            print(f"🇮🇳 Kannada Translation: {kannada_text}")
            print("🔊 Speaking Kannada text...")
            self.speak_kannada(kannada_text)
        else:
            print("Translation failed!")
    
    def interactive_mode(self):
        """Run the translator in interactive mode."""
        print("=" * 50)
        print("🌐 English to Kannada Translator with Speech")
        print("=" * 50)
        print("Commands:")
        print("  'exit' - Quit the program")
        print("  'clear' - Clear screen")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\n📌 Enter English text: ").strip()
                
                if user_input.lower() == 'exit':
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                elif not user_input:
                    print("⚠️  Please enter some text!")
                    continue
                
                self.translate_and_speak(user_input)
                
            except KeyboardInterrupt:
                print("\n\n👋 Program interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")


def main():
    """Main function to run the translator."""
    translator = EnglishToKannadaTranslator()
    
    # Example usage
    print("=" * 50)
    print("Example Translations:")
    print("=" * 50)
    
    examples = [
        "Hello, how are you?",
        "Good morning",
        "Thank you very much",
        "What is your name?"
    ]
    
    for text in examples:
        translator.translate_and_speak(text)
    
    # Interactive mode
    print("\n\n" + "=" * 50)
    translator.interactive_mode()


if __name__ == "__main__":
    main()
