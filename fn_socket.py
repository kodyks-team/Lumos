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
import time
from threading import Thread
import textwrap


TOKEN = "y0__wgBEI7P1rsHGK2tPyCepcn2GDC9-KLlB2T1Lktn2skHCpc2GgPqFTFZtbvB"
client = yadisk.Client(token=TOKEN)

SALT_SIZE = 16
NONCE_SIZE = 12

PASSWORD_ENC = "DG2rUstjFxkhC2XlZT1c9DHjp82T0QDe7hvClJ1hKNweC1+9gz5FQl7GRmARr4Yf9DsRI6ANgy8aoyRMXBlP4aWa8wI4FXtxDsZiDgU+BBG24d+p3TtFeeXDDRhKTn+r82yOlaIBG6aTFmoGePvuk5B0FVYqmqC4eXBMI+sph5BP9CmcDMFUsUwWOkAc017R2ovOGVQPuZnihPF3w8xK7UC0Uo0ByO+mWQYp5BgkSrMpWhmQwcT7bLKgWIBrIQ7dvNmpqH5a+ZU5mvtUty3ePVJI2Zsv9tve6n0h3yguxlfT6+hlb/Uk+DXIUp/7AD6ARUA1POUMPwWY6fIbZp9RZvfCzlwFvn9UiBRgZ7pOUJVzFrm68PQpw4A0NwhvWYdU+Vy2X6ijaEDJu0cU"
CHECK_ENC = "UwhNS1km4aoePVfrIfCz2bR3LJcLRsnw0alwVqYRDSqKBbpihdmJsNtMyEpaWAZJw5Ts"

FOLDER = "lms_msgr_kdtm"
FOLDER_USERS_LIST = "lms_msgr_kdtm_u"

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
        raise e

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

def enocde_safe_filename(text:str):
    text = text.replace("/", "_")
    text = text.replace("+", "-")
    return text

def decode_safe_filename(text:str):
    text = text.replace("_", "/")
    text = text.replace("-", "+")
    return text

def SEND(message_text:str, to_user_id:str, my_user_id:str):
    

    wraped = False
    wraped_message = textwrap.wrap(message_text, 50)
    if len(wraped_message) > 1:
        wraped = True
    wraped_message = list(map(lambda x: f"{x}{int(wraped)}" , wraped_message))

    users_list = get_all_user_ids()
    
    if client.exists(FOLDER):
        if to_user_id in users_list:
            if my_user_id in users_list:
                for message_part in wraped_message:
                    file_name = f"{my_user_id}|{time.time()}|{enocde_safe_filename(encrypt(message_part.encode(), get_password()))}"
                    create_file(f"{FOLDER}/{to_user_id}/{file_name}", "")
            else:
                return ValueError(f"user {my_user_id} not found")
        else:
            return ValueError(f"user {to_user_id} not found")
    else:
        return ValueError(f"Folder {FOLDER} not found")

def GET(my_user_id:str, split_time = 0, auto_del = False):
    list_messages_not_parsed = listdir(f"{FOLDER}/{my_user_id}")
    result = {}
    for message in list_messages_not_parsed:
            if "|" in message:
                if len(message.split("|")) == 3:
                    timestmp = float(message.split("|")[1])
                    if timestmp >= split_time:
                        from_userid = message.split("|")[0]
                        
                        data = decrypt(decode_safe_filename(message.split("|")[2]), get_password()).decode()

                        if auto_del:
                            client.remove(f"{FOLDER}/{my_user_id}/{message}")
                        if not from_userid in result.keys():
                            result[from_userid] = []
                        result[from_userid].append([timestmp, data])
                    else:
                        continue
                else:
                    continue
            else:
                continue
    return result


def get_all_user_ids():
    return listdir(FOLDER)

def get_users_list():
    try:
        return list(map(lambda x: (x.split("|")[0], x.split("|")[1]), listdir(FOLDER_USERS_LIST)))
    except Exception as e:
        raise e

def get_usernames_list():
    try:
        return list(map(lambda x: x.split("|")[0], listdir(FOLDER_USERS_LIST)))
    except Exception as e:
        raise e

def create_user(username:str, description = "", avatar = "👤"):
    st_time = time.time()
    username = username.replace("|", "")
    if username in get_usernames_list():
        raise ValueError(f"{username} уже используется")
    list_users = get_all_user_ids()
    count = 10
    while str(count) in list_users:
        if count > 99:
            raise ValueError("Создать аккаунт невозможно, все ID с 10 до 99 заняты")
        count += 1
    client.mkdir(f"{FOLDER}/{count}")
    client.mkdir(f"{FOLDER}/{count}/userinfo")
    t1 = Thread(target = lambda : create_file(f"{FOLDER}/{count}/userinfo/user.json", json.dumps({"user_id":str(count),"username":username, "description":description, "avatar":avatar})))
    t2 = Thread(target = lambda : create_file(f"{FOLDER}/{count}/userinfo/last_change", str(time.time())))
    t3 = Thread(target = lambda : create_file(f"{FOLDER_USERS_LIST}/{username}|{count}", " "))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    print(time.time()-st_time)
    return count

def get_user_info(user_id:str, last_update_time:float = None):
    """
    Поулчает информацию о пользователе/группе(в будущем)
    Если не указывать время последнего обновления информации о юзере в локальной бд то возвращает True и инфу о пользователе 
    Иначе возвращает True/False в зависимости от того обновлялась ли инфа после указонного времени последего обновления в локальной бд и сами данные (в случае False {})
    данные в таком виде (словарь)
    {"user_id":id[str],"username":username[str], "description":description[str], "avatar":avatar[str]}
    """
    if user_id in get_all_user_ids():
        last_change_time = float(get_file_data(f"{FOLDER}/{user_id}/userinfo/last_change"))
        if last_update_time != None:
            if last_change_time > last_update_time:

                userinfo = json.loads(get_file_data(f"{FOLDER}/{user_id}/userinfo/user.json"))
                
                return True, userinfo
            else:
                return False, {}
        else:
            userinfo = json.loads(get_file_data(f"{FOLDER}/{user_id}/userinfo/user.json"))
                
            return True, userinfo
    else:
        raise ValueError(f"{user_id} Даник долбаеб")