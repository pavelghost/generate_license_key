import random
import string

def generate_license_key():
    characters = string.ascii_uppercase.replace('Z', '').replace('L', '').replace('A', '').replace('E', '').replace('S', '').replace('I', '').replace('U', '')
    digits = string.digits.replace('0', '').replace('1', '')

    key = ''.join(random.choice(characters + digits) for _ in range(5))
    key += '-' + ''.join(random.choice(characters + digits) for _ in range(5))
    key += '-' + ''.join(random.choice(characters + digits) for _ in range(5))
    key += '-' + ''.join(random.choice(characters + digits) for _ in range(5))
    key += '-' + ''.join(random.choice(characters + digits) for _ in range(5))

    return key

# Генерируем 5 примеров ключей и сохраняем их в файл "keys.txt"
with open('keys.txt', 'w') as file:
    for _ in range(1000):
        key = generate_license_key()
        file.write(key + '\n')

print("Ключи сгенерированы и сохранены в файл 'keys.txt'.")