import sqlite3


DB_FILE = "chats.db"



def create_db():
    db = sqlite3.connect(DB_FILE)
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS chats (
        chat_id TEXT,
        chat_name TEXT,
        chat_description TEXT,
        avatar TEXT
    )
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
        sender_id TEXT,
        to_id TEXT,
        data TEXT,
        timestmp FLOAT
    )
    """)

    db.commit()
    db.close()

def is_chat_exists(chat_id:str):
    db = sqlite3.connect(DB_FILE)
    cursor = db.cursor()

    cursor.execute("SELECT chat_name FROM chats WHERE chat_id = ?", (chat_id,))
    res = cursor.fetchone()
    db.close()
    if res == None:
        return False
    else:
        return True
    
def create_chat(chat_id:str, chat_description = "Это описание чата", chat_name = "Чат", avatar = "👤"):
    if not is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("INSERT INTO chats (chat_id, chat_name, chat_description, avatar) VALUES(?, ?, ?, ?)", (chat_id, chat_name, chat_description,avatar,))

        db.commit()
        db.close()

    else:
        raise ValueError(f"{chat_id} : Уже есть чат с таким ID")

def get_chat_name(chat_id:str):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("SELECT chat_name FROM chats WHERE chat_id = ?", (chat_id,))
        chat_name = cursor.fetchone()

        db.close()
        return chat_name[0]

    else:
        raise ValueError(f"{chat_id} : Нету такого чата")

def update_chat_name(chat_id:str, new_name:str):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("""
            UPDATE chats 
            SET chat_name = ?
            WHERE chat_id = ?
        """, (new_name , chat_id,))
        
        db.commit()
        db.close()
    else:
        raise ValueError(f"{chat_id} : Нету такого чата")

def get_chat_description(chat_id:str):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("SELECT chat_description FROM chats WHERE chat_id = ?", (chat_id,))
        chat_description = cursor.fetchone()

        db.close()
        return chat_description[0]

    else:
        raise ValueError(f"{chat_id} : Нету такого чата")

def update_chat_description(chat_id:str, new_chat_description:str):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("""
            UPDATE chats 
            SET chat_description = ?
            WHERE chat_id = ?
        """, (new_chat_description , chat_id,))
        
        db.commit()
        db.close()
    else:
        raise ValueError(f"{chat_id} : Нету такого чата")

def get_chat_avatar(chat_id:str):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("SELECT avatar FROM chats WHERE chat_id = ?", (chat_id,))
        chat_description = cursor.fetchone()

        db.close()
        return chat_description[0]

    else:
        raise ValueError(f"{chat_id} : Нету такого чата")

def update_chat_avatar(chat_id:str, new_avatar:str):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        cursor.execute("""
            UPDATE chats 
            SET avatar = ?
            WHERE chat_id = ?
        """, (new_avatar , chat_id,))
        
        db.commit()
        db.close()
    else:
        raise ValueError(f"{chat_id} : Нету такого чата")

def create_message(sender_id:str, to_id:str, data:str, timestmp:float):
    if is_chat_exists(to_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()
        cursor.execute("INSERT INTO messages (sender_id, to_id, data, timestmp) VALUES (?, ?, ?, ?)", (sender_id, to_id, data, timestmp,))
        
        db.commit()
        db.close()
    else:
        create_chat(to_id)
        create_message(sender_id, to_id, data, timestmp)

def get_messages_in_chat(chat_id:str, time_split = 0.0):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        if int(chat_id) >= 0:# Если это личка то айди чата - это айди собеседника. 
                             # Если это группа, то вместо собственного айди, клиент подставляет айди группы и соответсвенно айди чата - это айди поулчателя
            
            cursor.execute("SELECT * FROM messages WHERE sender_id = ? and timestmp > ?", (chat_id, time_split,))

            res = cursor.fetchall()
            db.close()

            return res
        else:
            raise ValueError("Группы не реализованы")
    else:
        raise ValueError(f"{chat_id} : Чат не существует")

def del_all_messages_in_chat(chat_id:str):
    if is_chat_exists(chat_id):
        db = sqlite3.connect(DB_FILE)
        cursor = db.cursor()

        if int(chat_id) >= 0:

            cursor.execute("DELETE FROM messages WHERE sender_id = ?", (chat_id,))
            db.commit()
            db.close()


        else:
            raise ValueError("Группы не реализованы")
    else:
        raise ValueError(f"{chat_id} : Чат не существует") 

def get_chats_list():
    db = sqlite3.connect(DB_FILE)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM chats")

    res = cursor.fetchall()
    db.close()
    return res

create_db()
print(get_chats_list())


