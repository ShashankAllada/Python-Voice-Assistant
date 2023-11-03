#"Soni" operates continuously until explicitly stopped. 
#It is designed for tasks that require ongoing or repeated execution. 
#"Soni" can be initiated and will run in a loop, and you can stop its operation at any time by issuing a "stop command." 
#This allows for continuous or interactive processes that run as long as needed.

# Import necessary libraries for speech recognition, text-to-speech, and other functionalities.
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

# Initialize speech recognition, text-to-speech engine, and set the voice.
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak text using the text-to-speech engine.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet the user based on the time of day.
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 1 and hour < 12:
        print("A very good morning sir! ")
        speak("A very good morning sir! ")

    elif hour >= 12 and hour < 16:
        print("A very good afternoon sir! ")
        speak("A very good afternoon sir! ")

    else:
        print("A very good evening sir! ")
        speak("A very good evening sir! ")

    print("Iam Soni how may I help you?")
    speak("Iam Soni how may I help you?")

# Define a function to process user commands.
def start_command(command):
    # Process different user commands based on keywords.
    if "Play" or "play" in command:
        # Ask the user what to play and play it on YouTube.
        speak("What do you want me to play? ")
        something = start_command()  # Recursive call to get user input.
        print('playing ' + something)
        speak('playing ' + something)
        pywhatkit.playonyt(something)  # Play the requested content on YouTube.

    elif "news" in command:
        # Retrieve and play the latest news from YouTube.
        print('Todays news are ')
        speak('Todays news are ')
        pywhatkit.playonyt("Today's news")

    elif "tell" in command:
        # Provide information on a topic using Wikipedia.
        p = command.replace("tell me about", "")
        speak("According to Wikipedia")
        print(wikipedia.summary(p, 2))
        speak(wikipedia.summary(p, 2))

    elif 'time' in command:
        # Get and announce the current time.
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        speak('Current time is ' + time)

    elif 'today' in command:
        # Get and announce the current date.
        time = datetime.datetime.now().strftime("%A %dth %B %Y")
        print('Today is ' + time)
        speak('Today is ' + time)

    elif 'joke' in command:
        # Tell a random joke.
        speak(pyjokes.get_joke())

    elif 'Google' in command:
        # Open a web browser and navigate to Google.
        webbrowser.open("google.com")

    elif 'file' in command:
        # List files in a directory and open the first file.
        dir = "D:\Third year sem 2"
        file = os.listdir(dir)
        print(file)
        os.startfile(os.path.join(dir, file[0]))

    elif "message" in command:
        # Send a WhatsApp message to a specified phone number.
        print("Please enter the phone number below, to send the message ")
        speak("Please enter the phone number below, to send the message ")
        number = "+91" + input()
        speak("What message do you want me to send?")
        message = start_command()  # Recursive call to get user input.
        print("Messaging" + message)
        speak("Messaging" + message)
        pywhatkit.sendwhatmsg(number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 10, True, 2)

    else:
        pass  # Handle unrecognized commands.
   

# Greet the user at the beginning.
wish()

# Continuously listen for user commands.
while True:
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        try:
            print("Taking input...")
            listener.pause_threshold = 0.5 
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="en-in")
            if "Sony stop" in command:
                break
            if "Sony" in command:
                command = command.replace("Sony","")
                start_command(command)
            
        except:
            pass