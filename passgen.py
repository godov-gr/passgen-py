import itertools
import random
import time
import os

def show_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔══════════════════════════════════════╗")
    print("║          🚀 Password Generator       ║")
    print("║   Создай уникальные и сложные пароли ║")
    print("╚══════════════════════════════════════╝")
    print("\nДобро пожаловать! Следуйте инструкциям ниже.")
    time.sleep(1.5)

# Показ интро перед началом работы.
show_intro()

# Функция для замены некоторых букв на похожие символы.
def replace_with_symbols(word):
    replacements = {"o": "0", "a": "@", "e": "3", "i": "1", "k": "<"}
    return ''.join(replacements.get(c, c) for c in word)

# Функция для генерации паролей.
def generate_passwords(birth_date, surname, nickname, other_data):
    special_chars = ["!", "@", "#", "$", "%", "&", "*"]
    numbers = ["123", "007", "911", "000", "321", "456", "789"]

    # Список всех данных для генерации.
    data_variants = []
    if birth_date:
        data_variants.append(birth_date)
    if surname:
        data_variants.append(surname)
    if nickname:
        data_variants.append(nickname)
    if other_data:
        data_variants.append(other_data)

    if not data_variants:
        print("Нет данных для генерации паролей.")
        return []

    password_variations = set()

    # Генерация комбинаций.
    for combination in itertools.permutations(data_variants, 2):
        base = ''.join(combination)
        password_variations.add(base)
        password_variations.add(base.capitalize())
        password_variations.add(replace_with_symbols(base))
        password_variations.add(replace_with_symbols(base).capitalize())

        # Добавляем специальные символы и числа.
        for char, num in itertools.product(special_chars, numbers):
            password_variations.add(base + char + num)
            password_variations.add(char + base + num)
            password_variations.add(base + num + char)

        # Перемешиваем части и добавляем символы.
        shuffled_parts = list(base + random.choice(numbers))
        random.shuffle(shuffled_parts)
        password_variations.add(''.join(shuffled_parts))
        password_variations.add(''.join(shuffled_parts).capitalize())

    return password_variations

# Ввод данных.
birth_date = input("Введите дату рождения (или оставьте пустым): ").strip()
surname = input("Введите фамилию (или оставьте пустым): ").strip()
nickname = input("Введите никнейм (или оставьте пустым): ").strip()
other_data = input("Введите прочие данные (или оставьте пустым): ").strip()

# Генерация паролей.
passwords = generate_passwords(birth_date, surname, nickname, other_data)

if passwords:
    # Сохранение паролей в файл.
    with open("generated_passwords.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")
    print(f"Сгенерировано {len(passwords)} уникальных паролей в файле generated_passwords.txt")
else:
    print("Пароли не были сгенерированы.")