# run file
import receiver_class
import os
import sys
import netifaces as ni

# Please run as root
os.system("clear")
# Asking for Pi's IP to set up SSH com
print('Please enter the number of the interface your using to connect to the internet:')

interfaces = ni.interfaces()	 # Get all network interfaces of the computer

i = 1
for x in interfaces:		 # Print out all network interfaces of the computer
	print(str(i)+ " : " + x)
	i+=1

selection = sys.stdin.readline().rstrip('\n') 	# The user shall choose one 

interface = interfaces[int(selection)-1] # Choice of the user

user_ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']  # Getting user IP address

print("Your IP address is : "+ user_ip) 	# Printing out user IP address

## We might need here to enable port forwarding
print("You have to enable PORT 5706 for listening for outcoming data")
print("You might be asked to provide root permissions !")
#os.system("sudo iptables -A OUTPUT -p tcp --dport  5706 -j ACCEPT")

receive = receiver_class.receive(user_ip, 5706)  # Establishing connection, setting port

receive.get() 		# Getting data