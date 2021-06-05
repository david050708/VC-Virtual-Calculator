import speech_recognition as sr
import pyttsx3


def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum = num1+num2
    print(sum)
    pyttsx3.speak(sum)

def minus():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    diff = num1-num2
    print(diff)
    pyttsx3.speak(diff)

def product():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    product = num1*num2
    print(product)
    pyttsx3.speak(product)

def quotient():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    q = num1/num2
    print(q)
    pyttsx3.speak(q)

def bye():
    pyttsx3.speak("bye sir, happy to help")
    
def VC():
    pyttsx3.speak("Yes, How may I help you")

def takeCommand():
  
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('Listening...')
			r.pause_threshold = 1.0
			audio = r.listen(source)
			try:
				print("Analysing...")
				Query = r.recognize_google(audio, language='en-in')
				print(Query)
				
			except Exception as e:
				print(e)
				print("Say that again sir")
				return "None"
			
			return Query

def run_VC():
    command = takeCommand()
    print(command)
    if 'plus' in command or 'add' in command:
        add()
    elif 'minus' in command or 'subtract' in command:
        minus()
    elif 'multiply' in command or 'into' in command:
        product()
    elif 'divide' in command:
        quotient()
    elif 'bye' in command or 'see you later' in command:
        bye()
        exit()
    elif'VC' in command or 'hey' in command or 'hey there' in command or 'can you help me' in command:
        VC()

while True:
    run_VC()
