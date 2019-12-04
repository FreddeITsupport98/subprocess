
import subprocess
import os
import sys

#https://github.com/Z3roTwo/ADPythonAutomatisering?files=1


# kollar upp git version med returnvalue = 0
#cmd = 'git --version'
#returned_value = os.system(cmd) #tillkalar git commando
#print('returned value:', returned_value)

#kör 'echo' kommandon i shell i output
#shell = subprocess.run(['echo', 'hello world'], capture_output=True, shell=True)
#print(shell.stdout) 

# hämtar system info med returnvalue = 0
#
#cmd = "systeminfo"
# 
#returned_value = subprocess.call(cmd, shell=True)
#print("returned_value:", returned_value) 

#ska väcka wsl kommando i windows
#wsl = subprocess.call(['ls'])
#print(wsl


#Skapar användare med administartör priviligeier
#
#print("hej vill du skapa ny användare? ja eller nej")
#x = input()
#if x == 'ja':
#    ws1 = subprocess.call(['net', 'user', 'Testuser', 'li05zzIe2', '/ADD'], shell=True)
#    print(ws1)
#elif x == 'nej':
#    exit
    
import random, string

chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "1234567890"
chars2 = "!#%&/()="
password = ""
for c in range(2):
    password += random.choice(chars)
    password += random.choice(chars.upper())
    password += random.choice(chars1)
    password += random.choice(chars2)
password = ''.join(random.sample(password, len(password)))
print(password)
print(len(password))