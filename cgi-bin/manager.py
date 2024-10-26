#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pandas as pd
import random
import os
import cgi
import cgitb
import sys
import random, yaml

cgitb.enable(display=1, logdir="/path/to/logdir")  # Optional: logdir anpassen, um Logs zu speichern


form = cgi.FieldStorage()


print("Content-type: text/html\n")

try: 
    password = form["password"].value
except:
    decrypt_text = "Never gonnda give you up"



def add_password(pw):
     with open("password.yaml", "a+") as file:
        # Falls die Datei leer sein sollte, wird erstmal der Header geschrieben
        if os.stat("password.yaml").st_size == 0:
            file.write("passwords:\n")
        file.write(f'  - id: {random.randint(1,100)}\n')
        file.write(f'    password: {pw}\n')
        file.close()



   

# Exception für den Fall, dass jemand dachte ich ändere "number" to "text" um ein Fehler zu provozieren.
try:
    add_password(password)
except:
    add_password("Never gonna let you down")



print("<!DOCTYPE html>")
print('''<html lang="de">''')
print("<head>")
print('<meta charset="utf-8">')
print('''<meta name="viewport" content="width=device-width, initial-scale=1.0">''')
print("<link rel="+"icon ""type="+"image/png"+ " href="+"../sempro/thb.png"+">")
print("<title>Meine Seite</title>")
print("<link rel="+"stylesheet"+" href="+"../style.css"+">") 

# Bei diesem Abschnitt handelt es sich um einen kleinen Insider. Alle regulären Nutzer werden von dieser
# Verzweigung nichts mitbekommen, aber für jeden der wie oben jemand beschrieben versucht aus dem Programm auszubrechen
# halte ich hiermit ein kleines Easteregg parat.


print("</head>")    
print("<body>")



print(''' 
<div class="navigation">
   <ul>
    <li><a class="navbar" href="../sempro/index.html">Caeser</a></li>
    <li><a class="navbar" href="../sempro/pwGenerator.html">Passwort Generator</a></li>
    <li><a class="navbar" href="#contact">Contact</a></li>
    <li><a class="navbar" href="readme.txt">About</a></li>
  </ul>
</div> ''')


print("<p class"+"=encrypted" + "> Ursprünglicher Text: " + decrypt_text +"</p>") 

print("<br>")
print("</body>")
print("</html>")
