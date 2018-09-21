#!/usr/bin/env python
#Emitter Class
# It uses TCP/IP protocol
# Used to send the results of processing to the client

import socket

class emitter(object):
 	def __init__(self):
		pass

	def send(self, MESSAGE):
		TCP_IP = '192.168.1.106'
		TCP_PORT = 5706
		BUFFER_SIZE = 1024
		#MESSAGE = "Hello, World!"
 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, TCP_PORT))
		s.send(MESSAGE)
		data = s.recv(BUFFER_SIZE)
		s.close()
 
		print("received data:", data)
