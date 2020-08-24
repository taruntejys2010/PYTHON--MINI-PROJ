import pyttsx3
a=pyttsx3.init()
a.setProperty('rate', 150) 
a.setProperty('volume', 1.0)
voice = a.getProperty('voice')
a.setProperty('voice', voice[1].id)
a.say("Hello this is the simple code about the words converts into speech by using python code")
a.runAndWait()
