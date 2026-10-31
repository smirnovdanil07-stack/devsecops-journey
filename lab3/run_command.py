import subprocess
import sys

# Проверяем, передал ли пользователь команду
if len(sys.argv) < 2:
    print("Ошибка: укажи команду. Пример: python3 run_command.py ls -la")
    sys.exit(1)

# Собираем команду из всех аргументов (например, "ls" и "-la")
command = sys.argv[1:]

print(f"Выполняю команду: {' '.join(command)}")
print("-" * 40)

try:
    # Запускаем команду и захватываем вывод
    result = subprocess.run(
        command,
        capture_output=True,  # Захватываем stdout и stderr
        text=True,            # Возвращаем строку, а не байты
        check=True            # Если команда упадет с ошибкой, выбросит исключение
    )
    
    # Выводим стандартный вывод (stdout)
    print(result.stdout)
    
except subprocess.CalledProcessError as e:
    # Если команда завершилась с ошибкой (например, нет такого файла)
    print(f"Ошибка выполнения команды (код {e.returncode}):")
    print(e.stderr)
except FileNotFoundError:
    # Если команды вообще не существует в системе
    print(f"Команда '{command[0]}' не найдена в системе.")
