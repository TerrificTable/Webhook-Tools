from pypresence import Presence
import colorama
import requests
import time
import os

#####################
## -Console Utils- ##
#####################

inp = f"[{colorama.Fore.MAGENTA}>{colorama.Style.RESET_ALL}] $ "
err = f"[{colorama.Fore.RED}-{colorama.Style.RESET_ALL}]"
inf = f"[{colorama.Fore.YELLOW}i{colorama.Style.RESET_ALL}]"
out = f"[{colorama.Fore.GREEN}:{colorama.Style.RESET_ALL}]"
log = f"[{colorama.Fore.CYAN}={colorama.Style.RESET_ALL}]"


###################
## -Discord RPC- ##
###################

buttonList = [
    {
        "label":"GitHub",
        "url":"https://github.com/TerrificTable"
    },
    {
        "label":"This Programm",
        "url":"https://github.com/TerrificTable/Webhook-Tools"
    }
]


rpc = Presence("894180358755581953")
rpc.connect()
rpc.update(
    details="Terrific's Webhook Tools",
    large_text="Webhook Tools",
    large_image="rpc",
    small_text="by Terrific",
    small_image="small",
    buttons=buttonList,
    start=time.time()
)


#####################
## -Check Webhook- ##
#####################

def checkwebhook(w):
    try:
        check = requests.get(w, params = { 'wait' : True })
        if check.ok or check:
            return True
        else:
            return False
    except:
        return False


#####################
## -Sender Module- ##
#####################

def sender():
    try:
        os.system('cls; clear')
        os.system("title [Terrific's Webhook-Tools - Spammer]")
        print(f'{log} [WEBHOOK-TOOLS] - Webhook spammer\n')
        webhook = input(f" {inp} Webhook Url: ")
        if checkwebhook(webhook):
            cu = input(f"\n {inp} Do you want to put a Custom Webhook name inside (it changes the name of the Webhook if it sends a message) [y/n]: ")
            if str(cu) == "y":
                username = input(f" {inp} Username: ")
            av  = input(f"\n {inp} Do you want the Webhook to have a Custom avatar [y/n]: ")
            if str(av) == "y":
                avatarurl = input(f" {inp} Avatar-Url (A Image URL): ")
            message = input(f"\n {inp} Message: ")
            amt = input(f" {inp} Amout of Messages send: ")
            print("")

            if webhook != "" or message != "" or str(amt) != "":
                for i in range(int(amt)):
                    try:
                        if str(cu) == "y" and str(av) == "y":
                            response = requests.post(webhook, json = { "content" : message, "username": username, "avatar_url": avatarurl }, params = { 'wait' : True })
                        elif str(cu) == "y" and str(av) == "n":
                            response = requests.post(webhook, json = { "content" : message, "username": username }, params = { 'wait' : True })
                        elif str(cu) == "n" and str(av) == "y":
                            response = requests.post(webhook, json = { "content" : message, "avatar_url": avatarurl }, params = { 'wait' : True })
                        elif str(cu) == "n" and str(av) == "n":
                            response = requests.post(webhook, json = { "content" : message }, params = { 'wait' : True })
                    except Exception as e:
                        print(e + ", press [ENTER] to return")
                        input()
                        screen()

                    if response.status_code == 204 or response.status_code == 200:
                        print(f" {out} - Message sent")
                    elif response.status_code == 429:
                        print(f" {log} - Rate limited ({response.json()['retry_after']}ms)")
                        time.sleep(response.json()["retry_after"] / 1000)
                    else:
                        print(f" {err} - Error code: {response.status_code}, press [ENTER] to return")
                        input()
                        screen()
                    time.sleep(.5)
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input(); sender()
        print(f" {err} - Invalid input, press [ENTER] to return")
        input()
        screen()
    except KeyboardInterrupt:
        screen()
    except:
        screen()


######################
## -Spammer Module- ##
######################

def spammer():
    try:
        os.system('cls; clear')
        os.system("title [Terrific's Webhook-Tools - Spammer]")
        print(f'{log} [WEBHOOK-TOOLS] - Webhook spammer\n')
        webhook = input(f" {inp} Webhook Url: ")
        if checkwebhook(webhook):
            message = input(f" {inp} Message: ")
            print("")
            try:
                while True:
                    try:
                        response = requests.post(webhook, json = {"content" : message}, params = {'wait' : True})
                    except Exception as e:
                        print(e + ", press [ENTER] to return")
                        input()
                        screen()

                    if response.status_code == 204 or response.status_code == 200:
                        print(f" {out} - Message sent")

                    elif response.status_code == 429:
                        print(f" {log} - Rate limited ({response.json()['retry_after']}ms)")
                        time.sleep(response.json()["retry_after"] / 1000)

                    else:
                        print(f" {err} - Error code: {response.status_code}, press [ENTER] to return")
                        input()
                        screen()
                    time.sleep(.5)
            except:
                print(f" {log} Press [ENTER] to return")
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input(); spammer()
    except KeyboardInterrupt:
        screen()
    except:
        screen()


######################
## -Deleter Module- ##
######################

def deleter():
    try:
        os.system('cls; clear')
        os.system("title [Terrific's Webhook-Tools - Deleter]")
        print(f'{log} [WEBHOOK-TOOLS] - Webhook deleter\n')
        webhook = input(f" {inp} Webhook: ")
        if checkwebhook(webhook):
            if webhook != "":
                try:
                    requests.delete(webhook.rstrip())
                    print(f' {out} - Webhook has been deleted, press [ENTER] to return')
                    input()
                    screen()
                except Exception as e:
                    print(f" {err} - Webhook could not be deleted, press [ENTER] to return")
                    input()
                    screen()
            else:
                print(f" {err} - Invalid Input, press [ENTER] to return")
                input()
                screen()
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input(); deleter()
    except KeyboardInterrupt:
        screen()
    except:
        screen()

        
######################
## -Checker Module- ##
######################

def checker():
    try:
        os.system("cls; clear")
        os.system("title [Terrific's Webhook-Tools - Checker]")
        print(f"{log} [WEBHOOK-TOOLS] - Webhook checker\n")
        webhook = input(f" {inp} Webhook: ")
        try:
            r = requests.get(webhook)
            if r.ok == False:
                print(f"{log} [WEBHOOK-TOOLS] - Webhook Invalid")
                input(); screen()
            elif r.ok == True:
                print(f"{log} [WEBHOOK-TOOLS] - Webhook Works, press [ENTER] to return")
                input(); screen()
        except Exception as e:
            print(f"{err} [WEBHOOK-TOOLS] - Webhook could not be checked\n{err} [WEBHOOK-TOOLS] - Error Message: {e}")
            input(); screen()
    except KeyboardInterrupt as e:
        screen()
    except Exception as e:
        screen()


##############
## -Banned- ##
##############

banner = f'''{colorama.Fore.RED}

    █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
    ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
    ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
    ░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
    ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
    ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
    ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
        ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░                   ░ ░      ░ ░      ░  ░      ░  
                        ░                                                                                 
                        ░                                                                         {colorama.Style.RESET_ALL}'''

###################
## -Screen Loop- ##
###################

def screen():
    try:
        global i

        os.system('cls; clear')
        os.system(f'mode 110, 25')
        os.system("title [Terrific's Webhook-Tools]")
        print(banner)
        print(f'''
            [x]==================[x]===================[x]
            ║ 1  =  Sender       ║  4  =  Checker      ║
            ║ 2  =  Spammer      ║  5  =  SingleUtils  ║
            ║ 3  =  Deleter      ║  X  =  Exit         ║
            [x]==================[x]===================[x]''')
        i = input(f" {inp} ")
        if str(i) == str(1):
            sender()
            input()
            screen()
        elif str(i) == str(2):
            spammer()
            input()
            screen()
        elif str(i) == str(3):
            deleter()
            input()
            screen()
        elif str(i) == str(4):
            checker()
            input()
            screen()
        elif str(i) == str(5):
            singleutils()
            input()
            screen()
        elif str(i).lower() == "x":
            screen()
        else:
            print(f" {err} - Invalid Input")
            input()
            screen()
    except KeyboardInterrupt:
        screen()
    except:
        screen()



######################
## -Message Sender- ##
######################

def sendmessage(w, m):
    r = requests.post(w, json = {"content" : m}, params = {'wait' : True})
    if r.ok:
        print(f" {out} Message sent")
    else:
        print(f" {err} Message failed to sent")

def chatsession():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - ChatSession]")
    print(f'{log} [WEBHOOK-TOOLS] - Chat Session\n\n\n')

    try:
        print(f" {inf} Press Ctrl + C to exit Chat session\n")
        webhook = input(f" {inp} Webhook: ")
        if checkwebhook(webhook):
            print(f"\n\n {inf} Input Message")
            while True:
                message = input(f" {inp} ")
                sendmessage(webhook, message)
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input(); chatsession()
    except KeyboardInterrupt:
        screen()
    except:
        screen()


#########################
## -ChangeInfo Module- ##
#########################

def changeinfo():
    try:
        os.system('cls; clear')
        os.system("title [Terrific's Webhook-Tools - ChangeInfo]")
        print(f'{log} [WEBHOOK-TOOLS] - Change Info\n\n')

        webhook = input(f" {inp} Webhook URL: ")

        if checkwebhook(webhook):
            print(f"""\n
            [x]=====================[x]
            ║ 1  =  Change Name     ║
            ║ 2  =  Change Avatar   ║
            ║ 3  =  Return to Menu  ║
            ║ X  =  Exit            ║
            [x]=====================[x]
            """)
            i = input(f" {inp} ")
            if str(i) == "1":
                name = input(f" {inp} Name: ")
                r = requests.patch(webhook, json={ "name":name })
                if r.ok:
                    print(f" {out} Succesfully Changed Name")
                else:
                    print(f" {err} Failed to Change Name")
            elif str(i) == "2":
                avatar = input(f" {inp} Image URL: ")
                r = requests.patch(webhook, json={"avatar_url":avatar})
                if r.ok:
                    print(f" {out} Succesfully Changed Name")
                else:
                    print(f" {err} Failed to Change Name")
            elif str(i) == "3":
                screen()
            elif str(i).lower() == "x":
                exit()
            else:
                print(f" {err} Invalid Input, pres [ENTER] to return")
                input()
                changeinfo()
        else:
            print(f" {err} Invalid Webhook, press [ENTER] to return")
            input(); changeinfo()
    except KeyboardInterrupt:
        screen()
    except:
        screen()


########################
## -SingleUtils Loop- ##
########################

def singleutils():
    try:
        os.system("cls")
        os.system("title [Terrific's Webhook-Tools - SingleUtils]")
        print(banner + "\n")
        print(f'''
        [x]=====================[x]======================[x]
        ║ 1  =  Chat Session    ║  3  =  Return to Menu  ║
        ║ 2  =  Change Info     ║  X  =  Exit            ║
        [x]=====================[x]======================[x]''')
        i = input(f" {inp} ")
        if str(i) == str(1):
            chatsession()
        elif str(i) == str(2):
            changeinfo()
        elif str(i) == str(3):
            screen()
        elif str(i).lower() == "x":
            exit()
        else:
            print(f" {err} Invalid Input, pres [ENTER] to return")
            input()
            singleutils()
    except KeyboardInterrupt:
        screen()
    except:
        screen()
screen()
