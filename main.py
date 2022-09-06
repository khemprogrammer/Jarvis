import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from distutils.cmd import Command
from tkinter import *
import googletrans
import smtplib
import textblob
from tkinter import ttk,messagebox
import speedtest
import numpy as np
import cv2
import pyautogui as p

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning sir!")
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        print("Good Afternoon sir!")
        speak("Good Afternoon sir!")

    else:
        print("Good Evening sir!")
        speak("Good Evening sir!")

    print("I am Mazdur . Please tell me how may I help you sir")
    speak("I am Maazduur . Please tell me how may I help you sir k gardai ho")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def TaskExecution():
    p.press('esc')
    speak("Verification successful")
    print("Verification successful")
    speak("welcome back khem sir")
    print("welcome back khem sir")
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # test me
        elif 'who is' in query or 'how to' in query or 'what is' in query:
            speak('Searching Wikipedia...')
            resultsw = wikipedia.summary(query, sentences=2)
            speak("sir,")
            print(resultsw)
            speak(resultsw)
            speak("that's it")

        elif "google translation" in query:
            root = Tk()
            root.geometry("880x300")


            def translate_it():
                translate_text.delete(1.0, END)
                try:
                    for key, value in languages.items():
                        if (value == original_combo.get()):
                            from_language_key = key

                    for key, value in languages.items():
                        if (value == translated_combo.get()):
                            to_language_key = key
                    words = textblob.TextBlob(original_text.get(1.0, END))
                    words = words.translate(from_lang=from_language_key, to=to_language_key)
                    translate_text.insert(1.0, words)
                except Exception as e:
                     messagebox.showerror("translator", e)


            def clear():
                original_text.delete(1.0, END)
                translate_text.delete(1.0, END)


            languages = googletrans.LANGUAGES
            language_list = list(languages.values())

            original_text = Text(root, height=10, width=40)
            original_text.grid(row=0, column=0, pady=20, padx=10)

            translate_button = Button(root, text="translate!", font=("Helvetica", 24), command=translate_it)
            translate_button.grid(row=0, column=1, padx=10)

            translate_text = Text(root, height=10, width=40)
            translate_text.grid(row=0, column=2, pady=20, padx=10)

            original_combo = ttk.Combobox(root, width=50, value=language_list)
            original_combo.current(21)
            original_combo.grid(row=1, column=0)

            translated_combo = ttk.Combobox(root, width=50, value=language_list)
            translated_combo.current(68)
            translated_combo.grid(row=1, column=2)

            clear_button = Button(root, text="Clear", command=clear)
            clear_button.grid(row=2, column=1)

            root.mainloop()


        elif "internet speed" in query:
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
            download_net = wifi.download() / 1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ", download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'who are you' in query or 'about you' in query or "your details" in query:
            speak("i am your work partner. sir, i work for you.")

        elif 'how are you' in query or 'fill you' in query or "filling" in query:
            speak("i am your fine. sir, can i help you.")

        elif 'exit' in query or 'goodbye' in query or 'good bye' in query or 'bye' in query:
            speak("thank you sir. good bye .")
            quit()

        elif 'thank you' in query or 'thanks' in query:
            speak("No problem sir.")

        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello  Sir ! How May i Help you.."
            print(hel)
            speak(hel)

        elif 'clean' in query:
            speak("ok.")
            def clear():
                return os.system('cls')
            clear()

        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query or 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)
        #
        # elif 'email to harry' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "harryyourEmail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")

#face recognition
if __name__ == "__main__":
    
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 2 #number of persons you want to Recognize


    names = ['','khem']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                TaskExecution()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
            cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

        # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()