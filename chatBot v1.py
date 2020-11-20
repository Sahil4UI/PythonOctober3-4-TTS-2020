#CHAT BOT
from datetime import datetime
import webbrowser
chat = True
helloIntent = ["hi","hello","hie","wassup","heya"]
byeIntent = ["bye","good bye","TTYL","GTG","catch you later"]
dateIntent = ["date","show me date","date please"]
timeIntent = ["time","show me time","time please"]
while chat==True:
    msg = input("Enter Message : ").lower()

    if msg in helloIntent:
        print("HEllo....")

    elif msg in byeIntent:
        print("Bye.....")
        chat = False
        
    elif msg in dateIntent:
        currDate = datetime.now()
        print(currDate.strftime("%d-%m-%y,%a"))

    elif msg in timeIntent:
        currtime = datetime.now()
        print(currtime.strftime("%l:%M:%S"))
        
    elif msg.startswith("open"):
        msg = msg.split()[-1]
        webbrowser.open(f"https://www.{msg}.com/")
        
    else:
        print("sorry i don't understand...")
