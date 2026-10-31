import os
import sys

# Проверяем, передал ли пользователь аргумент
if len(sys.argv) < 2:
    print("Ошибка: укажи имя папки. Пример: python3 first_script.py my_folder")
    sys.exit(1)  # Выходим с ошибкой

# Берем имя папки из аргументов (первый аргумент после имени скрипта)
folder_name = sys.argv[1]

if os.path.exists(folder_name):
    print(f"Папка '{folder_name}' уже существует.")
else:
    print(f"Папки '{folder_name}' нет. Создаю...")
    os.makedirs(folder_name)
    print(f"Папка '{folder_name}' успешно создана!")

