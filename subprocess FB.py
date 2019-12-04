
import subprocess
import os
import sys

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

print("hej vill du skapa ny användare?")

input('ja', 'nej')

if a == 'ja':
    ws1 = subprocess.call(['net', 'user', 'Testuser', 'li05zzIe2', '/ADD'], shell=True)
    print(ws1)
    elif:
        exit