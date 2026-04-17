import sounddevice as sd
print(sd.query_devices())
import speech_recognition as sr
import wave
import os
sd.default.device = 1  

def get_speech_text():

    fs = 44100 
    duration = 10 

    print("\nSpeak your answer...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    filename = "temp.wav"

    with wave.open(filename, 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(fs)
        f.writeframes(recording.tobytes())

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language="en-IN")
            print("You said:", text)
    except:
        text = ""
        print("Could not understand audio")

    if os.path.exists(filename):
        os.remove(filename)

    return text