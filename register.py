import requests
from captcha import solver
from modul import *

def regist(email,password,refferal_code,i):
    url = 'https://api.solixdepin.net/api/auth/register'
    payload = {"email":email,"password":password,"captchaToken":solver(),"referralCode":refferal_code}
    response = requests.post(url,headers=headers('post'),json=payload).json()
    try:
        if response['result'] == 'success':
            print(f'[{i}] email {email} successful register')
            save_account(email,password)
    except Exception as e:
        print(e)

def run():
    refferal_code = input('input your refferal code: ')
    name_mail = input('input name for email: ')
    password = input('input password: ')
    loop = int(input('how many account (number): '))
    i = 1
    while i <= loop:
        email = f'{name_mail}{random_int(5)}@gmail.com'
        regist(email,password,refferal_code,i)
        i+=1
