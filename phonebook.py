import os


def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding = 'utf-8') as data:
            data.write("")

def add_new_user(name: str, phone: str, filename: str):
    with open(filename, 'r+t', encoding = 'utf-8') as wrtbl:
       #l = wrtbl.readlines()
       lins_count = len(wrtbl.readlines())
       wrtbl.write(f"{lins_count + 1};{name};{phone}\n")
       return 'Запись добавлена'


def read_all(filename: str) -> str:
    with open(filename, 'r', encoding = 'utf-8') as data:
        resolt = data.read()   
    return resolt


def search_user(data: str, filename: str) -> str:
    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
        res = [item for item in text if data.lower() in item.lower()]
    return '\n'.join(res) if res else 'Вхождений не найдено'

def copy_user(number: int, filename_date: str, filename_copy: str) -> str:
    with open(filename_date, 'r', encoding = 'UTF-8') as content, open(filename_copy, 'r+t', encoding = 'utf-8') as wrtbl:
        text = content.readlines()
        res = [item for item in text if number == int(item[:len(str(number))])]
        if res is not None:
            wrtbl.write(f'{res}\n')
            print('Запись: ',res, ' добавлена в файл ',filename_copy)
        else:
            print('Вхождений не найдено')

    


INFO_STRING = """ 
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - скопировать строку
"""

DATASOURCE = 'phone.txt'
DATACOPY = 'phonecopy.txt'


check_directory(DATASOURCE)
check_directory(DATACOPY)


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:        
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        add_new_user(name=user, phone=phone, filename=DATASOURCE)
    elif mode == 3:
        search = input ('Введите строку поиска ')
        print(search_user(search, DATASOURCE))
    elif mode == 4:
        num_search = int(input('Введите номер строки: '))
        copy_user(num_search, DATASOURCE, DATACOPY)

