import colorama
import requests
import time
import os

inp = f"[{colorama.Fore.MAGENTA}>{colorama.Style.RESET_ALL}] $ "
err = f"[{colorama.Fore.RED}-{colorama.Style.RESET_ALL}]"
out = f"[{colorama.Fore.GREEN}:{colorama.Style.RESET_ALL}]"
log = f"[{colorama.Fore.CYAN}={colorama.Style.RESET_ALL}]"

def sender():
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
                for i in range(int(amt)):
                    response = requests.post(webhook, json = {"content" : message}, params = {'wait' : True})
            except Exception as e:
                print(e + ", press [ENTER] to exit")
                input()
                exit()

            if response.status_code == 204 or response.status_code == 200:
                print(f" {out} - Message sent")
            elif response.status_code == 429:
                print(f" {log} - Rate limited ({response.json()['retry_after']}ms)")
                time.sleep(response.json()["retry_after"] / 1000)
            else:
                print(f" {err} - Error code: {response.status_code}, press [ENTER] to exit")
                input()
                exit()
            time.sleep(.5)
    print(f" {err} - Invalid input, press [ENTER] to exit")
    input()
    exit()

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
                print(e + ", press [ENTER] to exit")
                input()
                exit()

            if response.status_code == 204 or response.status_code == 200:
                print(f" {out} - Message sent")

            elif response.status_code == 429:
                print(f" {log} - Rate limited ({response.json()['retry_after']}ms)")
                time.sleep(response.json()["retry_after"] / 1000)

            else:
                print(f" {err} - Error code: {response.status_code}, press [ENTER] to exit")
                input()
                exit()
            time.sleep(.5)
    except:
        print(f" {log} Press [ENTER] to exit")

def deleter():
    os.system('cls; clear')
    os.system("title [Terrific's Webhook-Tools - Deleter]")
    print(f'{log} [WEBHOOK-TOOLS] - Webhook deleter\n')
    webhook = input(f" {inp} Webhook: ")
    if webhook != "":
        try:
            requests.delete(webhook.rstrip())
            print(f' {out} - Webhook has been deleted, press [ENTER] to exit')
            input()
            exit()
        except Exception as e:
            print(f" {err} - Webhook could not be deleted, press [ENTER] to exit")
            input()
            exit()
    else:
        print(f" {err} - Invalid Input, press [ENTER] to exit")
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
         ║ 1  =  Sender   ║
         ║ 2  =  Spammer  ║
         ║ 3  =  Deleter  ║
         ║ X  =  Exit     ║
        [x]==============[x]''')
    i = input(f" {inp} ")

screen()
if str(i) == str(1):
    sender()
elif str(i) == str(2):
    spammer()
elif str(i) == str(3):
    deleter()
elif str(i).lower() == "x":
    exit()
else:
    print(f" {err} - Invalid Input")
    input()
    exit()
