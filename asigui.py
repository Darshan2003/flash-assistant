from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
joke=["I went to the zoo the other day. There was only a dog in it – it was a shihtzu.","I asked my 91-year-old father, “Dad, what were your good old days?” His thoughtful reply: “When I wasn’t good, and I wasn’t old.” ","harry: I have the perfect son. Ben: Does he smoke? harry: No, he doesn't. Ben: Does he drink whiskey? harry: No, he doesn't. Ben: Does he ever come home late? harry: No, he doesn't. Ben: I guess you really do have the perfect son. How old is he? harry: He will be six months old next Wednesday."]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    start.withdraw()
    root.deiconify()
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Flash, How can i help you")
    

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        r.energy_threshold=350
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
    
        query=r.recognize_google(audio, language='en-in')
        st.insert(INSERT,"You : "+str(query)+"\n")
    
    except Exception as e:
        st.insert(INSERT,"Flash : Say that again please...\n")
        speak("Say that again please...")
        return "None"
    
    query=query.lower()
        
    if 'wikipedia'in query:
        st.insert(INSERT,"Flash : Searching Wikipedia...\n")
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        st.insert(INSERT,"Flash : "+str(results)+"\n")
        speak(results)
    
    elif 'who is a your boyfriend' in query:
        st.insert(INSERT,"Flash : Firstly I am a boy,so i can't have boyfriend\n")
        speak("Firstly I am a boy,so i can't have boyfriend")

    elif 'do you have a boyfriend' in query:
        st.insert(INSERT,"Flash : Firstly I am a boy,so i can't have boyfriend\n")
        speak("Firstly I am a boy,so i can't have boyfriend")

    elif 'who is a your girlfriend' in query:
        st.insert(INSERT,"Flash : No, I am still searching\n")
        speak("No, I am still searching")
    elif 'do you have a girlfriend' in query:
        st.insert(INSERT,"Flash : No, I am still searching\n")
        speak("No, I am still searching")


    elif 'the time' in query:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        a=time.split(":")
        st.insert(INSERT,"Flash : Sir, the time is "+str(time)+"\n")
        speak("Sir, the time is"+str(a[0])+"hours"+str(a[1])+"minutes"+str(a[2])+"seconds")
    
     

    elif 'who are you' in query:
        st.insert(INSERT,"Flash : My name is Flash, and I am your assistant robot\n")
        speak("My name is Flash, and I am your assistant robot")
        
    elif 'what is your name' in query:
        st.insert(INSERT,"Flash : My name is Flash, and I am your assistant robot\n")
        speak("My name is Flash, and I am your assistant robot")
        

    elif 'meaning' in query:
        query=query.replace("meaning", "")
        results=wikipedia.summary(query, sentences=1)
        st.insert(INSERT,"Flash : "+str(results)+"\n")
        speak(results)
    
    elif 'what is ' in query:
        query=query.replace("what is a", "")
        results=wikipedia.summary(query, sentences=1)
        st.insert(INSERT,"Flash : "+str(results)+"\n")
        speak(results)
    
     
    elif 'who is' in query:
        query=query.replace("who is", "")
        results=wikipedia.summary(query, sentences=1)
        st.insert(INSERT,"Flash : "+str(results)+"\n")
        speak(results)
    
    
    elif 'open youtube' in query:
        st.insert(INSERT,"Flash : Opening...\n")
        speak('Opening...')
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        st.insert(INSERT,"Flash : Opening...\n")
        speak('Opening...')
        webbrowser.open("google.com")
    
    elif 'open visual studio code' in query:
        st.insert(INSERT,"Flash : Opening...\n")
        speak('Opening...')
        os.startfile("C:\\Users\\drish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        

    elif 'play music' in query:
        st.insert(INSERT,"Flash :Opening wynk music\n")
        speak('Opening wink music')
        
    
        
   
    elif 'joke' in query:
        r=random.randrange(len(joke))
        st.insert(INSERT,"Flash : "+joke[r]+"\n")
        speak(joke[r])
        speak("haah haah haah")
            
    elif 'exit' in query:
        st.insert(INSERT,"Flash : Have a good day\n")
        speak("Have a good day")
        root.destroy()

    elif 'close' in query:
        st.insert(INSERT,"Flash : Have a good day\n")
        speak("Have a good day")
        root.destroy()
    elif 'bye' in query:
        st.insert(INSERT,"Flash : Have a good day\n")
        speak("Have a good day")
        root.destroy()
    elif 'search' in query:
        query=query.replace("search","")
        query=query.replace(" ","+")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.com/search?hl=en-US&sxsrf=ALeKk01SaLQKGKz-WYOKdbOJoNMttZ65MQ%3A1603795654676&source=hp&ei=xvqXX5TbJrmX4-EPqM6VoAk&iflsig=AINFCbYAAAAAX5gI1iFf3RosTM6YqET9gLYb66yuD-o2&q="+(query)+"&oq="+(query)+"&gs_lcp=CgZwc3ktYWIQAzIICAAQsQMQyQMyAggAMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzICCAAyBQguELEDMgIIADIFCAAQsQM6BAgjECc6CAgAELEDEIMBOgIILlDOIFjAK2CXLmgAcAB4AIAB0wGIAd4IkgEFMC40LjKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiU1qWyzNTsAhW5yzgGHShnBZQQ4dUDCAY&uact=5")
        speak("Searching..")
        st.insert(INSERT,"Flash: Searching...")
    else:
        st.insert(INSERT,"Flash : Sorry I didn't get that!\n")
        speak("Sorry I didn't get that!")
    

start=Tk()
start.title("Flash AI")
start.geometry("400x400+500+200")
startbtn=Button(start,text="Start",font=('arial',13,'bold'),width=10,command=wishme,foreground='purple',background='white')
startbtn.place(x=145,y=160)

start.configure(background='purple')
root=Toplevel(start)
root.title("Flash AI")
root.geometry("400x400+500+200")




st=ScrolledText(root,width=32,height=14,font=('arial',14,'bold'),wrap='word')
bt=Button(root,text="Talk",font=('arial',13,'bold'),width=10,command=takecommand,foreground='purple',background='white')

st.pack(pady=(10,5))
bt.pack(pady=(14,5))
root.configure(background='purple')
root.withdraw()
start.mainloop()
