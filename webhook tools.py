import json
import colorama
import requests
import time
import os

from requests.api import request

inp = f"[{colorama.Fore.MAGENTA}>{colorama.Style.RESET_ALL}] $ "
err = f"[{colorama.Fore.RED}-{colorama.Style.RESET_ALL}]"
inf = f"[{colorama.Fore.YELLOW}i{colorama.Style.RESET_ALL}]"
out = f"[{colorama.Fore.GREEN}:{colorama.Style.RESET_ALL}]"
log = f"[{colorama.Fore.CYAN}={colorama.Style.RESET_ALL}]"

def sender():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - Spammer]")
    print(f'{log} [WEBHOOK-TOOLS] - Webhook spammer\n')
    webhook = input(f" {inp} Webhook Url: ")
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
    print(f" {err} - Invalid input, press [ENTER] to return")
    input()
    screen()

def spammer():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - Spammer]")
    print(f'{log} [WEBHOOK-TOOLS] - Webhook spammer\n')
    webhook = input(f" {inp} Webhook Url: ")
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

def deleter():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - Deleter]")
    print(f'{log} [WEBHOOK-TOOLS] - Webhook deleter\n')
    webhook = input(f" {inp} Webhook: ")
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

def checker():
    os.system("cls; clear")
    os.system("title [Terrific's Webhook-Tools - Checker]")
    print(f"{log} [WEBHOOK-TOOLS] - Webhook checker\n")
    webhook = input(f" {inp} Webhook: ")
    if webhook != "":
        try:
            r = requests.get(webhook)
            if r.ok == False:
                print(f"{log} [WEBHOOK-TOOLS] - Webhook Invalid")
            elif r.ok == True:
                print(f"{log} [WEBHOOK-TOOLS] - Webhook Works")
        except Exception as e:
            print(f"{err} [WEBHOOK-TOOLS] - Webhook could not be checked\n{err} [WEBHOOK-TOOLS] - Error Message: {e}")


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
def screen():
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
        print(f"\n\n {inf} Input Message")
        while True:
            message = input(f" {inp} ")
            sendmessage(webhook, message)

    except KeyboardInterrupt:
        screen()
    except:
        screen()

def changeinfo():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - ChangeInfo]")
    print(f'{log} [WEBHOOK-TOOLS] - Change Info\n\n')

    webhook = input(f" {inp} Webhook URL: ")

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

def singleutils():
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
screen()
