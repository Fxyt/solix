import requests
import json

PAGE_URL = "https://dashboard.solixdepin.net/sign-up"
SITEKEY = "0x4AAAAAABD9Dqblkacz6ou7"

with open('apikey.txt', 'r') as file:
    APIKEY = file.read()
    APIKEY = APIKEY.strip()

def solver():
    response = requests.get(f"https://api.sctg.xyz/in.php?key={APIKEY}&method=turnstile&pageurl={PAGE_URL}&sitekey={SITEKEY}").text
    id = response.replace('OK|','')
    while True:
        req = requests.get(f"https://api.sctg.xyz/res.php?key={APIKEY}&id={id}").text
        if req == 'CAPCHA_NOT_READY':
            print('CAPCHA_NOT_READY',end='\r')
        else:
            captcha = req.replace('OK|','')
            return captcha
