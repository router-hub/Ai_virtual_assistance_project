import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

emailData = { "aditya": "adityamanitiwari5","satyam" : "sathyamleo","sourav":"its.sourav","sir":"sumandebcs"}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your assistant sir, please tell me how may I help you")

def takeCommand():
    #takes microphone input and return string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ..")

        query = r.recognize_google(audio, language ="en-in")
        print(f"User said: {query} \n")

    except Exception as e:
        print("say that again please..")
        return "None"
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('fakemail.aiproject@gmail.com','987654321dcba')
    server.sendmail('fakemail.aiproject@gmail.com',to,content)
    server.close()


if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            webbrowser.open('gaana.com')

        
        
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {time}")


        elif 'open visual studio' in query:
            codePath = "C:\\Users\\Amitesh ManiTiwari\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                if 'aditya' in query:
                    to = emailData["aditya"]
                elif 'satyam' in query:
                    to = emailData["satyam"]
                elif 'sourav' or 'saurav' in query:
                    to = emailData["sourav"]
                elif 'sir' in query:
                    to = emailData["sir"]
                
                to = to + "@gmail.com"
                
                sendEmail(to,content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Not sent, sorry!")

        elif 'quit' in query:
            speak("Thank you for using me, sir!")
            break
