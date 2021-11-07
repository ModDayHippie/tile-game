#this script will update the RPI and install the needed moduals for this game
import os
import time

print('this script will automatily update and and install RPI updates and python moduals')
print('-----------------------------------------------')
time.sleep(2)
os.system("sudo")
print('updating repos ')
os.system("sudo apt-get update")
os.system("sudo apt-get update")
os.system("sudo apt-get install python3-pip")
os.system("pip install pytweening")
os.system("pip install pygame")
os.system("pip install PyTMX")
os.system("pip install setuptools")
os.system("sudo apt-get update")
os.system("sudo apt-get upgrade")
#os.system("")
#os.system("")