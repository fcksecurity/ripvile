### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD
### ZGOV ON DISCORD

import time
import threading
import random
import colorama
import os
import json
import httpx
import datetime
from colorama           import Fore

config = json.load(open("data/config.json", "r"))
proxies = open("data/proxies.txt", "r").read().splitlines()
banner = Fore.LIGHTBLUE_EX + '''
       _          _ __   
  ____(_)__ _  __(_) /__ 
 / __/ / _ \ |/ / / / -_)       <3
/_/ /_/ .__/___/_/_/\__/ 
     /_/                 
                                                                      
'''

class Logging():
    def send(text, token:str):
        timeez = datetime.datetime.now().strftime('%H:%M:%S')
        token = token.split('.')[0]
        print(f'{Fore.LIGHTBLACK_EX}{timeez} {Fore.LIGHTBLUE_EX}{text} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLUE_EX}[{Fore.WHITE}{token}***{Fore.LIGHTBLUE_EX}]')

    def send2(text):
        timeez = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'{Fore.LIGHTBLACK_EX}{timeez} {Fore.LIGHTBLUE_EX}{text} {Fore.LIGHTBLACK_EX}')

def send_request(channelid, token):
    try:
        session = httpx.Client(proxies = {"http://": random.choice(proxies)})
        session.headers = {"Authorization": str(token)}

        r = session.post(
            url = f'https://discord.com/api/v9/channels/{channelid}/messages',
            json = {
                "content": config["message"]
            }
        )
        if r.status_code == 429:
            data = r.json()
            retry = int(data["retry_after"])
            Logging.send(f'Ratelimited: {retry}s', token)
            time.sleep(retry)
        else:
            Logging.send('Successfully sent message', token)
            time.sleep(float(config["cool_per_send"]))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    os.system('cls')
    os.system('title RIPVile @zgov on discord')
    print(banner)
    Logging.send2('Starting threads...')
    cool = config["cool_per_thread"]
    while True:
        with open("data/tokens.txt", "r") as file:
            tokens = file.read().splitlines()
            for token in tokens:
                threading.Thread(target=send_request, args=(config["channelid"], token,)).start()
                time.sleep(float(cool))
