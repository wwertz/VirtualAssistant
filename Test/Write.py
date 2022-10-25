#import library: C:\Users\WW081114\AppData\Local\Programs\Python\Python310\python.exe -m pip install SpeechRecognition
import speech_recognition as sr

class WriteSpeech:
    def __init__(self):
        # Initialize recognizer class (for recognizing the speech)
        self.r = sr.Recognizer()

    def myWrite(self, myRecording):
        # Reading Audio file as source
        # listening the audio file and store in audio_text variable

        with sr.AudioFile(myRecording) as source:
    
            audio_text = self.r.listen(source)
    
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
        
        # using google speech recognition
                text = self.r.recognize_google(audio_text)
                print('Converting audio transcripts into text ...')
                print(text)
                return text
            except:
                print('***Try again, not word found***')
                return ""
