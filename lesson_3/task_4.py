"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib
from uuid import uuid4

s_hash = set()
salt = uuid4().hex


def cache(url):
    hashed_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url not in s_hash:
        s_hash.add(hashed_url)
    return hashed_url


url = ''
while url != 'q':
    url = input('Введите URL: ')
    print(cache(url))
