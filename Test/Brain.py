from Communication.Mail import Mail
from Listen import Listen
from Speech import Speech, Speech2
from Write import WriteSpeech
from Basic.Weather import Weather
from Profile.User import User

import json
import time
from datetime import date

class Brain:
    def __init__(self, isOn):
        self.isOn = isOn
        self.z = Speech2("en", "SpeechAudio.wav", "")
        self.outputFile = "Input.wav"
        self.x = Listen(1024, "FORMAT", 2, 44100, 5, self.outputFile) 
        self.y = WriteSpeech()

        #get data for user profile
        myFile = open('Data/Profile.json')
        myUser = json.load(myFile)
        self.user = User(myUser["Profile"]["userName"], myUser["Profile"]["userEmail"], myUser["Profile"]["userPassword"], myUser["Profile"]["userDOB"])

    def setIsOn(self, isOn):
        self.isOn = isOn

    def getText(self):
        x = Listen(1024, "FORMAT", 2, 44100, 5, self.outputFile) 
        x.myRecord()
        x.myStop()
        readText = ""
        readText = self.y.myWrite(self.outputFile)
        return readText

    def waitForCommand(self):
        while self.isOn:
            #readText = ""
            readText = self.getText()
            
            if readText.find('hey listen') != -1 or readText.find('Hey listen') != -1:
                self.z.speak("Hello " + self.user.userName)

                readText = self.getText()
                self.doCommand(readText)

    def doCommand(self, readText):
        print("doing command based on audio")
                
        #Give time
        if readText.find('what') != -1 and readText.find('time') != -1: 
            tempVar = time.strftime("%H:%M:%S", time.localtime())
            xspeak = ("Current Time is, " + str(tempVar))   
            print(xspeak) 
            self.z.speak(xspeak)

        #Give date
        if readText.find('what') != -1 and readText.find('date') != -1: 
            tempVar = date.today()
            xspeak = ("Todays date is, " + str(tempVar))   
            print(xspeak) 
            self.z.speak(xspeak)

        #Give weather
        if readText.find('what') != -1 and readText.find('weather') != -1:
            xcity = "Kansas City"
            xWeather = Weather() 
            tempVar = xWeather.getWeather(xcity)
            print(tempVar)
            xspeak = ("The current weather for " + xcity + " is " + tempVar)    
            self.z.speak(xspeak)

        #Turn off
        if readText.find('turn') != -1 and readText.find('off') != -1 or readText.find('quit') != -1 or readText.find('stop') != -1:
            self.isOn = False
            self.z.speak("goodbye")
       
        #Send email
        if readText.find('send') != -1 and readText.find('mail') != -1 or readText.find('email') != -1: 
            self.z.speak("What do you want to say?")
            message = self.getText()

            xspeak = ("You want to send, " + str(message) + ". Is this correct?")   
            print(xspeak) 
            self.z.speak(xspeak)  

            answer = self.getText()

            if answer.find('yes') != -1 or answer.find('yea') != -1 or answer.find('send') != -1:
                m = Mail(self.user.userEmail, self.user.userPassword)
                m.send("wpwertz@gmail.com", message)
                self.z.speak("OK, its done")
            elif answer.find('no') != -1 or answer.find('nope') != -1 or answer.find('dont send') != -1:
                self.z.speak("I wont")
            else:
                 self.z.speak("I didnt get that. I am not sending") 

