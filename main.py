import os
from cryptography.fernet import Fernet
from logging import logging
from uploading import uploading_files

source = input("Введите путь к папке, в которой лежат все файлы, которые вы хотите расшифровать: ")
dest = uploading_files(source)

def load_key():                             # Загружаем ключ 'crypto.key' из текущего каталога
    return open('crypto.key', 'rb').read()

def decrypt(filename, key):
# Расшифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

key = load_key()                            # загрузить ключ

rez = os.listdir(dest)
for item in rez:
    str = "файлы/"
    decrypt(str + item, key)
    logging(item, "обратное преобразование")
