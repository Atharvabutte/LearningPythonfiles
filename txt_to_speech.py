import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = '''Hey! Atharva this is your laptop & you create me. 
This text is read after 3 seconds.hey Tell me what do you do.& your date of birth is 05/08/2005'''
speak.Speak(text)

# 3 second sleep
# time.sleep(3) 

# text = "This text is read after 3 seconds"
# speak.Speak(text)

# text = "hey Tell me what do you do."
# speak.Speak(text)