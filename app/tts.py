from gtts import gTTS
from googletrans import Translator

def generate_hindi_tts(text: str, filename: str = "output.mp3") -> str:
    translator = Translator()
    hindi_text = translator.translate(text, dest='hi').text
    
    tts = gTTS(text=hindi_text, lang='hi')
    tts.save(filename)
    return filename
