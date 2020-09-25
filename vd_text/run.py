import os
import speech_recognition as sr
command2mp3 = "ffmpeg -i input.mp4 input.mp3"
command2wav = "ffmpeg -i input.mp3 input.wav"
os.system(command2mp3)
os.system(command2wav)
filename="input.wav"
r=sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data=r.record(source)
    text=r.recognize_google(audio_data)
    print("\n\n text from vido is:\n\n",text)