import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pywhatkit
import webbrowser
import os
import pyjokes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    time= int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("good morning Boss")
    
    elif time>=12 and time<18:
        speak("good afternoon Boss")
    
    elif time>23:
        speak("Boss what are doing now!")
    
    else:
        speak("good evening Boss")
        
    speak("I am rock, how can i help you")
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "_main_":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break
        
        # elif 'russian' in query:
        #     speak("sir aukat ma raho")
            
        elif 'play' in query:
            print("playing..")
            song=query.replace('play','')
            speak("playing..."+song)
            pywhatkit.playonyt(song)
            break
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            break
            
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("www.google.com")
            break
            
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("whatsapp.com")
            break
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f"the current time is...{strTime}")
        
        elif 'shutdown'in query:
            speak("do you really want to shutdown")
            reply=takeCommand()
            if "yes" in reply:
                os.system("shutdown /s /t 1")
            else:
                break
            
        elif 'restart'in query:
            speak("do you really want to restart")
            reply=takeCommand()
            if "yes" in reply:
                os.system("restart /r /t 1")
            else:
                break
            
        
        elif 'date' in query:
            speak("ofcourse i would love too")
        
        elif 'want to go outside with me' in query:
            speak("yes ofcourse")

        elif 'how are you'in query:
            speak("i am fine whats about you")
            reply=takeCommand()
            if "i am fine"or"i am good" in reply:
                speak("great")
                break
            else:
                break
        
        elif 'coffee' in query:
            speak("yes i would love to go with you akshat")
            
        elif 'take rest' or 'take rest' in query:
            speak("you can call me anytime")
            speak("just tell mahi listen")
            break
        
        elif 'your are so cute' in query:
            speak("thankyou so much love to hear that")
            
        elif 'i love you' in query:
            speak("")
        
        elif 'thankyou' in query:
            speak ("its my pleasure")
            
        
        elif "would you help me" in query:
            speak("yes i am here for you")
            
        elif "quit" in query:
            takeCommand="none"
            
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke(language='en',category="all"))
        
        elif 'stop' in query:
            speak("Thanks Boos")
            break
        
        else :
            speak("I found some information for " + query + " on google")
            webbrowser.open('https://www.google.com/search?q=${query.replace(" ", "+")}', "_blank")
            break