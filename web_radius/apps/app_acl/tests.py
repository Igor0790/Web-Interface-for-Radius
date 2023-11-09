#from django.test import TestCase
import socket

client = socket.socket()



ip = '10.100.9.190'
port = 5555
client.connect((ip, port))
client.send(b'Hello World From Python!')


client.close()

