#!/usr/bin/env python
import socket

class receive:
	__TCP_IP = ''
	__TCP_PORT = 0
	__BUFFER_SIZE = 1024

	#Constructor to set IP and PORT
	def __init__(self, TCP_IP, TCP_PORT):
		self.__TCP_IP = TCP_IP
		self.__TCP_PORT = TCP_PORT

	def get(self):
		print("Connecting ...")

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Opening socket
		s.bind((self.__TCP_IP, self.__TCP_PORT))	# Setting IP and port settings of the socket
		s.listen(1)		# Start listening

		conn, addr = s.accept()
		print('Connection address:', addr)
		while 1:
			data = conn.recv(self.__BUFFER_SIZE)
			if not data: break
			print("received data:", data)
			conn.send(data)  # echo
		conn.close()