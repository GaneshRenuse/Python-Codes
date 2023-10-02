import win32com.client as w
import time

speak = w.Dispatch("SAPI.SpVoice")

print("--Welcome to Robo speaker chat bot--\n")
text = "welcome to Robo speaker chat bot application, to communicate type your text"
speak.Speak(text)

text2 = input("Enter your text [available options (hello, how are you, tell me a quote)] :")

if text2 == "hello":
    text = "hii, how are you"
    speak.Speak(text)
elif text2 == "how are you":
    text = "i am fine, what about you"
    speak.Speak(text)
elif text2 == "tell me a quote":
    text = "sure, the quote is hardworking is a key to success"
    speak.Speak(text)
else:
    text = "i did not understand what you said"
    speak.Speak(text)

time.sleep(3)
text = "thanks for using robo speaker"
speak.Speak(text)
