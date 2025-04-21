import string
import random
import json
import os

def headers(method = 'get', token = None):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }
    if method == 'post':
        header['Content-Type'] = 'application/json'
    
    if token is not None:
        header['Authorization'] = f'Bearer {token}'

    return header

def random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def random_int(length=10):
    return ''.join(random.choice('0123456789') for _ in range(length))

def printt(res):
    print(json.dumps(res, indent=4))

def save_account(email, password):
    file_path = "accounts.json"
    akun = []

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                akun = json.load(f)
        except:
            akun = []

    akun.append({
        "email": email,
        "password": password
    })

    with open(file_path, "w") as f:
        json.dump(akun, f, indent=4)

    print(f"[✔] account saved")

def read_account(file_path='accounts.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data