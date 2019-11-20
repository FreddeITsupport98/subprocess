
import subprocess
import os

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


wsl = subprocess.capita(['ls'])
print(wsl)