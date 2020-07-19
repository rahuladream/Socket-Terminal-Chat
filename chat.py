#Coded by Yashraj Singh Chouhan
import socket, threading
import colored
from colored import stylize
import random

nickname = input("Choose your nickname: ")

all_color = ['blue', 'magenta', 'cyan', 'light_gray', 'light_red', 'white', 'navy_blue', 'blue_1', 'turquoise_4', 'purple_3', 'wheat_4', 'dark_red_2']

for i, color in enumerate(all_color):
    print('{} : {}'.format(i, stylize(color, colored.fg(color))))

color = int(input("Pick avatar color number (e.g 1): "))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect(('127.0.0.1', 7976))                             #connecting client to server

def receive():
    while True:                                                 #making valid connection
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:                                                 #case on wrong ip/port details
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                #message layout
        message = '{}: {}'.format(stylize(nickname, colored.fg(all_color[color])), input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   #sending messages 
write_thread.start()