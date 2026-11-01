import sys

keywords = ["ERROR", "WARNING"]

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
            if any(word in line for word in keywords):  # <--- ЗАМЕНИ "..." на слово, которое ищешь (в кавычках)
                error_count = error_count + 1
                # 4. Сохраняем первые 5 строк с ошибками
                if len(error_lines) < 5:
                    error_lines.append(line.strip()) # strip() убирает лишние пробелы и переносы

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
    sys.exit(1)

# 5. Выводим результаты
print(f"Найдено ошибок: {error_count}")

with open("report.txt", "w") as report:
    report.write(f"Найдено ошибок: {error_count}\n")
    report.write("Первые 5 ошибок:\n")
    for err in error_lines:
        report.write(f" - {err}\n")
    if error_count > 5:
        report.write(f" ... и еще {error_count - 5} ошибок.\n")

if error_count > 0:
    print("\nПервые 5 ошибок:")
    for err in error_lines:
        print(f" - {err}")
    
    if error_count > 5:
        print(f" ERROR и еще {error_count - 5} ошибок.")
else:
    print("Ошибок не найдено. Все чисто!")
