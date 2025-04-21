import requests
import json
from modul import *
import time

def login(email,password):
    url = 'https://api.solixdepin.net/api/auth/login-password'
    payload = {"email":email,"password":password}
    try:
        response = requests.post(url,headers=headers('post'),json=payload).json()
        if response['result'] == 'success':
            token = response['data']['accessToken']
            return token
        else:
            print('failed login')
    except Exception as e:
        print(e)
    
def get_point(token):
    url = 'https://api.solixdepin.net/api/point/get-total-point'
    try:
        response = requests.get(url,headers=headers('get',token)).json()
        if response['result'] == 'success':
            point = response['data']['total']
            return point
    except Exception as e:
        print(e)

def task(token):
    url = 'https://api.solixdepin.net/api/task/get-user-task'
    try:
        response = requests.get(url,headers=headers('get',token)).json()
        for tasks in response['data']:
            id_task = tasks['_id']
            do_task(token, id_task)
            claim_task(token, id_task)
    except Exception as e:
        print(e)

def do_task(token, id_task):
    url = 'https://api.solixdepin.net/api/task/do-task'
    payload = {"taskId":id_task}
    try:
        response = requests.post(url,headers=headers('post',token),json=payload).json()
        print(response)
    except Exception as e:
        print(e)

def claim_task(token, id_task):
    url = 'https://api.solixdepin.net/api/task/claim-task'
    payload = {"taskId":id_task}
    try:
        response = requests.post(url,headers=headers('post',token),json=payload).json()
        print(response)
    except Exception as e:
        print(e)

def run():
    account_list = read_account()
    for akun in account_list:
        email = akun['email']
        password = akun['password']
        token = login(email,password)
        print(f'email: {email} | point {get_point(token)}')
        task(token)
        time.sleep(30)

