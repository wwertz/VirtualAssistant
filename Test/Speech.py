# C:\Users\WW081114\AppData\Local\Programs\Python\Python310\python.exe -m pip install gTTS
from gtts import gTTS
# This module is imported so that we can play the converted audio
import os

#plays an audio file
class Speech:
    def __init__(self, language, output, tld):
        # Language in which you want to convert
        self.language = language
        self.output = output
        self.tld = tld
        
    def speak(self, mytext):
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        print("Text to speek:", mytext, self.language)
        if self.tld == "":
            myobj = gTTS(text=mytext, lang=self.language, slow=False)
        else:
            myobj = gTTS(text=mytext, lang=self.language, slow=False, tld=self.tld)

        # Saving the converted audio in a wav file named
        myobj.save(self.output)
        playPath = "Start " + self.output
        print("The command is: " + playPath) 

        # Playing the converted file
        os.system(playPath)

#plays audio from cmd
class Speech2:
    def __init__(self, language, output, tld):
        # Language in which you want to convert
        self.language = language
        self.output = output
        
    def speak(self, mytext):
        print("***Speaking:", mytext)
        playPath = "PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + mytext + "');"
        print(playPath) 

        os.system(playPath)