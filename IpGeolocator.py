#import moduls
import requests
import time
import datetime
import socket
import sys

print("*************")
print("Ip Geolocater")
print("*************")
print("")
time.sleep(1)
print("useable commands :")
print("-show_local_ip (shows local ip)")
print("-geolocate_ip (geolocate the defined ip address)")
print("-geolocate_ip -hard_scan (aggressiv scan of the defined ip addres)")
print("-show_options to see all useable commands")
print("")

#waiting for commands...
command= input()

#command to geocolate the ip addres
if command == "-geolocate_ip":
    ip_input = input("Ip addres :")
    response = requests.post("http://ip-api.com/batch", json=[
      {"query": ip_input}
    ]).json()
    time.sleep(1)

    #only print the county Code,Status,City and Country of the ip
    for ip_info in response:
        print("Status:",ip_info['status'])
        print("Country Code:",ip_info['countryCode'])
        print("Country:",ip_info['country'])
        print("City:",ip_info['city'])
        sys.exit() 

#shows local ip
if command == "-show_local_ip":
	hostname = socket.gethostname()
	local_ip = socket.gethostbyname(hostname)
	print("your local ip is :",local_ip)
	sys.exit()

#shows all the usable commands
if command == "-show_options":
    print("-geolocate_ip (to locate the defined ip addres)")
    print("-show_local_ip (shows local ip)")
    print("-show_options to see all useable commands")

#shows all information about the Ip
if command == "-geolocate_ip -hard_scan":
    ip_input = input("Ip addres :")
    response = requests.post("http://ip-api.com/batch", json=[
      {"query": ip_input}
    ]).json()
    time.sleep(1)
    for ip_info in response:#prints the results(\n)
        for Xitems,Yitems in ip_info.items():
            print(Xitems,Yitems)

#if command wasnt found       
else:
    print("command not found\nType: -show_options to see the avaible commands")
