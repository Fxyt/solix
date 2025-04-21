import asyncio
import aiohttp
from modul import *
from loguru import logger

async def login(session, email, password):
    url = 'https://api.solixdepin.net/api/auth/login-password'
    payload = {"email": email, "password": password}
    async with session.post(url, headers=headers('post'), json=payload) as response:
        if response.status == 201:
            data = await response.json()
            if data['result'] == 'success':
                token = data['data']['accessToken']
                logger.info(f"Login successful for email: {email}")
                return token
            else:
                logger.error(f"Login failed for email: {email}, Reason: {data['msg']}")
                return None
        else:
            logger.error(f"Login request failed for email: {email}, Status code: {response.status}")
            return None

async def get_point(session, token):
    url = 'https://api.solixdepin.net/api/point/get-total-point'
    try:
        async with session.get(url, headers=headers('get', token)) as response:
            if response.status == 200:
                data = await response.json()
                if data['result'] == 'success':
                    point = data['data']['total']
                    return point
                else:
                    logger.error(f"Failed to get points, Reason: {data['msg']}")
                    return None
            else:
                logger.error(f"Get points request failed, Status code: {response.status}")
                return None
    except Exception as e:
        logger.error(f"Error while getting points: {e}")
        return None

async def runer(session, email, password):
    token = await login(session, email, password)
    while True:
        if not token:
            logger.warning(f"Token expired or invalid for email: {email}. Re-logging in...")
            token = await login(session, email, password)  # Login ulang kalau token invalid
            if not token:
                logger.error(f"Failed to re-login for email: {email}. Retrying in 30 seconds...")
                await asyncio.sleep(30)  # Tunggu sebelum coba login ulang
                continue

        point = await get_point(session, token)
        if point is not None:
            logger.info(f'email: {email}')
            logger.info(f'point: {point}')
            logger.info(f'+==================')
        else:
            logger.warning(f"Failed to fetch points for email: {email}. Token might be invalid.")
            token = None

        await asyncio.sleep(30)

async def process():
    async with aiohttp.ClientSession() as session:
        account_list = read_account('accounts.json')
        batch_size = 100
        for i in range(0, len(account_list), batch_size):
            batch = account_list[i:i + batch_size]  # Ambil batch 5 akun
            tasks = [runer(session, akun['email'], akun['password']) for akun in batch]
            await asyncio.gather(*tasks)  # Jalankan semua akun dalam batch secara paralel

def run():
    asyncio.run(process())