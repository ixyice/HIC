import pyttsx3 as p
import speech_recognition as sr
import datetime
import wikipedia as wiki
import webbrowser as wb


def take_command ():
    r = sr. Recognizer()

    with sr.Microphone () as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise (source, 1.2)
        audio = r.listen (source)

    try:
        print("Recognizing...")
        query = r. recognize_google (audio)
        print("You said: ", query)
    except Exception as e:
        print(e)
        print("Please, say that again.")
        return "None"

    return query

#function for system response

def speak(audio):
    engine = p.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


#Function for reporting the current system day:

def tell_day():
    day = datetime.datetime.today().weekday() + 1 
    Day_dict = {1:  'Monday' , 2: 'Tuesday' , 3: 'Wednesday' , 4: 'Thursday' , 5: 'Friday' , 6: 'Saturday' , 7: 'Sunday' }

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

#function report for current system time
def tell_time():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11.13]
    min = time[14.16]
    speak("The Time is " + hour + "Hours and " + min + "minutes")

#Function for giving information form Wikipedia
def hello():
    speak("Hello sire")


def intro_self():
    speak(" I am not me")



#Function for giving information form Wikipedia:
def give_info():
    speak("What information do you want sir")
    query = take_command().lower()

    try:
        result = wiki.summary(query, sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)

    except Exception as e:
        print(e)
        print("Sorry, error found reading the topic.")

#Function for taking query from the user:

def take_query():
    hello()

    while(True):
        query = take_command().lower()
        if "day" and "today" in query:
            tell_day()
            continue
        elif "time" and "now" in query:
            tell_time()
            continue
        elif "open google" in query:
            speak ("Opening google")
            wb.open("www.google.com")
            speak("is there anything you want sir?")
            continue
        elif "your name" and "who are you" in query:
            intro_self()
            continue
        elif "stop" and "exit" and "nothing" in query:
            speak ("Thank you and have a nice day.")
            exit()
        elif "information" in query:
            query = query.replace("information", "")
            give_info()
            speak("is there anything you want sir?")
            continue
        else:
            speak ("Sorry, thats an unrecognized command for me")
            continue

#Main class declaration

if __name__ == '__main__':
    query = "none"
    take_query()