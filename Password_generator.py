import random as rnd

def generate_passwords(long, chars):
     '''генерируем пасс'''
     password = ''
     for _ in range(long):
         password += rnd.choice(chars)
         print(password)



digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

  

print('Добро пожаловать в генератор паролей!)')
count_pass = int(input('Сколько паролей сгенерировать?:'))
long_pass = int(input('Длинна пароля: '))


if input('Напиши да, чтобы разрешить прописные буквы:') == 'да':
    chars += lowercase_letters


if input('Напиши да, чтобы разрешить заглавные буквы:') == 'да':
    chars += uppercase_letters


if input('Напиши да, чтобы разрешить цифры:') == 'да':
    chars += digits


if input('Напиши да, чтобы разрешить символы:') == 'да':
    chars += punctuation
  

if input('Напиши да, чтобы разрешить неоднозначные символы "il1Lo0O":') != 'да':
    for _ in 'il1Lo0O':
        chars = chars.replace(_,'')


for _ in range(count_pass):
    generate_passwords(long_pass, chars)