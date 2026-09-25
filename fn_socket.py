import yadisk
import io
import json
import io
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import hashlib
import requests
from datetime import datetime



TOKEN = "y0__wgBEI7P1rsHGK2tPyCepcn2GDC9-KLlB2T1Lktn2skHCpc2GgPqFTFZtbvB"
client = yadisk.Client(token=TOKEN)

def check_vpn_ipapi():
    try:
        response = requests.get('http://ip-api.com/json/', timeout=10)
        data = response.json()
        
        if data.get('status') == 'success':
            ip = data.get('query')
            country = data.get('country')
            org = data.get('isp')
            city = data.get('city')
            
            # Проверка на прокси/VPN (если есть данные)
            is_proxy = data.get('proxy', False)
            is_hosting = data.get('hosting', False)
            
            return ip, country, org, is_proxy, is_hosting
        else:
            return None, None, None, False, False
        
    except Exception as e:
        print(f"Ошибка ip-api: {e}")
        return None, None, None, False, False

SALT_SIZE = 16
NONCE_SIZE = 12

PASSWORD_ENC = "DG2rUstjFxkhC2XlZT1c9DHjp82T0QDe7hvClJ1hKNweC1+9gz5FQl7GRmARr4Yf9DsRI6ANgy8aoyRMXBlP4aWa8wI4FXtxDsZiDgU+BBG24d+p3TtFeeXDDRhKTn+r82yOlaIBG6aTFmoGePvuk5B0FVYqmqC4eXBMI+sph5BP9CmcDMFUsUwWOkAc017R2ovOGVQPuZnihPF3w8xK7UC0Uo0ByO+mWQYp5BgkSrMpWhmQwcT7bLKgWIBrIQ7dvNmpqH5a+ZU5mvtUty3ePVJI2Zsv9tve6n0h3yguxlfT6+hlb/Uk+DXIUp/7AD6ARUA1POUMPwWY6fIbZp9RZvfCzlwFvn9UiBRgZ7pOUJVzFrm68PQpw4A0NwhvWYdU+Vy2X6ijaEDJu0cU"
CHECK_ENC = "UwhNS1km4aoePVfrIfCz2bR3LJcLRsnw0alwVqYRDSqKBbpihdmJsNtMyEpaWAZJw5Ts"

FOLDER = "lms_msgr_kdtm"

master_password = "0"

def check_password(password: str) -> bool:
    """Проверяет, правильный ли пароль"""
    try:
        result = decrypt(CHECK_ENC, get_master_password(password)).decode()
        return result == "FreeNet"
    except Exception as e:
        return False

def get_master_password(password:str):
    return hashlib.sha512(password.encode()).hexdigest()

def get_password() -> str:
    try:
        return decrypt(PASSWORD_ENC, get_master_password(master_password)).decode()
    except:
        return "0"

def get_key(password, salt):
    """Делает ключ из пароля и соли"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=300000,
    )
    return kdf.derive(password.encode())

def encrypt(data, password):
    """Шифрует данные паролем. Возвращает зашифрованный файл"""
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)
    key = get_key(password, salt)
    
    ciphertext = AESGCM(key).encrypt(nonce, data, None)

    b64_text = base64.b64encode(salt + nonce + ciphertext).decode('utf-8')
    return b64_text

def decrypt(b64_text, password):
    try:
        """Расшифровывает данные паролем. Возвращает исходные данные"""
        encrypted_data = base64.b64decode(b64_text)
        salt = encrypted_data[:SALT_SIZE]
        nonce = encrypted_data[SALT_SIZE:SALT_SIZE+NONCE_SIZE]
        ciphertext = encrypted_data[SALT_SIZE+NONCE_SIZE:]
        
        key = get_key(password, salt)
        
        return AESGCM(key).decrypt(nonce, ciphertext, None)
    except Exception as e:
        return json.dumps({"filename":"errdec.n", "data":{"version":"0", "data":[["title", {"text":"Ошибка"}], ["label", {"text":f"Ошибка дешифрования {e}"}]]}}).encode()

def listdir(dirname:str, dirs = False):
    if client.exists(dirname):
        files = []
        for item in client.listdir(dirname):
            if not dirs:
                files.append(item.name)
            else:
                files.append(item.name, item.type)
        return files
    else:
        raise ValueError("Dir not found")

def get_file_data(path:str):
    if client.exists(path):
        buffer = io.BytesIO()
        client.download(path, buffer)
        data = decrypt(buffer.getvalue().decode("utf-8"), get_password()).decode()
        return data
    else:
        raise FileNotFoundError(path)

def create_file(filename:str, data:str):
    if client.exists(filename):
        raise ValueError(f"File {filename} already exists")
    else:
        buffer = io.BytesIO(bytes(encrypt(data.encode(), get_password()), "utf-8"))
        client.upload(buffer, filename)
        return True



def SEND(message_text:str, to_user_id:str, my_user_id:str):
    now = datetime.now()
    time_now = now.strftime("%d/%m/%Y")     #Время в формате ДД/ММ/ГГГГ
    file_name = f"{my_user_id}|{time_now}"
    if client.exists(FOLDER):
        if client.exists(f"{FOLDER}/{to_user_id}"):
            create_file(f"{FOLDER}/{to_user_id}/{file_name}", message_text)
        else:
            return ValueError(f"Folder {FOLDER}/{to_user_id} not found")
    else:
        return ValueError(f"Folder {FOLDER} not found")

def GET(my_user_id:str, split_time = "01/03/2000", auto_del = False): #split_time тоже в формате ДД/ММ/ГГГГ
    list_messages_not_parsed = listdir(f"{FOLDER}/{my_user_id}")
    result = {}
    for message in list_messages_not_parsed:
            if "|" in message:
                if len(message.split("|")) == 2:
                    from_userid = message.split("|")[0]

                    timestmp = message.split("|")[1]    #Время в формате ДД/ММ/ГГГГ

                    time_split_converted = datetime.strptime(split_time, "%d/%m/%Y")
                    time_sended_converted = datetime.strptime(timestmp, "%d/%m/%Y")

                    if time_sended_converted >= time_split_converted:
                        if not from_userid in result.keys():
                            result[from_userid] = []
                        result[from_userid].append([timestmp, get_file_data(f"{FOLDER}/{my_user_id}/{message}")])
                    else:
                        continue
                else:
                    continue
            else:
                continue
    return result

            
    
