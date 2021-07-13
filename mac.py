import os
import subprocess
import colorama
from colorama import Fore



if os.geteuid() != 0:
    exit(Fore.RED+ "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
print("")
print(Fore.RED + '''
  ___                 __      __  __   _   ___ 
 / __|_ __  ___  ___ / _|_  _|  \/  | /_\ / __|
 \__ \ '_ \/ _ \/ _ \  _| || | |\/| |/ _ \ (__ 
 |___/ .__/\___/\___/_|  \_, |_|  |_/_/ \_\___|
     |_|                 |__/  
                              ''' + Fore.GREEN + '''Simple MAC address changer by R00tDev1l''')

print(Fore.WHITE + "")     
os.system('ifconfig')
print("")
print(Fore.RED + "These interfaces are currently availabe in your system please pick one of them.")
try:
    print("")    
    interface = input(Fore.GREEN + "Please type the interface=>")
    print("")
    new_mac = input(Fore.GREEN + "Please type a new MAC address here=>")
    print("")

    print(Fore.RED + "Changeing MAC address for " + interface + " to " + new_mac)
    print(Fore.WHITE + "")

    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether" + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

    print("")
    print(Fore.GREEN + "MAC address for "+ Fore.RED + interface + Fore.GREEN + " has been changed to "+ Fore.RED + new_mac + Fore.GREEN + " successfully.")
except KeyboardInterrupt:
    os.system('exit')