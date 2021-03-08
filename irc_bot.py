#!/usr/bin/python3
from irc_class import *
import os
import random
import subprocess
import re


def send_message (recipient, subject, body):
   cmd="echo {} | mail -s '{}' {}".format(body,subject, recipient)
   process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}\$"

def check(email):
   if(re.search(regex,email)):
      return True
   else:
     return False



## IRC Config
server = "YourServer" # Provide a valid server IP/Hostname
port = 6667
channel = "YourChannell"
botnick = "BotName"
botnickpass = "YourBotNickPass"
botpass = "YourBotPass"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)
recipient = "YourEmail"


while True:
    text = irc.get_response()
    print(text)

    if "PRIVMSG" in text:
       user = text.split('!',1)[0][1:]
       channel = text.split('PRIVMSG',1)[1].split(':',1)[0] or ''
       userMessage = text.split('PRIVMSG',1)[1].split(':',1)[1] or ''

       if "PRIVMSG" in text and "#" in text and "hello" in text:
           irc.send(channel, user, "Hello! I'm a xxxxxxxxx BoT, please DM me with command for a list of command.")
    
       if "PRIVMSG" in text and "#" not in text and "command" in text:
           irc.send(channel, user, "Please if you have any problems with your email, use: <email:your_email> <description:problem_description>. You will be contacted as soon as possible and mail will be sent to the administrator. Thank you.")
           irc.send(channel, user, "Use: about, for information.")

        if "PRIVMSG" in text and "#" not in text and "about" in text:
           irc.send("Put here your message")
         

       if "PRIVMSG" in text and "email" in text and "description" in text:
           email = text.split("email",1)[1].split(":",1)[1].split()[0]
           if check(email) == True:
              description = text.split("description",1)[1].split(":",1)[1]
              body = description.rstrip()
              subject = "email from {}".format(email)
              send_message (recipient, subject, body)
              irc.send(channel, user, "Email sent to administrator. Thank you.")
           else:
              irc.send(channel, user, "Please insert a valid mail address !")

