import pyttsx3 
import wikipedia
import os
fullpath=os.path.join(os.getcwd(),'bar.wav')
"""google voice search"""
# voice=pyttsx3.init()
# In=input("searching wikipedia/google: ")
# result=wikipedia.summary(In,sentences=3)
# print(result)
# voice.say(result)
# voice.runAndWait()
""" RATE"""
engine = pyttsx3.init()
engine.say('Im sick of them sweatsuits and them corny hats lets talk about it Im sick of you bein rich and you still mad, lets talk about it Both of us single dads from the Midwest, we can talk about it' +'str(rate)')
rate=engine.getProperty('rate')
print(rate)
engine.setProperty('rate',125)
engine.runAndWait()

"""volume"""
volume=engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)
engine.runAndWait()

"""voice"""
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id) 
# """id [0] for male"""
engine.setProperty('voice',voices[1].id)    
# """id[1] for female"""
engine.runAndWait()

"""saving voice to any file"""
engine.save_to_file(fullpath)
engine.runAndWait()
