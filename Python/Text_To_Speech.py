from gtts import gTTS
import subprocess

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

    # Use a platform-independent method to play the audio
    try:
        subprocess.call(['xdg-open', output_file])  # Linux
    except FileNotFoundError:
        try:
            subprocess.call(['open', output_file])  # macOS
        except FileNotFoundError:
            subprocess.call(['start', output_file], shell=True)  # Windows

if __name__ == "__main__":
    text = "Hello, this is a text-to-speech conversion example in Python."
    text_to_speech(text)
