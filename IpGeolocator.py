#imports the rquired moduls
import requests
import time
import requests
import socket
import sys
import subprocess


print("""                  
 _____                 _____
|  ___|   _ _ __  _ __|___  |_      __
| |_ | | | | '_ \| '_ \  / /\ \ /\ / /
|  _|| |_| | | | | | | |/ /  \ V  V /
|_|   \__, |_| |_|_| |_/_/    \_/\_/
      |___/""")
print("")
time.sleep(1)
print("*************************************************")
print("Mail: Fynn_Wilhelm@ProtonMail.com\nGitHub: Fynn7w\nFor educational purposes only!")
print("*************************************************")
print("")

print("useable commands :")
print("-show_local_ip (shows local ip)")
print("-geolocate_ip (geolocate the defined ip address)")
print("-geolocate_ip -hard_scan (harder scan of option2)")
print("-change_mac_adr (only works under linux)")
print("")


time.sleep(2)

command = input("")
if command == "-geolocate_ip":
    a = input("please enter a ip addres :")#user input
    #get the information about the ip(4) address
    response = requests.get("https://geolocation-db.com/json/",a).json()
    #Lists the informations
    Ip_address = response['IPv4']
    country = response['country_name']
    city = response['city']
    postal = response['postal']

    #prints the informations
    print("Information about following ip :", Ip_address)
    time.sleep(1.)
    print("Country :", country)
    print("City :", city)
    print("postal:", postal)
    print("")
    time.sleep(2)
    sys.exit()

if command == "-show_local_ip":
    hostname = socket.gethostname()#gets hostname
    local_ip = socket.gethostbyname(hostname)#gets ip of this hostname
    print("your local ip is :",local_ip)
    sys.exit()

if command == "-geolocate_ip -hard_scan":
    a = input("please enter a ip addres :")#user input
    #get the information about the ip(4) address
    response = requests.get("https://geolocation-db.com/json/",a).json()
    time.sleep(1)
    print("")
    print(response)
    sys.exit()

if command == "-change_mac_adr":
    print("changing mac address...")
    subprocess.call(["sudo","ipconfig","ens33","down"])
    subprocess.call(["sudo","ipconfig","ens33","hw","ether","00:11:22:33:44:55"])
    subprocess.call(["sudo","ipconfig","ens33","up"])


#shows alle useable commands
if command == "show_options":
    print("useable commands :")
    print("-show_local_ip (shows local ip)")
    print("-geolocate_ip (geolocate the defined ip address)")
    print("-geolocate_ip -hard_scan (harder scan of option2)")
    print("-change_mac-adr (changes your current mac address)")
    sys.exit()


#if command isnt defined
else:
    print("undefined command!")
    print("to see a list of all the commands type : show_options")
    sys.exit()
