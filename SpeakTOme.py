import speech_recognition as sr
import wolframalpha,pyttsx3,wikipedia,pyaudio

def listen_mic(r):
  with sr.Microphone() as source:
    print("-"*170)
    print("MICROPHONE IS LISTINING....")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    return text

def check_len(text):
  if len(text) <= 200:
    print(text)
    speak(text)
  else:
    print(text)
    speak_fast(text)

      

def wolfframe_check(text):
  app_id = "XHRH93-9XPWXAJJVH"
  client = wolframalpha.Client(app_id)
  res = client.query(text)
  answer = next(res.results).text
  check_len(answer)

def wikipedia_check(text):
  answer = wikipedia.summary(text)
  a = "According to Wikipedia"
  print(a+"\n")
  speak(a)
  check_len(answer)

def speak_fast(text):
  read = pyttsx3.init()
  read.setProperty('rate', 230)
  read.setProperty('volume', 1.3)
  read.say(text)
  read.runAndWait()

def speak(text):
  read = pyttsx3.init()
  read.setProperty('rate', 230)
  read.setProperty('volume', 1.3)
  read.say(text)
  read.runAndWait()

while True:
  r = sr.Recognizer()
  try:
    text = listen_mic(r)
    if text == "stop":
      speak("bye, it was nice talking to u!")
      break
    try:
      wolfframe_check(text)
      
    except:
      wikipedia_check(text)
      
  except:
    answer = "Can you say it again...."
    print(answer)
    speak(answer)