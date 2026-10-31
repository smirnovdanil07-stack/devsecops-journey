Скрипт 1: first_script.py (Создание папки и файла)
Для чего нужен: Это база. Он показывает, как Python взаимодействует с файловой системой. В DevSecOps ты будешь использовать такие конструкции, чтобы создавать папки для логов, отчетов сканеров или конфигураций.

Что он делает:

Принимает имя папки из аргументов командной строки (через sys.argv).
Проверяет, существует ли она (os.path.exists).
Если нет — создает (os.makedirs).
Создает внутри файл hello.txt и пишет туда текст.
Ключевые модули: import os, import sys.


import os

 1. Создаем папку (если её нет)
folder_name = "python_test"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Папка '{folder_name}' создана.")
else:
    print(f"Папка '{folder_name}' уже существует.")

 2. Создаем файл и записываем в него текст
file_path = os.path.join(folder_name, "hello.txt")
with open(file_path, "w") as f:
    f.write("Привет, это мой первый Python-скрипт для DevSecOps!\n")
    f.write("Я учусь автоматизировать рутину.\n")

print(f"Файл '{file_path}' создан и заполнен.")

 3. Читаем файл и выводим его содержимое
with open(file_path, "r") as f:
    content = f.read()
    print("\n--- Содержимое файла ---")
    print(content)
    print("------------------------")

 4. Выводим список файлов в текущей директории
print("\nФайлы в текущей папке:")
for item in os.listdir("."):
    print(f" - {item}")


Скрипт 2: run_command.py (Запуск команд Linux)
Для чего нужен: Это твой мост в системное администрирование. Ты пишешь скрипт на Python, который внутри себя запускает ls, git, docker или nmap. Это нужно для автоматизации. Например, скрипт, который сам запускает nmap и парсит результаты.

Что он делает:

Принимает команду из аргументов (например, ls -la).
Запускает её через subprocess.run.
Захватывает вывод (capture_output=True).
Если команда упала с ошибкой — ловит исключение (try/except) и выводит stderr.
Ключевые модули: import subprocess, import sys.



import os

 Запрашиваем имя папки у пользователя
folder_name = input("Введите имя папки для создания: ")

 Проверяем, не пустая ли строка
if not folder_name.strip():
    print("Ошибка: имя папки не может быть пустым!")
else:
    if not os.path.exists(folder_name):
        try:
            os.makedirs(folder_name)
            print(f"Папка '{folder_name}' успешно создана.")
            
            # Создаем файл внутри
            file_path = os.path.join(folder_name, "info.txt")
            with open(file_path, "w") as f:
                f.write(f"Это файл внутри папки {folder_name}\n")
            print(f"Файл '{file_path}' создан.")
            
        except PermissionError:
            print(f"Ошибка: нет прав на создание папки '{folder_name}'.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    else:
        print(f"Папка '{folder_name}' уже существует.")


Как спросить существуел ли папка


Способ 1: os.path.exists() (Проверяет вообще всё)
Эта команда проверяет, существует ли вообще что-то по указанному пути — папка это, файл или просто пустое место.


import os

if os.path.exists("python_test"):
    print("Папка существует")
else:
    print("Папки нет")


Способ 2: os.path.isdir() (Проверяет именно папку)
Эта команда проверяет, существует ли путь и является ли он именно директорией (папкой), а не файлом.


import os

if os.path.isdir("python_test"):
    print("Это папка, и она существует")
else:
    print("Это не папка или её нет")


Скрипт 3: check_logs.py (Парсинг логов — мы не успели дописать)
Для чего нужен: Это твой хлеб. В DevSecOps 80% времени — это чтение логов. Этот скрипт ищет в файле ошибки и выводит их.

Что он должен делать:

Принимает путь к файлу лога.
Открывает файл (with open(...)).
В цикле ищет строки со словом "ERROR".
Считает их количество и выводит первые 5.
Ключевые модули: import sys, встроенная функция open().



import os
import sys

 Проверяем, передал ли пользователь аргумент
if len(sys.argv) < 2:
    print("Ошибка: укажи имя папки. Пример: python3 first_script.py my_folder")
    sys.exit(1)  # Выходим с ошибкой

 Берем имя папки из аргументов (первый аргумент после имени скрипта)
folder_name = sys.argv[1]

if os.path.exists(folder_name):
    print(f"Папка '{folder_name}' уже существует.")
else:
    print(f"Папки '{folder_name}' нет. Создаю...")
    os.makedirs(folder_name)
    print(f"Папка '{folder_name}' успешно создана!")




Команда nano "Название файла".py

Скрипт для поиска ошибок и логов 

import sys

keywords = ["", ""]    # <--- В данную строку слова который мы изем через запятую в "" "ERROR", "WARNING", "CRITICAL" , SQL_INJECTION , Failed

# 1. Проверяем, передал ли пользователь путь к файлу
if len(sys.argv) < 2:
    print("Ошибка: укажи путь к файлу. Пример: python3 check_logs.py test.log")
    sys.exit(1)

file_path = sys.argv[1]

# Переменные для подсчета и хранения строк
error_count = 0
error_lines = []

# 2. Открываем файл и читаем его построчно
try:
    with open(file_path, 'r') as f:
        for line in f:
            # 3. Проверяем, есть ли в строке слово "ERROR"
            if any(word in line for word in keywords):  # <--- ЗАМЕНИ "..." на слово, которое ищешь (>
                error_count = error_count + 1



                # 4. Сохраняем первые 5 строк с ошибками
                if len(error_lines) < 5:
                    error_lines.append(line.strip()) # strip() убирает лишние пробелы и переносы

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
    sys.exit(1)

# 5. Выводим результаты
print(f"Найдено ошибок: {error_count}")

if error_count > 0:
    print("\nПервые 5 ошибок:")
    for err in error_lines:
        print(f" - {err}")

    if error_count > 5:
        print(f" ERROR и еще {error_count - 5} ошибок.")
else:
    print("Ошибок не найдено. Все чисто!")

