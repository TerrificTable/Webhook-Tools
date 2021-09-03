from abc import abstractmethod
from colored import fg
import colorama
import requests
import time
import os

inp = f"[{colorama.Fore.MAGENTA}>{colorama.Style.RESET_ALL}] $ "
err = f"[{colorama.Fore.RED}-{colorama.Style.RESET_ALL}]"
out = f"[{colorama.Fore.GREEN}:{colorama.Style.RESET_ALL}]"
log = f"[{colorama.Fore.CYAN}={colorama.Style.RESET_ALL}]"

def spammer():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - Spammer]")
    print(f'{log} [WEBHOOK-TOOLS] - Webhook spammer\n')
    webhook = input(f" {inp} Webhook Url: ")
    message = input(f" {inp} Message: ")
    amt = input(f" {inp} Amout of Messages send: ")
    print("")

    if webhook != "" or message != "" or str(amt) != "":
        for i in range(int(amt)):
            try:
                response = requests.post(webhook, json = {"content" : message}, params = {'wait' : True})
            except Exception as e:
                print(e + ", press [ENTER] to exit")
                while True:
                    input()
                    exit()

            if response.status_code == 204 or response.status_code == 200:
                print(f" {out} - Message sent, press [ENTER] to exit")
                while True:
                    input()
                    exit()
            elif response.status_code == 429:
                print(f" {log} - Rate limited ({response.json()['retry_after']}ms)")
                time.sleep(response.json()["retry_after"] / 1000)
            else:
                print(f" {err} - Error code: {response.status_code}, press [ENTER] to exit")
                while True:
                    input()
                    exit()
            time.sleep(.5)
    print(f" {err} - Invalid input, press [ENTER] to exit")
    while True:
        input()
        exit()

def deleter():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - Deleter]")
    print(f'{log} [WEBHOOK-TOOLS] - Webhook deleter\n')
    webhook = input(f" {inp} Webhook: ")
    if webhook != "":
        try:
            requests.delete(webhook.rstrip())
            print(f' {out} - Webhook has been deleted, press [ENTER] to exit')
            while True:
                input()
                exit()
        except Exception as e:
            print(f" {err} - Webhook could not be deleted, press [ENTER] to exit")
            while True:
                input()
                exit()
    else:
        print(f" {err} - Invalid Input, press [ENTER] to exit")
        while True:
            input()
            exit()


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
        [x]==============[x]
         ║ 1  =  Spammer  ║
         ║ 2  =  Deleter  ║
         ║ X  =  Exit     ║
        [x]==============[x]''')
    i = input(f" {inp} ")

screen()
if str(i) == str(1):
    spammer()
elif str(i) == str(2):
    deleter()
elif str(i).lower() == "x":
    exit()
else:
    print(f" {err} - Invalid Input")
    input()
    exit()
