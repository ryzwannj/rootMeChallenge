import socket
import math
from time import sleep


host = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
botname = "candy"
nick = "xwHelOlowx"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Connecting to the server:", host)
irc.connect((host, port))
sleep(1)
irc.send(("USER " + nick + " " + nick + " " + host + " " + nick + '\r\n').encode('utf-8'))
sleep(1)
irc.send(("NICK " + nick + '\r\n').encode('utf-8'))
sleep(1)
irc.send(("JOIN " + channel + '\r\n').encode('utf-8'))
sleep(2)
irc.send(("PRIVMSG "+ botname +" :"+ "!ep1" + "\r\n").encode('utf-8'))

def rootFunc(num1, num2):
    square = math.sqrt(int(num1))
    times = square * int(num2)
    final_result = round(times, 2)
    return final_result

running = True
while running:
    response = irc.recv(1024).decode("utf-8", "ignore")
    print(response)
    if response.startswith(":Candy!Candy@root-me.org PRIVMSG"):
        f1 = response.replace(":Candy!Candy@root-me.org PRIVMSG " + nick + " :", "")
        print(f1)
        numbers = f1.split('/')

        # number one formating

        print(numbers[0], len(numbers[0]))
        num1 = numbers[0].replace(" ", "")
        print(num1 + " " + str(len(num1)))

        # number two formating

        print(numbers[1], len(numbers[1]))
        num2 = numbers[1].replace(" ", "")
        num2 = num2.replace("\r\n", "")
        print(num2 + " " + str(len(num2)))

        result = str(rootFunc(num1, num2))

        irc.send(("PRIVMSG "+ botname +" :"+ "!ep1 -rep "+ result + "\r\n").encode('utf-8'))
        sleep(1)





    