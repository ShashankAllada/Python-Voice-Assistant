#"Assistant" is designed to perform tasks on a one-time basis. 
#When executed, it carries out a specific task and then automatically terminates itself. 
#It is ideal for single, isolated operations where you need a quick and focused response.
    
# Import necessary libraries for speech recognition, text-to-speech, and other functionalities.
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Get available voices for the text-to-speech engine and set the voice to the first one (index 0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak a given text using the text-to-speech engine
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of the day
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

    print("I am Soni, how may I help you?")
    speak("I am Soni, how may I help you?")

# Function to listen to user's voice commands
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise and set a pause threshold
        listener.adjust_for_ambient_noise(source)
        listener.pause_threshold = 0.5

        while True:
            try:
                print("Taking input...")
                voice = listener.listen(source)
                # Recognize the user's voice command using Google's speech recognition
                command = listener.recognize_google(voice, language="en-in")
                return command
            except:
                print("I am sorry, could you repeat the command? ")
                speak("I am sorry, could you repeat the command? ")

            
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
  

# Call the 'wish' function to greet the user based on the time of the day
wish()

# Call the 'start_command' function to begin listening for user commands
start_command()