# -*- coding: utf-8 -*-
# x1, y1, x2, y2 = int(input()),int(input()),int(input()),int(input())
#
# if abs(x1 - x2) == abs(y1 - y2):
#     print("YES")
# else:
#     print("NO")
import random
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# # Проверяем условие
# # if abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(
# y1 - y2) == 2:
# if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
#     print("YES")
# else:
#     print("NO")

# n = int(input())
# s = input()
#
#
# for i in s:
#     a = ord(i)-n
#
#     if a<97:
#         a=123-(97-a)
#
#     print(chr(a),end='')


# s = input()
# result = ""
# for i in range(len(s)):
#     if (i) % 3 != 0 :
#         result += s[i]
# print(result)


# s = input()
# if s.find('f')>-1 and s.count('f')==1:
#     print('-1')
# elif s.count('f')>1:
#     s=s[:s.find('f')]+s[s.find('f')+1:]
#     print(s.find('f')+1)
# else:
#     print('-2')


# n = int(input())
# l = []
# k=[]
# for i in range(n):
#     s = input()
#     l.append(s)
# s=int(input())
# for j in l:
#     if s<=len(j):
#         print(j[s-1],end='')

# n = int(input())
# k = []
# for i in range(n):
#     x = int(input())
#     k.append(x)
# k.remove(min(k))
# k.remove(max(k))
# print(*k, sep='\n')

# n = int(input())
# strings = []
# for _ in range(n):
#     string = input()
#     if string not in strings:
#         strings.append(string)
# print(*strings,sep='\n')


# n = int(input())
# strings = []
# for _ in range(n):
#     strings.append(input())
#
# k = int(input())
# queries = []
# for _ in range(k):
#     queries.append(input())
#
# z = []
# for i in strings:
#     found = True
#     for q in queries:
#         if q.lower() not in i.lower():
#             found = False
#             continue
#     if found:
#         z.append(i)
#
# print(*z,sep='\n')


# n = int(input())
# s = []
# for _ in range(n):
#     s.append(int(input()))
# a=[]
# b=[]
# c=[]
# for i in s:
#     if i<0:
#         a.append(i)
#     elif i==0:
#         b.append(i)
#     else:
#         c.append(i)
#
# a.extend(b)
# a.extend(c)
# print(*a,sep='\n')

#
# n = input().split()
# l=[]
# for i in n:
#     l.append(int(i))
#
# mn = l.index(min(l))
# mx = l.index(max(l))
#
# l[mn], l[mx] = l[mx], l[mn]
#
# print(*l,sep=' ')


# s = input()
# words = s.split()
# longest_word_length = max([len(word) for word in words])
# print(longest_word_length)


# s = input()
# result = [word[1:] + word[0] + 'ки' for word in s.split()]
# print(' '.join(result))


# def draw_box():
#     matrix = [['*' if i == 0 or j == 0 or i == 13 or j == 9 else ' ' for j
#     in range(10)] for i in range(14)]
#     for row in matrix:
#         print(*row, sep='', end='\n')
# #     for i in range(14):
# #
# #         for j in range(10):
# #             if i==0 or j==0 or i==13 or j ==9:
# #                 print('*',end='')
# #             # elif j>0 and j<9:
# #             else:
# #                 print(' ',end='')
# #
# #         print()
# #
# draw_box()


# def draw_triangle():
#     matrix = [['*' for j in range(i+1)] for i in range(10)]
#     for row in matrix:
#         print(*row, sep='', end='\n')
#
# draw_triangle()

# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1
#
# print_text('Python', 4)

# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(fill * i)
#     for j in range(base // 2, 0, -1):
#         print(fill * j)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)

# def print_digit_sum(num):
#     l = [int(i) for i in str(num)]
#     print(sum(l))
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)
#
# n = int(input("Введите высоту треугольника: "))
#
# # Вывод верхней половины треугольника
# for i in range(1, n + 1):
#     print('*' * i)
#
# # Вывод нижней половины треугольника
# for i in range(n - 1, 0, -1):
#     print('*' * i)


# n = int(input("Введите количество строк: "))
# i = 1
#
# # Выводим треугольник восходящей последовательности
# while i <= n:
#     print("*" * i)
#     i += 1
#
# # Выводим треугольник нисходящей последовательности
# i = n - 1
# while i >= 0:
#     print("*" * i)
#     i -= 1


# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя
#     бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     else:  # иначе прицепляем остаток другого списка
#         result += list2[p2:]
#
#     return result
# l=[]
# n = int(input())
# l1= [int(q) for q in input().split()]
# for i in range(1,n):
#     l2=[int(q) for q in input().split()]
#     l1=quick_merge(l1,l2)
#
# print(*l1)


# def is_prime(num):
#     c = 0
#     for i in range(1,num+1):
#
#         if num%i==0:
#             c+=1
#     if c>2 or num==1:
#
#         return False
#     else:
#
#         return True
#
# # считываем данные
# n = int(input())
# v=1
# f=True
# while f:
#     if is_prime(n+v):
#
#         print(n+v)
#         f=False
#     else:
#         v+=1
#
#
# # вызываем функцию
# is_prime(n)

# def is_prime(num):
#     if num <= 1:
#         return False
#
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
# # считываем данные
# n = int(input())
# v = 1
# while True:
#     if is_prime(n + v):
#         print(n + v)
#         break
#     else:
#         v += 1
#
# # вызываем функцию
# is_prime(n)


# def is_password_good(password):
#     u = False
#     l = False
#     d = False
#     if password.isalnum() and len(password) > 7:
#
#         for i in password:
#             if i == i.upper() and i.isalpha():
#                 u = True
#             if i == i.lower() and i.isalpha():
#                 l = True
#             if i.isdigit():
#                 d = True
#
#     if u == True and l == True and d == True:
#         print('True')
#     else:
#         print('False')
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# is_password_good(txt)
#
#
# def is_password_good(password):
#     if len(password) >= 8 and any(char.isupper() for char in password) and
#     any(
#             char.islower() for char in password) and any(char.isdigit()
#             for char in password):
#         return True
#     else:
#         return False


# def is_one_away(word1, word2):
#     l = 0
#     if len(word1)==len(word2):
#
#         for i in range(len(word1)):
#             if word1[i]!=word2[i]:
#                 l+=1
#     if l==1:
#         print('True')
#     else:
#         print('False')
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# is_one_away(txt1, txt2)
#
# def is_one_away(word1, word2):
#     l = 0
#     if len(word1) != len(word2):
#         print('False')
#         return
#
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             l += 1
#         if l > 1:
#             print('False')
#             return
#
#     print('True')
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# is_one_away(txt1, txt2)

#
# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#
#     difference_count = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             difference_count += 1
#
#     return difference_count == 1


# def is_palindrome(text):
#     s=''
#     t=''
#     for a in text:
#         if a.isalpha():
#             s+=a
#     for b in text[::-1]:
#         if b.isalpha():
#             t+=b
#     text=s
#     print(text)
#     f=0
#     t2=t
#     print(t2)
#     print('*******************************')
#     for i in range(len(text)):
#         if text[i].lower()==t2[i].lower():
#             f+=1
#     if f==len(text):
#         print('True')
#     else:
#         print('False')
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# is_palindrome(txt)
#
#
#
# def is_palindrome(text):
#     # Удаление символов , . ! ? -
#     text = text.replace(',', '').replace('.', '').replace('!',
#     '').replace('?', '').replace('-', '')
#     # Удаление пробелов
#     text = text.replace(' ', '')
#     # Приведение текста к нижнему регистру
#     text = text.lower()
#     # Проверка на палиндром
#     return text == text[::-1]


# def is_valid_password(password):
#     p=password.split(':')
#
#     c=0
#     if p[0]==p[0][::-1]:
#         c+=1
#     if int(p[1])>1:
#         for i in range(2, int(int(p[1]) ** 0.5) + 1):
#             if int(p[1]) % i == 0:
#                 c+=1
#     if int(p[2])%2==0:
#         c += 1
#
#     if c==2:
#         return True
#     else:
#         return False
#
#
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))


# def is_valid_password(password):
#     p = password.split(':')
#     c = 0
#
#     if p[0] == p[0][::-1]:
#         c += 1
#
#     if int(p[1]) > 1:
#         for i in range(2, int(p[1] ** 0.5) + 1):
#             if int(p[1]) % i == 0:
#                 c += 1
#
#     if int(p[2]) % 2 == 0:
#         c += 1
#
#     return c == 2

# def is_valid_password(password):
#     p = password.split(':')
#     c = 0
#     if len(p)==3:
#
#
#         if p[0] == p[0][::-1]:
#             c += 1
#
#         if int(p[1]) > 1:
#             for i in range(2, int(p[1])):
#                 if int(p[1]) % i == 0:
#                     c += 1
#
#         if int(p[2]) % 2 == 0:
#             c += 1
#
#     return c == 2
#
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))


# def is_correct_bracket(text):
#     while '()' in text:
#         text=text.replace('()','')
#     return  text==''
#
# def is_correct_bracket(text):
#     text=text.strip()
#     c=-1
#
#     if text[0]=='(':
#         c = 0
#         for i in range(len(text)):
#             if text[i]=='(':
#                 c+=1
#             else:
#                 c-=1
#                 if c<0:
#                     return False
#     return  c==0
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))

# def convert_to_python_case(text):
#     python_case = ""
#     for char in text:
#         if char.isupper():
#             python_case += "_" + char.lower()
#         else:
#             python_case += char
#     return python_case.lstrip("_")
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))

# from math import sqrt
#
#
# def solve(a, b, c):
#     d = b ** 2 - (4 * a * c)
#     if d > 0:
#         x1 = (-b + sqrt(d)) / (2 * a)
#         x2 = (-b - sqrt(d)) / (2 * a)
#         return min(x1, x2), max(x1, x2)
#
#     elif d == 0:
#         x1 = -b / (2 * a)
#         if x1 == 0:
#             return 0
#         else:
#             return x1,x1
#
#     else:
#         pass
#
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)


# def draw_triangle():
#     for i in range(8):
#         for j in range(i+2):
#             print('*',end='')
#         print()
#
# # основная программа
# draw_triangle()  # вызов функции


# def draw_triangle():
#     height = 8
#
#     for i in range(height):
#         # Print spaces before each line
#         for j in range(height - i):
#             print(" ", end="")
#
#         # Print stars for each line
#         for k in range(2 * i + 1):
#             print("*", sep='', end="")
#
#         # Go to next line
#         print()
#
#
# draw_triangle()
#
# def draw_triangle():
#     height = 8
#
#     for i in range(height):
#         # Print spaces before each line
#         for j in range(height - i):
#             print(" ", end="")
#
#         # Print stars for each line
#         for k in range(2 * i + 1):
#             print("*", sep='', end="")
#
#         # Go to next line
#         print()
#
#
# draw_triangle()

# def draw_triangle():
#     for i in range(8):
#         print(' '*(7-i)+'*'*(1+(i*2)))
#
# draw_triangle()


# def fak(n):
#     # if n == 0:
#     #     return 1
#     # else:
#     #     return n * fak(n - 1)
#
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     return factorial
#
# def compute_binom(n, k):
#     return int(fak(n)/(fak(k)*fak(n-k)))
#
#
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))

# def number_to_words(num):
#     # Создаем словарь с числами от 1 до 19
#     numbers = {
#         1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
#         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
#         11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
#         14: 'четырнадцать', 15: 'пятнадцать',
#         16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
#         19: 'девятнадцать'
#     }
#
#     # Создаем словарь с десятками
#     tens = {
#         2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
#         6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'
#     }
#
#     # Проверяем, является ли число однозначным
#     if num < 20:
#         return numbers[num]
#     elif num%10==0 and num!=10:
#         return tens[num//10]
#
#     else:
#         # Получаем десятки и единицы числа
#         ten_digit = num // 10
#         unit_digit = num % 10
#
#         # Возвращаем словесное описание числа
#         return f"{tens[ten_digit]} {numbers[unit_digit]}"
#
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))


# def get_month(language, number):
#     months = None
#     if language == 'ru':
#         months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#         'июль', 'август', 'сентябрь', 'октябрь',
#                   'ноябрь', 'декабрь']
#     elif language == 'en':
#         months = ['January', 'February', 'March', 'April', 'May', 'June',
#         'July', 'August', 'September', 'October',
#                   'November', 'December']
#     return months[number - 1].lower()
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))

# def is_magic(date):
#     day, month, year = date.split('.')
#     day = int(day)
#     month = int(month)
#     year = int(year)
#     return day * month == year % 100
#
# date = input()
#
# # вызываем функцию
# print(is_magic(date))


# def is_pangram(text):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     text = text.lower()
#     for letter in alphabet:
#         if letter not in text:
#             return False
#     return True

# from math import *
# from random import *
# name = input('Введи свое имя: ')
# p = int(input(f'{name} введи предел: '))
# u = randint(1, p)
#
# print(f'Добро пожаловать {name} в числовую угадайку!')
#
#
# def is_valid(argument):
#     try:
#         number = int(argument)
#         if 1 <= number <= p:
#             return True
#         else:
#             return False
#     except:
#         return False
#
#
# def ugaday(n):
#     if int(log(n, 2)) == log(n, 2):
#         n = int(log(n, 2))
#     else:
#         n = int(log(n, 2)) + 1
#     return n
#
#
# print(f'Максимально попыток по формуле log({p},2): ', ugaday(p))
# c = 1
# m = 1
# b = p
#
# while True:
#     num = input(f'{name} введи число от {m} до {b}: ')
#
#     if not is_valid(num):
#         print(f'{name}, а может быть все-таки введем целое число от {m} до
#         {b}?')
#         continue
#
#     num = int(num)
#
#     if num < u:
#         print(f'{name}, число меньше загаданного, введи число от {num} до
#         {b}')
#         c += 1
#         m = num
#         continue
#     elif num > u:
#         print(f'{name}, число больше загаданного, введи число от {m} до {
#         num}')
#         c += 1
#         b = num
#         continue
#     else:
#         print(f'{name} ты угадал c {c} попытки(ок) поздравляем!')
#         print(f'{name}, спасибо, что играл в числовую угадайку.')
#         i=input('Сыгрем еще раз? Напиши д (да) или н (нет): ')
#         if i.startswith('д'):
#             p = int(input(f'{name} введи предел: '))
#             u = randint(1, p)
#             print(f'Добро пожаловать {name} в числовую угадайку!')
#             print(f'Максимально попыток по формуле log({p},2): ', ugaday(p))
#             c = 1
#             m = 1
#             b = p
#             continue
#         else:
#             print(f'Досвидания {name}! Скажи ПАПЕ, что он МОЛОДЕЦ!')
#             break
#
# import random
#
# a = int(input('Укажите количество паролей для генерации: '))
# d = int(input('Укажите длину одного пароля: '))
#
#
# def parol(a, d):
#     digits = '0123456789'
#     digits_len = len(digits)
#     lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
#     lowercase_letters_len = len(lowercase_letters)
#     uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     uppercase_letters_len = len(uppercase_letters)
#     punctuation = '!#$%&*+-=?@^_'
#     punctuation_len = len(punctuation)
#     # вычисляем переменные в процентовке, т.е. сколько % в длине пароля
#     занимает группа цифр, букв, символов
#     sum_len = sum([digits_len, lowercase_letters_len,
#     uppercase_letters_len, punctuation_len])
#
#     pr_digits = digits_len * 100 / sum_len
#     pr_lowercase_letters = lowercase_letters_len * 100 / sum_len
#     pr_uppercase_letters = uppercase_letters_len * 100 / sum_len
#     pr_punctuation = punctuation_len * 100 / sum_len
#
#     print(int(pr_digits))
#     print(int(pr_uppercase_letters))
#     print(int(pr_lowercase_letters))
#     print(int(pr_punctuation))
#
#     parols = []
#     for i in range(a):
#         c = 0 # сумматор процентов к  включенной если группу не включать в
#         генерацию
#         chars = ''
#         digOn = input(f'Пароль №{i+1}\nВключать ли цифры 0123456789? (
#         y/n): ')
#         if digOn == 'y':
#             chars += ''.join(random.sample(digits, int(d * pr_digits /
#             100) + 1))
#             print(chars)
#         else:
#             c += pr_digits
#             print('****', c)
#         ABCon = input('Включать ли прописные буквы
#         ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
#         if ABCon == 'y':
#             chars += ''.join(random.sample(uppercase_letters, int(d * (
#             pr_uppercase_letters + c) / 100)))
#             print(chars)
#         else:
#             c += pr_uppercase_letters
#             print('****', c)
#         abcOn = input('Включать ли строчные буквы
#         abcdefghijklmnopqrstuvwxyz? (y/n): ')
#         if abcOn == 'y':
#             chars += ''.join(random.sample(lowercase_letters, int(d * (
#             pr_lowercase_letters + c) / 100)))
#             print(chars)
#         else:
#             c += pr_lowercase_letters
#             print('****', c)
#         chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
#         if chOn == 'y':
#             chars += ''.join(random.sample(punctuation, int(d * (
#             pr_punctuation + c) / 100) + 1))
#             print(chars)
#         else:
#             c += pr_punctuation
#             print('****', c)
#             print(chars)
#             print(len(chars))
#             print(int(int((d * c / 100) + 1) / len(chars)))
#             print(random.sample(digits, 3))
#             print(chars.join(random.sample(digits, 3)))
#             for k in chars:
#                 if k in digits:
#
#                     chars += ''.join(random.sample(digits, d - len(chars)))
#                 elif k in uppercase_letters:
#                     chars += ''.join(random.sample(uppercase_letters,
#                     d - len(chars)))
#                 elif k in lowercase_letters:
#                     chars += ''.join(random.sample(lowercase_letters,
#                     d - len(chars)))
#
#             print(chars)
#         excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ')
#         if excOn == 'y':
#             chars1 = ''
#             for j in chars:
#                 if j not in 'il1Lo0O':
#                     chars1 += j
#                 else:
#                     chars1 += 'x'
#             parols.append(chars1)
#         else:
#             parols.append(chars)
#
#         print(f'Ваши пароли: {parols}')
#
#
# parol(a, d)
#
# def r_caesar_decrypt(ciphertext, n):
#     plaintext = ""
#     for char in ciphertext:
#         # Проверяем, является ли символ буквой алфавита
#         if char.isalpha():
#             if char.isupper():
#                 plaintext += chr((ord(char) - ord('А') - n) % 32 + ord('А'))
#             else:
#                 plaintext += chr(
#                     (ord(char) - ord('а') - n) % 32 + ord('а'))
#         else:
#             # Если символ не является буквой алфавита,
#             # просто добавляем его к расшифрованному тексту без изменений
#             plaintext += char
#     return plaintext
#
# def caesar_decrypt(ciphertext, n):
#     plaintext = ""
#     for char in ciphertext:
#         # Проверяем, является ли символ буквой алфавита
#         if char.isalpha():
#             if char.isupper():
#                 plaintext += chr((ord(char) - ord('A') - n) % 26 + ord('A'))
#             else:
#                 plaintext += chr((ord(char) - ord('a') - n) % 26 + ord('a'))
#         else:
#             # Если символ не является буквой алфавита,
#             # просто добавляем его к расшифрованному тексту без изменений
#             plaintext += char
#     return plaintext
#
# def caesar_cipher(direction, language, shift):
#     if direction.startswith("д") or direction.startswith("d"):
#         shift = -shift  # Инвертируем сдвиг, чтобы использовать одну функцию
#         # для шифрования и дешифрования
#     alphabet = ""
#     if language == "russian":
#         alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
#     elif language == "english":
#         alphabet = "abcdefghijklmnopqrstuvwxyz"
#     text = input("Введите текст для обработки: ")
#     result = ""
#     for char in text:
#         if char.lower() in alphabet:  # Проверка, что символ содержится в
#             # алфавите
#             index = (alphabet.index(char.lower()) + shift) % len(alphabet)
#             if char.isupper():  # Проверка регистра символа
#                 result += alphabet[index].upper()
#             else:
#                 result += alphabet[index]
#         else:
#             result += char  # В случае, если символ не содержится в
#             # алфавите, оставляем его без изменений
#     print("Результат:", result)
#
# sdvig=input('Если не знаете сдвиг, нажмите - (н) или (n), иначе любой
# символ: ')
# if sdvig=='н' or sdvig=='n':
#     ciphertext = input('Вставьте зашифрованный текст: ')
#     if input('Русский? (да): ')=='да':
#         for shift in range(1, 32):
#             # Расшифровываем текст с заданным сдвигом и выводим результат
#             decrypted_text = r_caesar_decrypt(ciphertext, shift)
#             print(f"Сдвиг = {shift}: {decrypted_text}")
#     else:
#         # Перебираем все возможные сдвиги от 1 до 25
#         for shift in range(1, 26):
#             # Расшифровываем текст с заданным сдвигом и выводим результат
#             decrypted_text = caesar_decrypt(ciphertext, shift)
#             print(f"Сдвиг = {shift}: {decrypted_text}")
# else:
#
#     direction = input(
#         "Нажмите д, если дешифровать или любую другую если шифровать: ")
#     language = input("Выберите язык алфавита (russian/english): ")
#     shift = int(input("Введите шаг сдвига: "))
#     caesar_cipher(direction, language, shift)


# def caesar_decrypt(ciphertext, n):
#     plaintext = ""
#     text=ciphertext.split()
#     l_text=len(text)
#
#     for i in range(l_text):
#         n = len([i for i in text[i] if i.isalpha()])
#         plaintext += ' '
#         for char in text[i]:
#
#             # Проверяем, является ли символ буквой алфавита
#             if char.isalpha():
#                 if char.isupper():
#                     plaintext += chr((ord(char) - ord('A') + n) % 26 +
#                     ord('A'))
#                 else:
#                     plaintext += chr((ord(char) - ord('a') + n) % 26 +
#                     ord('a'))
#             else:
#                 # Если символ не является буквой алфавита,
#                 # просто добавляем его к расшифрованному тексту без изменений
#                 plaintext += char
#
#
#     return plaintext.strip()
#
# ciphertext = input()
#
#         # Расшифровываем текст с заданным сдвигом и выводим результат
# print(caesar_decrypt(ciphertext, len(ciphertext)))

# def from_to_10(num, n):
#     lst = list(num)
#     num16, a10, count = 'ABCDEF', 0, len(lst) - 1
#     for i, x in enumerate(lst):
#         if x in num16:
#             lst[i] = num16.index(x) + 10
#         a10 += int(lst[i]) * (n ** count)
#         count -= 1
#     return a10
#
#
# for j in range(1, 16):
#     a, b, c, d, e = from_to_10('32', j), from_to_10('22', j), from_to_10(
#     '16', j), from_to_10('17', j), from_to_10('88', j)
#     # для наглядности
#     print(f'{a} яблони, {b} груши, {c} слив и {d} вишен. Всешл деревьев: {
#     e}. Результат при n={j} : {a+b+c+d}')
#     # получаем результат
#     if e == a+b+c+d:
#         result = j
# print('*' * 10, f'Искомая n = {result}', '*' * 10,)


# def boh(n):
#     b=bin(n)
#     o=oct(n)
#     x=hex(n)
#     return b[2:],'\n',o[2:],'\n',x[2:].upper()
# print(*boh(int(input())),sep='')

# from random import *
# import openai
#
# openai.api_key = ''
# engine = "text-davinci-003"
#
# def ask(prompt):
#     completion = openai.Completion.create(engine=engine,
#                                           prompt=prompt,
#                                           temperature=0.5,
#                                           max_tokens=1000)
#
#     return completion.choices[0]['text']
#
# word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай',
#              'голова', 'ребенок', 'система',
#              'отношение', 'женщина', 'деньги', 'машина', 'проблема',
#              'решение',
#              'история', 'власть', 'тысяча',
#              'возможность', 'результат', 'область', 'статья', 'компания',
#              'группа', 'развитие', 'процесс', 'условие',
#              'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога',
#              'действие', 'государство', 'любовь',
#              'взгляд', 'общество', 'деятельность', 'организация',
#              'президент',
#              'комната', 'порядок', 'момент',
#              'письмо', 'помощь', 'ситуация', 'состояние', 'квартира',
#              'внимание', 'смерть', 'программа', 'задача',
#              'предприятие', 'разговор', 'правительство', 'производство',
#              'информация', 'положение', 'интерес',
#              'федерация', 'правило', 'управление', 'мужчина', 'партия',
#              'сердце', 'движение', 'материал', 'неделя',
#              'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура',
#              'данные', 'мнение', 'документ',
#              'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба',
#              'девушка', 'очередь', 'состав',
#              'количество', 'событие', 'объект', 'создание', 'значение',
#              'период', 'искусство', 'структура', 'пример',
#              'исследование', 'гражданин', 'начальник', 'принцип', 'воздух',
#              'характер', 'борьба', 'использование',
#              'размер', 'образование', 'мальчик', 'представитель', 'участие',
#              'девочка', 'политика', 'картина', 'доллар',
#              'территория', 'изменение', 'направление', 'рисунок', 'течение',
#              'церковь', 'население', 'большинство',
#              'музыка', 'правда', 'свобода', 'память', 'команда', 'договор',
#              'дерево', 'хозяин', 'природа', 'телефон',
#              'позиция', 'писатель', 'самолет', 'солнце', 'спектакль',
#              'способ',
#              'журнал', 'руководитель', 'специалист',
#              'оценка', 'регион', 'процент', 'родитель', 'требование',
#              'основание', 'половина', 'анализ', 'автомобиль',
#              'экономика', 'литература', 'бумага', 'степень', 'господин',
#              'надежда', 'предмет', 'вариант', 'министр',
#              'граница', 'модель', 'операция', 'название', 'старик',
#              'миллион',
#              'счастье', 'ребята', 'кабинет',
#              'магазин', 'пространство', 'знание', 'защита', 'руководство',
#              'площадь', 'сознание', 'возраст', 'участник',
#              'участок', 'желание', 'доктор', 'председатель', 'представление',
#              'солдат', 'художник', 'оружие',
#              'соответствие', 'парень', 'зрение', 'генерал', 'понятие',
#              'строительство', 'услуга', 'содержание',
#              'радость', 'безопасность', 'продукт', 'комплекс', 'бизнес',
#              'сотрудник', 'предложение', 'технология',
#              'реформа', 'отсутствие', 'собака', 'камень', 'будущее',
#              'рассказ',
#              'контроль', 'продукция', 'техника',
#              'здание', 'необходимость', 'подготовка', 'республика',
#              'хозяйство', 'бюджет', 'деревня', 'элемент',
#              'обстоятельство', 'победа', 'источник', 'звезда', 'сестра',
#              'практика', 'проведение', 'карман',
#              'определение', 'функция', 'войско', 'комиссия', 'применение',
#              'капитан', 'работник', 'обеспечение',
#              'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка',
#              'теория', 'разработка', 'личность',
#              'праздник', 'влияние', 'читатель', 'удовольствие',
#              'ответственность', 'учитель', 'множество',
#              'особенность', 'показатель', 'корабль', 'впечатление',
#              'частность', 'детство', 'профессор', 'прошлое',
#              'командир', 'коридор', 'поддержка', 'собрание', 'болезнь',
#              'клетка', 'заявление', 'попытка', 'сравнение',
#              'расчет', 'депутат', 'комитет', 'выражение', 'здоровье',
#              'десяток', 'глубина', 'студент', 'секунда',
#              'скорость', 'ошибка', 'режиссер', 'поверхность', 'ощущение',
#              'станция', 'революция', 'колено',
#              'министерство', 'стекло', 'высота', 'бабушка', 'трубка',
#              'мастер',
#              'поведение', 'столица', 'механизм',
#              'передача', 'способность', 'подход', 'энергия', 'существование',
#              'исполнение', 'сожаление', 'заместитель',
#              'ресурс', 'рождение', 'администрация', 'стоимость', 'улыбка',
#              'артист', 'фигура', 'субъект', 'реакция',
#              'список', 'фотография', 'журналист', 'нарушение', 'заседание',
#              'больница', 'существо', 'свойство',
#              'поколение', 'животное', 'усилие', 'отличие', 'остров',
#              'противник', 'реализация', 'страница',
#              'формирование', 'житель', 'красота', 'растение', 'явление',
#              'наличие', 'одежда', 'кресло', 'больной',
#              'университет', 'традиция', 'декабрь', 'ладонь', 'сведение',
#              'цветок', 'октябрь', 'занятие', 'сентябрь',
#              'помещение', 'январь', 'зритель', 'редакция', 'фактор',
#              'август',
#              'известие', 'зависимость', 'охрана',
#              'оборудование', 'концерт', 'отделение', 'расход', 'выставка',
#              'милиция', 'переход', 'произведение',
#              'родина', 'собственность', 'лагерь', 'имущество', 'кровать',
#              'аппарат', 'середина', 'клиент', 'отрасль',
#              'беседа', 'законодательство', 'продажа', 'повышение',
#              'полковник',
#              'сомнение', 'понимание', 'апрель',
#              'кодекс', 'настроение', 'должность', 'преступление', 'лестница',
#              'установка', 'появление', 'получение',
#              'образец', 'главное', 'костюм', 'ценность', 'обязанность',
#              'таблица', 'воспоминание', 'лошадь', 'коллега',
#              'организм', 'ученик', 'учреждение', 'открытие',
#              'характеристика',
#              'выполнение', 'оборона', 'выступление',
#              'температура', 'перспектива', 'подруга', 'приказ', 'жертва',
#              'ресторан', 'километр', 'признак',
#              'промышленность', 'американец', 'заключение', 'восток',
#              'исключение', 'постановление', 'перевод',
#              'секретарь', 'польза', 'звонок', 'обстановка', 'чиновник',
#              'соглашение', 'деталь', 'русский', 'тишина',
#              'зарплата', 'подарок', 'тюрьма', 'конкурс', 'книжка',
#              'изучение',
#              'просьба', 'публика', 'сообщение',
#              'угроза', 'достижение', 'назначение', 'реклама', 'портрет',
#              'стакан', 'творчество', 'телевизор',
#              'инструмент', 'концепция', 'лейтенант', 'реальность',
#              'знакомый',
#              'конфликт', 'переговоры', 'запись',
#              'площадка', 'последствие', 'сотрудничество', 'зеркало',
#              'академия', 'палата', 'потребность', 'ноябрь',
#              'увеличение', 'поездка', 'потеря', 'февраль', 'мероприятие',
#              'принятие', 'устройство', 'вещество',
#              'категория', 'гостиница', 'издание', 'объединение', 'темнота',
#              'человечество', 'колесо', 'опасность',
#              'разрешение', 'воздействие', 'коллектив', 'камера', 'следствие',
#              'кандидат', 'родственник', 'давление',
#              'присутствие', 'взаимодействие', 'партнер', 'двигатель',
#              'достоинство', 'страсть', 'испытание', 'оплата',
#              'разница', 'водитель', 'снижение', 'формула', 'капитал',
#              'новость', 'эффект', 'губернатор', 'доклад',
#              'убийство', 'эксперт', 'автобус', 'платье', 'общение',
#              'психология', 'проверка', 'процедура', 'рабочий',
#              'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник',
#              'корень', 'наблюдение', 'доказательство',
#              'признание', 'постель', 'владелец', 'компьютер', 'инженер',
#              'старуха', 'ракета', 'вершина', 'выпуск',
#              'торговля', 'молодежь', 'корпус', 'недостаток', 'сущность',
#              'талант', 'эффективность', 'полоса',
#              'основное', 'рассмотрение', 'следователь', 'описание',
#              'редактор',
#              'дворец', 'забота', 'столик',
#              'эксперимент', 'печать', 'кольцо', 'пистолет', 'воспитание',
#              'начальство', 'профессия', 'ворота', 'дружба',
#              'окончание', 'величина', 'записка', 'инициатива', 'совесть',
#              'активность', 'кредит', 'господь',
#              'конференция', 'потолок', 'библиотека', 'помощник',
#              'конструкция',
#              'металл', 'молоко', 'прокурор',
#              'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние',
#              'подразделение', 'сигнал', 'атмосфера',
#              'контакт', 'сигарета', 'восторг', 'золото', 'премия', 'король',
#              'подъезд', 'автомат', 'мальчишка',
#              'чтение', 'поселок', 'свидетель', 'ставка', 'удивление',
#              'поворот', 'возвращение', 'мгновение', 'статус',
#              'параметр', 'сказка', 'тенденция', 'дыхание', 'версия',
#              'масштаб',
#              'монастырь', 'хозяйка', 'эксплуатация',
#              'коммунист', 'пенсия', 'приятель', 'объяснение',
#              'производитель',
#              'философия', 'мощность', 'обязательство',
#              'кризис', 'указание', 'яблоко', 'препарат', 'действительность',
#              'москвич', 'остаток', 'изображение',
#              'сделка', 'сочинение', 'покупатель', 'затрата', 'строка',
#              'единица', 'обработка', 'чемпионат']
#
# def get_word():
#     s = word_list[randint(0, len(word_list))].upper()
#
#     return s
#
#
# get_word()
#
# # финальное состояние: голова, торс, обе руки, обе ноги
# def display_hangman(tries):
#     stages = [
#         '''
#            --------
#            |      |
#            |      O
#            |     ⎛▼⎞
#            |     ⎛ ⎞
#            |
#            -
#         ''',
#         # голова, торс, обе руки, одна нога
#         '''
#            --------
#            |      |
#            |      O
#            |     ⎛▼⎞
#            |     ⎛
#            |
#            -
#         ''',
#         # голова, торс, обе руки
#         '''
#            --------
#            |      |
#            |      O
#            |     ⎛▼⎞
#            |
#            |
#            -
#         ''',
#         # голова, торс и одна рука
#         '''
#            --------
#            |      |
#            |      O
#            |     ⎛▼
#            |
#            |
#            -
#         ''',
#         # голова и торс
#         '''
#            --------
#            |      |
#            |      O
#            |      ▼
#            |
#            |
#            -
#         ''',
#         # голова
#         '''
#            --------
#            |      |
#            |      O
#            |
#            |
#            |
#            -
#         ''',
#         # начальное состояние
#         '''
#            --------
#            |      |
#            |
#            |
#            |
#            |
#            -
#         '''
#     ]
#     return stages[tries]
#
# def play(word):
#     print(word[::-1])
#     word_completion = '_' * len(
#         word)  # строка, содержащая символы _ на каждую букву задуманного
#         слова
#
#     guessed = True  # сигнальная метка
#     guessed_letters = [i for i in word_completion]  # список уже названных
#     букв
#     guessed_words = []  # список уже названных слов
#     tries = 6  # количество попыток
#
#     print('Давайте играть в угадайку слов!')
#     print(display_hangman(tries),
#           f'\nСлово загадано из {len(word)} букв, '
#           f'{word_completion}\nКоличество допустимых промахов = 6')
#     opai = (f'Загадано это слово: {word} напиши какая это часть речи?, '
#             f'напиши короткую подсказку к этому слову, но не называй его!')
#     print(f'\nПодсказка: {ask(opai)}')
#     buk = input('Введи букву: ').upper()
#     while guessed:
#         if buk.isalpha():
#
#             if buk in word:
#                 for i in range(len(word)):
#
#                     if buk == word[i] and buk not in guessed_letters[i]:
#
#                         guessed_letters.pop(i)
#                         guessed_letters.insert(i, buk)
#
#                         if ''.join(guessed_letters).lower() == word.lower():
#                             print(f'Молодец! Ты разгадал слово {word}')
#                             guessed = False
#                             break
#                     if word.count(buk) > 1:
#                         for j in range(len(word[i:])):
#                             if buk == word[j] and buk not in guessed_letters[
#                                 j]:
#
#                                 guessed_letters.pop(j)
#                                 guessed_letters.insert(j, buk)
#                                 if (''.join(
#                                         guessed_letters).lower() ==
#                                         word.lower()):
#                                     print(f'Молодец! Ты разгадал слово {
#                                     word}')
#                                     i = input(
#                                         'Сыгрем еще раз? Напиши д (да) или
#                                         н '
#                                         '(нет): ')
#                                     if i.startswith('д'):
#                                         play(get_word())
#                                     else:
#                                         print(
#                                             'Досвидания! Скажи ПАПЕ, что он '
#                                             'МОЛОДЕЦ!')
#
#                                         guessed = False
#                                         break
#
#                 if guessed:
#                     print(display_hangman(tries),
#                           f'\nРазгадано {list(guessed_letters)}\nКоличество '
#                           f'допустимых промахов = {tries}')
#                     print(f'\nПодсказка: {ask(opai)}')
#                     buk = input('Введи букву: ').upper()
#             else:
#                 tries -= 1
#                 if tries == 0:
#                     guessed = False
#                     print(f'Ты не разгадал слово {word}')
#                     i = input(
#                         'Сыгрем еще раз? Напиши д (да) или н (нет): ')
#                     if i.startswith('д'):
#                         play(get_word())
#                     else:
#                         print('Досвидания! Скажи ПАПЕ, что он МОЛОДЕЦ!')
#
#                         guessed = False
#                         break
#                 print(display_hangman(tries),
#                       f'\nНЕУГАДАЛ {word_completion}\nКоличество допустимых '
#                       f'промахов = {tries}')
#                 print(f'\nПодсказка: {ask(opai)}')
#                 buk = input('Введи букву: ').upper()
#
#         else:
#
#             buk = input('Введи букву: ').upper()
#             6
#
# play(get_word())


# def easy(m=input()):
#    m=' '.join(m.split())
#    return m.count(' ')+1
# print(easy())


#
# year = int(input())
#
# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык",
# "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
# position = year % 12
#
# print(animals[position])

# def por(a=input()):
#     if len(a) == 6:
#         b = a[1:]
#         return int(a[0] + b[::-1])
#     else:
#         return int(a[::-1])
#
#
# print(por())


# res = 0
# for i in range(1, n + 1):
#     res = (res + k) % i
# print(res + 1)


# c=int(input())
#
# def chet(c):
#     c1=0
#     c2=0
#     c3=0
#     c4=0
#     for i in range(c):
#         t1=input().split()
#         if int(t1[0])>0 and int(t1[1])>0:
#             c1+=1
#         if int(t1[0])<0 and int(t1[1])>0:
#             c2+=1
#         if int(t1[0])<0 and int(t1[1])<0:
#             c3+=1
#         if int(t1[0])>0 and int(t1[1])<0:
#             c4+=1
#     return (f'Первая четверть: {c1}\nВторая четверть: {c2}\nТретья
#     четверть: '
#             f'{c3}\nЧетвертая четверть: {c4}\n')
#
#
# print(chet(c))


# string = input()
# numbers = list(map(int, string.split()))
# count = 0
#
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i-1]:
#         count += 1
#
# print(count)

# string = input()
# numbers = list(map(int, string.split()))
# count = 0

# def mest(nums):
#     for i in range(0, len(nums) - 1, 2):
#         print(i)
#         nums[i], nums[i + 1] = nums[i + 1], nums[i]
#
#     result = ' '.join(map(str,nums))
#     return result
# print(mest(numbers))

# # принимаем строку чисел
# numbers = input()
#
# # разделяем строку на отдельные числа и формируем список
# numbers_list = numbers.split()
#
# # сохраняем последний элемент списка
# last_number = numbers_list[-1]
#
# # сдвигаем все элементы списка вправо
# for i in range(len(numbers_list)-1, 0, -1):
#
#     numbers_list[i] = numbers_list[i-1]
#
# # первый элемент становится последним
# numbers_list[0] = last_number
#
# # выводим результат
# print(' '.join(numbers_list))

# numbers = input()
# number_list = numbers.split()
#
# count = 1
# for i in range(1, len(number_list)):
#     if number_list[i+5] != number_list[i-1]:
#         count += 1
#
# print(count)

# n = int(input())
# def is_product(n):
#     numbers=[]
#     for i in range(n):
#         num = int(input())
#         numbers.append(num)
#     target = int(input())
#
#     numbers.sort()  # сортировка списка чисел
#     left = 0  # указатель начала
#     right = len(numbers) - 1  # указатель конца
#
#     while left < right:
#         product = numbers[left] * numbers[right]
#         if product == target:
#             return "ДА"
#         elif product < target:
#             left += 1
#         else:
#             right -= 1
#
#     return "НЕТ"
#
#
# print(is_product(n))


# choice_timur = input()
# choice_ruslan = input()
#
# if choice_timur == choice_ruslan:
#     print("ничья")
# elif choice_timur == "камень" and choice_ruslan == "ножницы":
#     print("Тимур")
# elif choice_timur == "ножницы" and choice_ruslan == "бумага":
#     print("Тимур")
# elif choice_timur == "бумага" and choice_ruslan == "камень":
#     print("Тимур")
# else:
#     print("Руслан")


# choice_timur = input()
# choice_ruslan = input()
#
# if choice_timur == choice_ruslan:
#     print("ничья")
# elif (choice_timur == "камень" and (choice_ruslan == "ножницы" or
# choice_ruslan == "ящерица")) or (choice_timur == "ножницы" and (
# choice_ruslan == "бумага" or choice_ruslan == "ящерица")) or (choice_timur
# == "бумага" and (choice_ruslan == "камень" or choice_ruslan == "Спок")) or
# (choice_timur == "ящерица" and (choice_ruslan == "бумага" or choice_ruslan
# == "Спок")) or (choice_timur == "Спок" and (choice_ruslan == "камень" or
# choice_ruslan == "ножницы")):
#     print("Тимур")
# else:
#     print("Руслан")

# string = input("")
# def orresh(s):
#
#     max_count = 0
#     current_count = 0
#
#     for char in string:
#       if char == "Р":
#         current_count += 1
#       else:
#         max_count = max(current_count, max_count)
#         current_count = 0
#
#     max_count = max(current_count, max_count)
#     return max_count
#
# print(orresh(string))

# v = 'anton'
# c=[]
# for i in range(1, int(input()) + 1):
#     s, res = input(), ''
#     for j in v:
#         if j in s:
#             res += j
#             s = s[s.find(j):]
#
#     if res == 'anton':
#         c.append(i)
#         continue
#
# print(*c)

# s = input() + ' упрет букву'
#
# letters = set(s)
# for letter in sorted(letters):
#     if letter.isalpha():
#         print(f"{s.strip()}", letter)
#         s = s.replace(letter, '').replace('  ',' ')
#
#     letters = set(s)
#
# объявление функции

# n = int(input())
#
# lists = [[i for i in range(1, n+1)] for j in range(n)]
# for lst in lists:
#     print(lst)

# n = int(input())
#
# result = []
# for i in range(1, n+1):
#     sublist = []
#     for j in range(1, i+1):
#         sublist.append(j)
#     result.append(sublist)
#
# for sublist in result:
#     print(sublist)

# def pascal_triangle_row(n):
#     if n == 0:
#         return [1]
#     else:
#         previous_row = pascal_triangle_row(n-1)
#         row = [1]
#         for i in range(len(previous_row) - 1):
#             row.append(previous_row[i] + previous_row[i+1])
#         row.append(1)
#         return row


# Функция pascal_triangle_row(n) используется для создания
# строки треугольника Паскаля с указанным числом ряда
# def pascal_triangle_row(n):
#     # Создаем пустой список row, который будет представлять текущий ряд в
#     # треугольнике Паскаля. Начальным значением является список с одним
#     # элементом - 1
#     row = [1]
#     # Запускаем цикл, который будет выполняться n раз, чтобы создать нужное
#     # количество рядов
#     for _ in range(n):
#         # Внутри цикла создаем новый пустой список new_row, который будет
#         # представлять следующий ряд треугольника Паскаля
#         new_row = [1]
#         # Запускаем вложенный цикл, который будет проходить по всем
#         # элементам текущего ряда row, кроме последнего
#         for i in range(len(row) - 1):
#             new_row.append(row[i] + row[i + 1])
#         new_row.append(1)
#         row = new_row
#
#     return row
#
#
# n = int(input())
# for k in range(n):
#
#
#     print(*pascal_triangle_row(k))


# def pack_string(s):
#     packed_list = []
#     s=s.split()
#     current_char = None
#     count = 0
#     sub_list=[]
#
#     for char in s:
#         if char == current_char:
#             count += 1
#         else:
#             if current_char is not None:
#                 sub_list.extend([current_char]* count)
#                 packed_list.append(sub_list)
#             sub_list=[]
#             current_char = char
#             count = 1
#
#     packed_list.append([current_char]* count)
#
#     return packed_list
#
# s = input()
# result = pack_string(s)
# print(result)


# def chunked(lst, n):
#     l = lst.split()
#
#     new_lst = []
#
#     for i in range(0, len(l), n):
#         sub_lst = []
#         for j in range(i, min(i + n, len(l))):
#             sub_lst.append(l[j])
#         new_lst.append(sub_lst)
#
#     return new_lst
#
#
# lst = input()
# n = int(input())
# print(chunked(lst, n))


# def get_sublists(lst):
#     if not lst:  # если список пустой
#         return [[]]  # возвращаем список, содержащий только пустой список
#     sublists = get_sublists(
#         lst[1:])  # получаем все подсписки из оставшейся части списка
#     return [[lst[0]] + sublist for sublist in sublists] + sublists
#
# s = input()
# lst = s.split()
# sublists = get_sublists(lst)

# def get_sublists(word):  # [a, b, c, d]
#     sublists = [[]]
#     for length in range(1,
#                         len(word) + 1):  # все возможные длины списка - 1,
#                         2,3,4
#         for start in range(
#                 len(word) - length + 1):  # предел диапазона этого
#                 перебора покажет
#             # сколько подсписков с длиной первого перебора в начальном
#             списке [a, b, c, d]
#             sublist = word[start:start + length]
#             sublists.append(sublist)
#     # sublists.insert(0, [])
#     return sublists
#
#
# s = input()
# lst = s.split()
# print(get_sublists(lst))

# n = 8
# matrix = [[0]*n for _ in range(n)]
# print(matrix)# создаем квадратную матрицу размером 8×8
#
# for i in range(n):                    # заполняем главную диагональ
# единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
# print(matrix)
#
# for r in range(n):                    # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()

# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]), end=' ')
#         print()
#
# print(print_matrix([['yy']*9 for _ in range(9)],8))

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# print(matrix)

# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
#
# print(minimum + maximum)

# n = int(input())
# m = int(input())
#
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         element = input()
#         row.append(element)
#     matrix.append(row)
#
# for row in matrix:
#     print(' '.join(row))
#
# print()
# transposed_matrix = []
# for j in range(m):
#     transposed_row = []
#     for i in range(n):
#         transposed_row.append(matrix[i][j])
#     transposed_matrix.append(transposed_row)
#
# for row in transposed_matrix:
#     print(' '.join(row))

# n = int(input())
# matrix = []
# for i in range(n):
#     row = []
#     element = input().split()
#     matrix.append(element)
#
#
# transposed_matrix = []
# c=0
# for i in range(n):
#    c+=int(matrix[i][i])
#
# print(c)

# n = int(input())
# matrix = []
# for i in range(n):
#     row = []
#     element = input().split()
#     matrix.append(element)
#
# c1=[]
# for i in range(n):
#     c = 0
#
#     c2=0
#     for j in matrix[i]:
#         c+=int(j)
#
#     b=c/n
#
#     for k in matrix[i]:
#
#         if b<int(k):
#             c2+=1
#
#     c1.append(c2)
#
# print(*c1,sep='\n')

# n = int(input())
# matrix = []
# for i in range(n):
#     row = []
#     element = input().split()
#     matrix.append(element)
# c = float('-inf')
# u= float('-inf')
# for i in range(n):
#     for j in range(n):
#         if i >= j and i<=n-1-j:
#             if c < int(matrix[i][j]):
#                 c = int(matrix[i][j])
#         if i <= j and i>=n-1-j:
#             if u < int(matrix[i][j]):
#                 u = int(matrix[i][j])

# print(max(c,u))

# n = int(input())
# matrix = []
# for i in range(n):
#     row = []
#     element = map(int, input().split())
#     matrix.append(list(element))
# c = 0
# u = 0
# verh=0
# niz=0
# for i in range(n):
#     for j in range(n):
#         if i > j and i<n-1-j:
#
#             c +=matrix[i][j]
#         if  i < j and i>n-1-j:
#             u +=matrix[i][j]
#
#         if i < j and i<n-1-j:
#
#             verh +=matrix[i][j]
#         if  i > j and i>n-1-j:
#             niz +=matrix[i][j]
#
# print(f'Верхняя четверть: {verh}\nПравая четверть: {u}\nНижняя четверть: {niz}\nЛевая '
#       f'четверть: {c}')


# n = int(input())
# m = int(input())
#
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         element = i*j
#         row.append(str(element).ljust(2))
#     matrix.append(row)
#
# for row in matrix:
#     print(' '.join(row))


# n = int(input())
# m = int(input())
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
# c=0
# x=[]
# y=[]
# mx=[]
# for row in matrix:
#     row=[int(i) for i in row]
#     for i in range(len(row)):
#         if int(max(row))>0:
#             if max(row)==row[i]:
#                 x.append(i)
#                 mx.append(row[i])
#                 break
#         else:
#             if min(row)==row[i]:
#                 x.append(i)
#                 mx.append(row[i])
#                 break
#     y.append(c)
#     c += 1
#
# if int(max(row))>0:
#
#     ind_mx=mx.index(max(mx))
#     print(y[ind_mx],x[ind_mx])
# else:
#
#     ind_mx = mx.index(min(mx))
#     print(y[ind_mx], x[ind_mx])


# n = int(input())
# m = int(input())
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
# c=0
# x=[]
# y=[]
# mx=[]
# for row in matrix:
#     row=[int(i) for i in row]
#     for i in range(len(row)):
#
#         if max(row)==row[i]:
#             x.append(i)
#             mx.append(row[i])
#             break
#
#     y.append(c)
#     c += 1
#
# ind_mx=mx.index(max(mx))
# print(y[ind_mx],x[ind_mx])


# n = int(input())
# m = int(input())
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
# st = input().split()
# st=[int(i) for i in st]
#
#
#
# for i in range(n):
#     for j in range(m):
#         if st[0]==j:
#             # matrix[i] = [1, 2, 3, 4, 5]
#             temp = matrix[i][j]  # сохраняем значение первого элемента во временной переменной
#             matrix[i][j] = matrix[i][st[1]] # заменяем значение первого элемента значением
#             третьего элемента
#             matrix[i][st[1]] = temp  # заменяем значение третьего элемента сохраненным
#             значением первого элемента
#
#
# for row in matrix:
#     print(' '.join(row))#
# n = int(input())#
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
# c=1
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j]==matrix[j][i]:
#             pass#
#         else:
#             c=0#
# if c==1:
#     print('Yes')
# else:
#     print('NO')


# for row in matrix:
#     print(' '.join(row))


# n = int(input())
#
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
# c=1
# for i in range(n):
#     for j in range(n):
#
#         if i==j:
#             temp = matrix[i][i]  # сохраняем значение первого элемента во временной переменной
#             matrix[i][i] = matrix[n-i-1][n-1-(n-i-1)] # заменяем значение первого элемента
#             значением третьего элемента
#             matrix[n-i-1][n-1-(n-i-1)] = temp  # заменяем значение третьего элемента
#             сохраненным значением первого элемента
#
# for row in matrix:
#     print(' '.join(row))


# n = int(input())
#
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
#
# for row in matrix[::-1]:
#     print(' '.join(row))


# def rotate_matrix(matrix):
#     n = len(matrix)
#     rotated_matrix = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             rotated_matrix[i][j] = matrix[n - 1 - j][i]
#
#     return rotated_matrix
#
#
# n = int(input())
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
#
# rotated_matrix = rotate_matrix(matrix)
# for row in rotated_matrix:
#     print(' '.join(row))


# def knight_attack():
#     coordinates = input().strip()
#     col = ord(coordinates[0]) - ord('a')
#     row = 8 - int(coordinates[1])
#
#     board = [['.' for _ in range(8)] for _ in range(8)]
#
#     board[row][col] = 'N'
#     print(board)
#
#     for drow in (-2, -1, 1, 2):
#         for dcol in (-2, -1, 1, 2):
#             if abs(drow) != abs(
#                     dcol) and 0 <= row + drow < 8 and 0 <= col + dcol < 8:
#                 board[row + drow][col + dcol] = '*'
#
#     for row in board:
#         for cell in row:
#             print(cell, end=' ')
#         print()
#
#
# knight_attack()


# объявление функции knight_attack()
# def knight_attack():
#
# # вводим координаты коня и удаляем лишние пробелы
#     coordinates = input().strip()
#
# # вычисляем номер столбца, преобразовав символ в его номер в ASCII и вычитая номер символа 'a'
#     col = ord(coordinates[0]) - ord('a')
#
# # вычисляем номер строки, вычитая введенную цифру из числа 8
#     row = 8 - int(coordinates[1])
#
# # создаем пустую шахматную доску 8x8, заполненную точками
#     board = [['.' for _ in range(8)] for _ in  range(8)]
#
# # устанавливаем введенную координату коня на доске
#     board[row][col] = 'N'
#
# # перебираем все возможные смещения по строкам
#     for drow in (-2, -1, 1, 2):
#
#         # перебираем все возможные смещения по столбцам
#         for dcol in (-2, -1, 1, 2):
#
#             # проверяем, что смещение не является диагональным и новая позиция не выходит за
#             пределы доски
#             if abs(drow) != abs(dcol) and 0 <= row + drow < 8 and 0 <= col + dcol < 8:
#
#                 # устанавливаем на доске звездочки в местах, куда конь может сделать ход
#                 board[row + drow][col + dcol] = '*'
#
# # перебираем строки на доске
#     for row in board:
#         # перебираем ячейки в строке
#         for cell in row:
#             # выводим значение ячейки на экран, разделяя пробелами
#             print(cell, end=' ')
#         # выводим пустую строку для разделения строк на доске
#         print()
#
# # вызываем функцию knight_attack()
# knight_attack()

# n = int(input())
# matrix = []
# for i in range(n):
#     element = input().split()
#     matrix.append(element)
# k=1
# for w in matrix:
#     for element in w:
#         if int(element) == 0:
#             k=0
#
# vse = []
# dia = []
# pob = []
# row = []
# col = []
# for i in range(n):
#     row = []
#     col = []
#     for j in range(n):
#         row.append(int(matrix[j][i]))
#         col.append(int(matrix[i][n - 1 - j]))
#         if j == i:
#             dia.append(int(matrix[i][i]))
#         if j == n - i - 1:
#             pob.append(int(matrix[i][j]))
#
# vse.append(sum(col))
# vse.append(sum(row))
# vse.append(sum(dia))
# vse.append(sum(pob))
#
#
# if sum(vse) / 4 == sum(set(col))==sum(set(row))==sum(set(dia))==sum(set(pob)) and k!=0:
#     print('YES')
# else:
#     print('NO')

# def is_magic_square(n, matrix):
#     # создаем список для всех чисел правильной матрицы
#     correct_nums = list(range(1, n ** 2 + 1))
#
#     # создаем список для всех чисел нашей матрицы
#     our_nums = []
#     for row in matrix:
#         our_nums.extend(row)
#
#     # если эти списки не равны, значит наша матрица уже не состоит из всех чисел от 1 до n ** 2
#     # значит, мы сразу можем вернуть "NO" и не продолжать дальнейшие проверки
#     if sorted(our_nums) != correct_nums:
#         return "NO"
#
#     # в самой матрице мы уже храним все ряды (строки)
#     rows = matrix.copy()
#
#     # создаем список для всех столбцов
#     columns = []
#     for j in range(n):
#         cur_column = []
#         for i in range(n):
#             cur_column.append(matrix[i][j])
#
#         columns.append(cur_column)
#
#     # создаем список для диагоналей (с двумя пустыми подсписками)
#     diagonals = [[], []]
#     for i in range(n):
#         diagonals[0].append(matrix[i][i])
#         diagonals[1].append(matrix[i][n - 1 - i])
#
#     # соединям все строки, столбцы и диагонали в один список
#     all_lines = rows + columns + diagonals
#
#     # инициализируем переменные для максимальной и минимальной суммы среди всех "линий"
#     # за начальные значения возьмём сумму первой "линии"
#     max_sum = sum(all_lines[0])
#     min_sum = sum(all_lines[0])
#     for line in all_lines:
#         max_sum = max(max_sum, sum(line))
#         min_sum = min(min_sum, sum(line))
#
#     # теперь просто сравниваем максимальную и минимальную суммы
#     # они должны быть равны, т.к. все суммы должны быть равны
#     if max_sum != min_sum:
#         return "NO"
#
#     return "YES"
#
#
# n = int(input())
# matrix = [[int(el) for el in input().split()] for _ in range(n)]
#
# print(is_magic_square(n, matrix))

# n = int(input())
# m = int(input())
# # matrix = [['.' for _ in range(m)] for _ in  range(n)]
# # print(matrix)
# # for i in range(n):
# #     for j in range(m):
# #         if i%2!=0 and j%2==0:
# #             matrix[i][j]='*'
# #         elif i%2==0 and j%2!=0:
# #             matrix[i][j] = '*'
# # print(matrix)
# # for row in matrix:
# #         for cell in row:
# #             print(cell, end=' ')
# #         print()

# rows, cols = map(int, input().split())
# matrix1 = [['*' if i%2!=0 and j%2==0 else '*' if i%2==0 and j%2!=0 else '.' for j in range(cols)] for i in range(rows)]
#
# for row in matrix1:
#         for cell in row:
#             print(cell, end=' ')
#         print()
#
# import time
#
# # начальное время
#
#
# rows, cols = map(int, input().split())
# start_time = time.time()
#
# matrix1 = [['*' if (i + j) % 2 != 0 else '.' for j in range(cols)] for i in range(rows)]
# for row in matrix1:
#     print(' '.join(row))
# time.sleep(3)
# # конечное время
# end_time = time.time()
#
# # разница между конечным и начальным временем
# elapsed_time = end_time - start_time
# print('Время: ', elapsed_time)
# import time
# начальное время
#
#
# n, m = map(int, input().split())
# start_time = time.time()
#
#
# board = [['.' if (i + j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]
#
# for row in board:
#     print(*row)
# time.sleep(3)
# # конечное время
# end_time = time.time()
#
# # разница между конечным и начальным временем
# elapsed_time = end_time - start_time
# print('Время: ', elapsed_time)

# stepic
# n, m = [int(i) for i in input().split()]
# board = [['.'] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(1 - i % 2, m, 2):
#         board[i][j] = '*'
#
# for row in board:
#     print(*row)


# n = int(input())
# # matrix = [['0' for j in range(n)] for i in range(n)]
# # for i in range(n):
# #     for j in range(n):
# #         if j==n-i-1:
# #             matrix[i][j] = '1'
# #         elif j>=i and i>n-1-j:
# #             matrix[i][j] = '2'
# #         elif j<=i and i>n-1-j:
# #             matrix[i][j] = '2'
#
# matrix = [['1' if j == n - i - 1 else '2' if j >= i and i > n - 1 - j else '2' if j <= i and i > n - 1 - j else '0'
#               for j in range(n)] for i in range(n)]
# for row in matrix:
#     print(*row)

# n, m = map(int, input().split())
#
# matrix = [[k for k in range(1,m*n+1)] for i in range(n)]
# for row in matrix:
# print(*row)

#
# n, m = map(int, input().split())
# matrix = [[(i + j) % m + 1 for j in range(m)] for i in range(n)]
# for row in matrix:
#     print(*row)
# # ******** ДИАГОНАЛИ ************
# matrix = [['1' if j == n - i - 1 else '0' if j == i else '.' for j in range(m)] for i in range(n)]
# # for row in matrix:
# #     for value in row:
# #         print(value, end=" ")
# #     print()
# # print(999)
# for row in matrix:
#     print(*row)
# # ****** МАТРИЦА от 1 до n ***********
# matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]
# for row in matrix:
#     for value in row:
#         print(str(value).ljust(3), end=" ")
#     print()
# # ****** МАТРИЦА от 1 до n ***********
# matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]
# for row in matrix:
#     for value in row:
#         print(str(value).ljust(3), end=" ")
#     print()
# # ****** ВЕРХ/НИЗ ЧЕТВЕРТИ ***********
# matrix = [[1 if k<=i and k >=n-1-i else 1 if k>=i and k <=n-1-i else 0 for k in range(n)] for i in range(n)]
# for row in matrix:
#     aligned_row = ' '.join([str(element).ljust(3) for element in row])
#     print(aligned_row)
# # ****** ВОЗРАСТАНИЕ ВОЛНОЙ ОТ НАЧАЛА ГЛАВНОЙ ДИАГОНГАЛИ ***********
# matrix = [[(j + i) % m + 1 for j in range(m)] for i in range(n)]
# for item in matrix:
#     print(*[str(it).ljust(3) for it in item])
# # ****** 0 ДО ПОБОЧНОЙ ДИАГОНГАЛИ - 1 и 2 ПОСЛЕ ***********
# matrix = [['1' if j == n - i - 1 else '2' if j >= i and i > n - 1 - j else '2' if j <= i and i > n - 1 - j else '0'
#               for j in range(n)] for i in range(n)]
# for row in matrix:
#     print(*row)
# # ****** ЗМЕЙКА ***********
# matrix = [[i * m + j + 1 if i%2 == 0 else (i+1) * m - j for j in range(m)] for i in range(n)]
# for row in matrix:
#     for value in row:
#         print(str(value).ljust(3), end=" ")
#     print()
# ****** ЧИСЛА ПО ДИАГОНАЛИ ***********
# n, m = map(int, input().split())
# mtx = [[0] * m for _ in range(n)]
# sequence, k = 1, 0
# while sequence != n * m + 1:
#     for i in range(n):
#         for j in range(m):
#             if i + j == k:
#                 mtx[i][j] = sequence
#                 sequence += 1
#     k += 1
# for i in range(n):
#     for j in range(m):
#         print(str(mtx[i][j]).ljust(3), end='')
#     print()

# n, m = [int(el) for el in input().split()]
# matrix = [[None for _ in range(m)] for _ in range(n)]
# cnt = 1
# # проходим по всем диагоналям
# for d in range(n + m - 1):
#     for i in range(n):
#         for j in range(m):
#             if i + j == d:
#                 matrix[i][j] = cnt
#                 cnt += 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end="")
#     print()


#
# def create_spiral_matrix(n, m):
#     # Создаем матрицу размером n x m
#     matrix = [[0] * m for _ in range(n)]
#
#     # Определяем границы для заполнения матрицы
#     top = 0
#     bottom = n - 1
#     left = 0
#     right = m - 1
#
#     # Значение, которое будет установлено в матрицу
#     value = 1
#
#     while top <= bottom and left <= right:
#         # Заполняем верхнюю границу
#         for i in range(left, right + 1):
#             matrix[top][i] = value
#             value += 1
#         top += 1
#
#         # Заполняем правую границу
#         for i in range(top, bottom + 1):
#             matrix[i][right] = value
#             value += 1
#         right -= 1
#
#         # Заполняем нижнюю границу (если есть)
#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 matrix[bottom][i] = value
#                 value += 1
#             bottom -= 1
#
#         # Заполняем левую границу (если есть)
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 matrix[i][left] = value
#                 value += 1
#             left += 1
#
#     return matrix
#
# # Считываем значения n и m
# n, m = map(int, input().split())
#
# # Создаем и выводим на экран "спиральную" матрицу
# matrix = create_spiral_matrix(n, m)
# for row in matrix:
#     print(*row)


# n, m = map(int, input().split())
#
# matrix1 = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix1.append(row)
#
# input()
#
# matrix2 = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix2.append(row)
#
# result = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         element = matrix1[i][j] + matrix2[i][j]
#         row.append(element)
#     result.append(row)
#
# for row in result:
#     print(*row)

# n1, m1 = map(int, input().split())  # количество строк и столбцов в первой матрице
# matrix1 = []
# for _ in range(n1):
#     row = list(map(int, input().split()))  # элементы первой матрицы
#     matrix1.append(row)
# input()  # пустая строка
#
# m2, k2 = map(int, input().split())  # количество строк и столбцов второй матрицы
# matrix2 = []
# for _ in range(m2):
#     row = list(map(int, input().split()))  # элементы второй матрицы
#     matrix2.append(row)
#
# # проверяем возможность умножения матриц
# if m1 != m2:
#     print('Умножение невозможно')
# else:
#     # создаем результирующую матрицу
#     result = []
#     for i in range(n1):
#         row = []
#         for j in range(k2):
#             element = 0
#             for x in range(m1):
#                 element += matrix1[i][x] * matrix2[x][j]
#             row.append(element)
#         result.append(row)
#
#     # выводим результирующую матрицу
#     for row in result:
#         print(*row)

# n = int(input())
# matrixA = [[int(i) for i in input().split()] for _ in range(n)]
#
# x = int(input())
# matrixB = matrixA
#
# for _ in range(x-1):
#     matrixC = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for q in range(n):
#                 matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
#     matrixA=matrixC
#
# for row in matrixC:
#     print(*row)

# считываем строку и число n


# s = input().split()
# n = int(input())
#
# nested_list = []
# for i in range(n):
#     nested_list.append(s[i::n])
#
# print(nested_list)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# m1=[]
# for i in range(n):
#     for j in range(n):
#         if i+j+1>=n:
#             m1.append(matrix[i][j])
# print(max(m1))

# n = int(input())
# matrix = []
#
# # считываем матрицу
# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# # транспонируем матрицу
# for i in range(n):
#     for j in range(i+1, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# # выводим транспонированную матрицу
# for row in matrix:
#     print(*row)


# ******* СНЕЖИНКА *********
# n = int(input())
#
# matrix = [['.']*n for _ in range(n)]
# middle = n // 2
#
# for i in range(n):
#     matrix[middle-1][i] = '*'
#     matrix[i][middle] = '*'
#     matrix[i][i] = '*'
#     matrix[i][n-1-i] = '*'
#
# for row in matrix:
#     print(*row)
# ************* СИММЕТРИЯ МАТРИЦЫ **************
# n = int(input())
# matrix = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# is_symmetric = True
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[n-1-j][n-1-i]:
#             is_symmetric = False
#             break
#
# if is_symmetric:
#     print("YES")
# else:
#     print("NO")
# ************* ЛАТИНСКИЙ КВАДРАТ ***********
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     if sorted(matrix[i]) != list(range(1, n + 1)) or sorted([matrix[j][i] for j in range(n)]) != list(range(1, n + 1)):
#         print('NO')
#         break
# else:
#     print('YES')

# ********** ХОД ФЕРЗЕМ ************
# x, y = input()
# n = 8
# matrix = [["."] * n for _ in range(n)]
# y = n - int(y)
# x = ord(x) - 97
#
# for i in range(n):
#     for q in range(n):
#         if i == y or q == x:
#             matrix[i][q] = "*"
#         elif (i + q == y +x) or (i - q == y -x):
#             matrix[i][q] = "*"
#
# matrix[y][x] = "Q"
# for x in range(n):
#     print()
#     for y in range(n):
#         print(matrix[x][y], end = " ")

# n = int(input())
# matrix = [[abs(i-j) for j in range(n)] for i in range(n)]
# for row in matrix:
#     print(*row)
# print()
# matrix = [[abs(j-i+2) for j in range(n)] for i in range(n)]
# for row in matrix:
#     print(*row)

# n = int(input())
# students = []
# excellent = []
# good = []
#
# for _ in range(n):
#     name, grade = input().split()
#     students.append((name, int(grade)))
# for name, grade in students:
#     print(name, grade)
# for name, grade in students:
#     if grade >3:
#         excellent.append((name, grade))
# print()
# for name, grade in excellent:
#     print(name, grade)

# n = int(input())
# tribonacci = [1, 1, 1]
# if n==1:
#     print(1)
# elif n==2:
#     print(1,1)
# else:
#     for i in range(3, n):
#         tribonacci.append(tribonacci[i - 3] + tribonacci[i - 2] + tribonacci[i - 1])
#
#     print(*tribonacci)

# ********** ТРИБОНАЧИ **************
# n = int(input())
# t1 = t2 = t3 = 1
# for _ in range(n):
#     print(t1, end=' ')
#     t1, t2, t3 = t2, t3, t1 + t2 + t3

# n, m, k, x, y, z = (int(input()) for i in range(6))
# vseh=(k-y)+(m-x-y)+(n-x)+y+x+z
# print(vseh)

# n, m, k, x, y, z, t, a = (int(input()) for i in range(8))
# s1=n+m-x-t
# s2=m+k-y-t
# s3=k+n-z-t
#
# odna=(k-s3-s2-t)+(m-s1-s2-t)+(n-s1-s3-t)
# dve=s1+s2+s3
# vseh=a-((k-s3-s2-t)+(m-s1-s2-t)+(n-s1-s3-t)+s1+s2+s3+t)
# print(odna,dve,vseh,sep='\n')


# n = int(input())
# numbers = []
# for _ in range(n):
#     numbers.append(set(input()))
# common_digits = set.intersection(*numbers)
# sorted_digits = sorted(common_digits)
#
# print(*sorted(common_digits))

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
#
# print(*sorted(((set1 & set2) - set3), reverse=True))

# grades1 = set(input().split())
# grades2 = set(input().split())
# grades3 = set(input().split())
# all_grades = grades1 | grades2 | grades3
# result = set()
# for grade in all_grades:
#     count = 0
#     if grade in grades1:
#         count += 1
#     if grade in grades2:
#         count += 1
#     if grade in grades3:
#         count += 1
#     # Если оценка встречается не более, чем у двух учеников, добавляем ее в результирующее множество
#     if count <= 2:
#         result.add(grade)
#
# print(*sorted(result))

# grades1, grades2, grades3 = set(map(int,input().split())),set(map(int,input().split())),set(map(int,input().split()))
# result = set()
# for grade in grades1.union(grades2, grades3):
#     count = sum(1 for grades in [grades1, grades2, grades3] if grade in grades)
#     if count <= 2:
#         result.add(grade)
# print(*sorted(result))

# grades1, grades2, grades3 = set(map(int,input().split())),set(map(int,input().split())),set(map(int,input().split()))
# result = set()
#
# all_grades = grades1 | grades2 | grades3
# result = set()
# for grade in all_grades:
#     count = 0
#     if grade not in grades1:
#         count += 1
#     if grade not in grades2:
#         count += 1
#     if grade in grades3:
#         count += 1
#     # Если оценка встречается не более, чем у двух учеников, добавляем ее в результирующее множество
#     if count == 3:
#         result.add(grade)
#
# print(*sorted(result, reverse=True))


# grades1, grades2, grades3 = set(map(int,input().split())),set(map(int,input().split())),set(map(int,input().split()))
# result = set()
#
# all_grades = set(range(11))
# result = set()
# for grade in all_grades:
#     count = 0
#     if grade not in grades1:
#         count += 1
#     if grade not in grades2:
#         count += 1
#     if grade not in grades3:
#         count += 1
#     # Если оценка встречается не более, чем у двух учеников, добавляем ее в результирующее множество
#     if count == 3:
#         result.add(grade)
#
# print(*sorted(result))

# sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'
#
# words = sentence.lower().replace('.', '').replace(',', '').split()
#
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}
#
# print(*consonants, sep='\n')

# m,n = int(input()),int(input())
# c=[]
# c2=[]
# for i in range(m):
#     c.append(input())
# for i in range(n):
#     c2.append(input())
#
# for j in c2:
#     if j in c:
#         print('YES')
#
#     else:
#         print('NO')


# m, n =set(map(int,input().split())),set(map(int,input().split()))
# h=set(m) & set(n)
# if len(h)==len(m) and len(h)==len(n):
#     print('YES')
# else:
#     print('NO')

# m, n =int(input()),int(input())
# s1=set()
# s2=set()
# for i in range(m):
#     s1.add(input())
# for i in range(n):
#     s2.add(input())
#
# if len(s1 ^ s2):
#     print(len(s1 ^ s2))
# else:
#     print('NO')


# m, n =set(input().split()),set(input().split())
# h=m | n
# print(*sorted(h))

# m, n =int(input()),int(input())
# s1=[]
#
# for i in range(m+n):
#     s1.append(input())
# if m+n-(len(s1)-len(set(s1)))*2==0:
#     print('NO')
# else:
#     print(m+n-(len(s1)-len(set(s1)))*2)


# m = int(input())
#
# students = set()
# for _ in range(m):
#     ni = int(input())
#     lesson_students = set()
#     for _ in range(ni):
#         student = input()
#         lesson_students.add(student)
#     if len(students) == 0:
#         students = lesson_students
#     else:
#         students = students.intersection(lesson_students)
#
# sorted_students = sorted(students)
#
# for student in sorted_students:
#     print(student)

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'}]
# # names = []
# # for i in users:
# #     if i['phone'][-1] == '8':
# #         names.append(i['name'])
# #
# # names.sort()
# #
# # for name in names:
# #     print(name, end=' ')
#
# result = [user['name'] for user in users if user['phone'].endswith('8')]
#
# print(*sorted(result))


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'}]
# result = [user['name'] for user in users if ('email' in user and user['email']=='') or not 'email' in user]
#
# print(*sorted(result))

# d={
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
# n=[i for i in input()]
#
# for j in n:
#     for i in d:
#         if j==i:
#             print(d[j],end=' ')

# courses = {'CS101': ['3004', 'Хайнс', '8:00'],
#            'CS102': ['4501', 'Альварадо', '9:00'],
#            'CS103': ['6755', 'Рич', '10:00'],
#            'NT110': ['1244', 'Берк', '11:00'],
#            'CM241': ['1411', 'Ли', '13:00']}
#
# n=input()
# print(f'{n}: {courses[n][0]}, {courses[n][1]}, {courses[n][2]}')

# d = {
#     ".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#     "a": '2', "b": '22', "c": '222',
#     "d": '3', "e": '33', "f": '333',
#     "g": '4', "h": '44', "i": '444',
#     "j": '5', "k": '55', "l": '555',
#     "m": '6', "n": '66', "o": '666',
#     "p": '7', "q": '77', "r": '777', "s": '7777',
#     "t": '8', "u": '88', "v": '888',
#     "w": '9', "x": '99', "y": '999', "z": '9999',
#     " ": '0'
# }
# # n=input().lower()
# # for i in n:
# #
# #     for j in d:
# #         if i==j:
# #             print(d[j], end='')
#
# n = input().lower()
# output = [d[j] for i in n for j in d if i == j]
# print(''.join(output))

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# d=dict(zip(letters,morse))
# n = input().upper()
# output = [d[j] for i in n for j in d if i == j]
# print(' '.join(output))

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
#
# print(result, len(set(result)))
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# result = {}
#
# for num in numbers:
#     count = numbers.count(num)
#     if count > 1:  # Проверяем, что элемент повторяется
#         result[num] = count
#
# print(result)

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
#
# какой код асимптотически лучше?
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# result = {}
#
# for num in numbers:
#     count = numbers.count(num)
#     if count > 1:  # Проверяем, что элемент повторяется
#         result[num] = count
#
# print(result)
# Второй код асимптотически лучше, поскольку он имеет временную сложность O (n), тогда как первый код имеет временную сложность O (n ^ 2), потому что он использует оператор "not in" внутри цикла for, который имеет сложность O (n).


# info = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev', 'salary':'888'}
#
# item1 = info.get('salary')
# item2 = info.get('salary', 'Информации о зарплате нет')
#
# print(info)
# print(item2)


# result = {}
# for i in range(1,16):
#     result.setdefault(i,i ** 2)
# print(result)
#
# result = {i: i ** 2 for i in range(1, 16)}
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
#
# for key in dict1:
#     if key in dict2:
#         result[key] = dict1[key] + dict2[key]
#     else:
#         result[key] = dict1[key]
#
# for key in dict2:
#     if key not in dict1:
#         result[key] = dict2[key]

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
#
# for num in text:
#     count = text.count(num)
#     if count > 0:
#         result[num] = count
# print(result)
#
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# word_list = s.split()
# word_count = {}
# for word in word_list:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# max_count = max(word_count.values())
# print(max_count)
# most_frequent_words = [word for word, count in word_count.items() if count == max_count]
# print(most_frequent_words)
#
# most_frequent_words.sort()
# print(most_frequent_words[0])
#
# 12
# ['barley', 'banana']
# banana

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# # result = {}
# # for pet in pets:
# #     owner = (pet[1], pet[2], pet[3])
# #     if owner not in result:
# #         result[owner] = [pet[0]]
# #     else:
# #         result[owner].append(pet[0])
#
# result = {}
# for pet in pets:
#     result.setdefault(pet[1:], []).append(pet[0])

# s = input().lower()
# words = [element for element in s if element.isalnum() or element.isspace()]
# words = "".join(words).split()
# word_count = {}
# for word in words:
#     if word.isalpha():
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
# min_count = min(word_count.values())
# min_words = [word for word, count in word_count.items() if count == min_count]
#
# min_word = sorted(min_words)
#
# print(*min_word[0],sep='')

# s = input().split()
#
# result = []
# count = {}
#
# for i in s:
#     if i in count:
#         count[i] += 1
#         result.append(i + "_" + str(count[i]))
#     else:
#         count[i] = 0
#         result.append(i)
#
# print(" ".join(result))

# lst = input().split()
# res = {}
# for c in lst:
#     if c in res:
#         print(f'{c}_{res[c]}', end=' ')
#     else:
#         print(c, end=' ')
#     res[c] = res.get(c, 0) + 1

# n = int(input())
# d={}
# for _ in range(n):
#     s=input().split(': ')
#     d[s[0].lower()]=s[1]
# m = int(input())
# l=[]
# for _ in range(m):
#     key=input().lower()
#     l.append(d.get(key,'Не найдено'))
# print(*l,sep='\n')

# s=sorted(input())
# s1=sorted(input())
# d=dict(zip(range(len(s)),s))
# d1=dict(zip(range(len(s1)),s1))
#
# if d==d1:
#     print('YES')
# else:
#     print('NO')

# s=''.join(sorted([i.lower() for i in input() if i.isalpha()]))
# s1=''.join(sorted([i.lower() for i in input() if i.isalpha()]))
# if s==s1:
#     print('YES')
# else:
#     print('NO')
# d=dict(zip(range(len(s)),s))
# d1=dict(zip(range(len(s1)),s1))
#
# if d==d1:
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# synonyms = {}
# for _ in range(n):
#     word1, word2 = input().split()
#     synonyms[word1] = word2
#     synonyms[word2] = word1
#
# word = input()
# print(synonyms[word])


# n = int(input())
# cities = {}
# for _ in range(n):
#     line = input().split()
#     country = line[0]
#     cities_list = line[1:]
#     for city in cities_list:
#         cities[city] = country
# m = int(input())
# p=[]
#
# for _ in range(m):
#     query = input()
#     country = cities.get(query)
#     p.append(country)
# print(*p,sep='\n')


# n = int(input()) # количество номеров телефонов
# d = {} # словарь для хранения номеров телефонов
# for _ in range(n):
#     phone, name = input().lower().split()
#     d[name]=d.get(name,'')+' '+phone
# p=[]
# for _ in range(int(input())):
#     n1=input().lower()
#     p.append(d.get(n1,'абонент не найден').strip())
# print(*p,sep='\n')

# s=input()
# my={}
# for _ in range(int(input())):
#     v,k=input().split(': ')
#     my[int(k)]=v
# for j in s:
#     print(my[s.count(j)],end='')

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i:numbers[i]**2 for i in range(len(numbers))}
# print(result)

# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {j:i for i,j in months.items()}
# print(result)

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'.split()
# print(s)
# result = {n.split(':')[0]:n.split(':')[1] for n in s}
# print(result)

# def d(x):
#     k=[]
#     for i in range(1,x+1):
#         if x%i==0:
#             k.append(i)
#     return sorted(k)
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {i: d(i) for i in numbers}
# print(result)

# def d(x):
#     k=[]
#     for i in x:
#         k.append(ord(i))
#     return k
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {i: d(i) for i in words}
# print(result)
#
# result = {word: [ord(letter) for letter in word] for word in words}

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {i:j for i,j in letters.items() if i not in remove_keys}
# print(result)

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {i:j for i,j in students.items() if j[0]>167 and j[1]<75}
# print(result)


# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {i[0]:i[1:] for i in tuples}
# print(result)


# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{student_id: {student_name: student_grade}} for student_id, student_name, student_grade in zip(student_ids, student_names, student_grades)]
#
# print(*zip(student_ids, student_names, student_grades),sep='\n')


# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#
# # for key in my_dict:
# #
# #     my_dict[key] = [x for x in my_dict[key] if x <= 20]
# my_new_dict = {key: [x for x in my_dict[key] if x <= 20] for key in my_dict}
# print(my_dict)
# print(my_new_dict)

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# l=[]
# for domain, usernames in emails.items():
#     for username in usernames:
#         l.append(f"{username}@{domain}")
# print(*sorted(l),sep='\n')

# s=input()
#
# # d={'G':'C','C':'G','T':'A','A':'U'}
# # for i in s:
# #     print(d[i],end='')
# #
# # s=input()
#
# d={'G':'C','C':'G','T':'A','A':'U'}
# print(''.join([d[i] for i in s]), end='')

# s=input().split()
# r={}
# for i in s:
#     r[i]=r.get(i,0)+1
#     print(r[i],end=' ')

# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# s=input()
# r=[i for l in s for i,j in d.items() if l in j]
# print(sum(r))

# def build_query_string(params):
#     return '&'.join([f'{i}={j}' for i,j in sorted(params.items())])
# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
#
# def merge(values):      # values - это список словарей
#     r={}
#     for i in values:
#         for j in i:
#             r.setdefault(j,set()).add(i[j])
#     return r
# print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))

# r={}
# d={'W':'write','R':'read','X':'execute'}
# for _ in  range(int(input())):
#     x=input().split()
#     r[x[0]]=[d[i] for i in x[1:]]
#
# for _ in range(int(input())):
#     x = input().split()
#     if x[0] in r[x[1]]:
#         print('OK')
#     else:
#         print('Access denied')

# r={}
#
# for _ in  range(int(input())):
#     n,p,c=input().split()
#     r.setdefault(n,{})
#     r[n][p]=r[n].get(p,0)+int(c)
#
# for i,j in sorted(r.items()):
#     print(f'{i}:')
#     for k in sorted(j):
#         print(k,j[k])

# import random
# def generate_ip():
#     n = random.choice(range(256))
#     n2 = random.choice(range(256))
#     n3 = random.choice(range(256))
#     n1=random.choice(range(10))
#     for _ in range(4):
#         return f'{n}.{n2}.{n1}.{n3}'
# print(generate_ip())
# from random import randrange as r
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'

from random import randrange as r, sample as s
from string import ascii_uppercase as ss

# from random import randrange as r, sample as s
# from string import ascii_uppercase as ss
#
#
# def generate_index():
#     letters1 = s(ss, 2)
#     letters2 = s(ss, 2)
#     numbers = str(r(100))
#     numbers2 =str(r(100))
#     return ''.join(letters1) + ''.join(numbers) + '_' + ''.join(numbers2) + ''.join(letters2)
#
# def generate_index():
#     n1, n2 = (randrange(100) for i in range(2))
#     a, b, c, d = (choice(ascii_uppercase) for i in range(4))
#     return (f'{a}{b}{n1}_{n2}{c}{d}')
#
# def generate_index():
#     return f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}{choice(letter)}{choice(letter)}'
#
# def generate_index():
#
#     kek = '112_211'
#     kek = kek.replace('1', random.choice(string.ascii_uppercase))
#     kek = kek.replace('2', random.choice(string.digits))
#
#     return kek

# print(chr(128139), ord('🧦'))


# from random import shuffle as s
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# m=[]
# for i in matrix:
#     s(i)
#     m.append(i)
#
# matrix=m
# print(matrix)

# from random import shuffle as s
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# [s(i) for i in matrix]
# print(matrix)
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# s(matrix)
# print(matrix)

# from random import randrange as r
#
# s=[]
# b=r(1000000,10000000)
# for _ in range(101):
#     if b not in s:
#         s.append(b)
#         print(b)
#         b = r(1000000, 10000000)
# from random import sample as r
#
# print(*r(range(int(1e6), int(1e7)), 100), sep='\n')
#
# from random import randint
# s=set()
# while len(s)!=100:
#     s.add(randint(1000000,9999999))
# print(*s,sep='\n')

#
# from random import shuffle as s
# word = input()
# # w=[i for i in word]
# w = list(word)
# s(w)
# print(''.join(w))


# import random
# def generate_bingo_card():
#     card = [['-' for _ in range(5)] for _ in range(5)]
#     nums = random.sample(range(1, 76), 24)
#     nums.insert(12, 0)
#     index = 0
#     for i in range(5):
#         for j in range(5):
#             card[i][j] = nums[index]
#             index += 1
#     return card
# def print_bingo_card(card):
#     for row in card:
#         print("".join(str(num).ljust(3) for num in row))
#
# card = generate_bingo_card()
# print_bingo_card(card)

# import random
# l=[input() for _ in range(int(input()))]
# random.shuffle(l)
# for i in range(len(l)):
#     print(f'{l[i-1]} - {l[i]}')

# import string
# import random
# def generate_password(length):
#     s=string.ascii_uppercase+string.ascii_lowercase+string.digits[2:]
#     s=''.join([i for i in s if i not in 'IloO'])
#     return ''.join(random.sample(s,length))
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n,m),sep='\n')

# import string
# import random
# def generate_password(length):
#     u=[i for i in string.ascii_uppercase if i not in 'IO']
#     l = [i for i in string.ascii_lowercase if i not in 'lo']
#     d=list(string.digits[2:])
#     s=u+l+d
#
#     r=[random.choice(i) for i in (u,l,d)]
#
#     r += [random.choice(s) for _ in range(length-3)]
#     return ''.join(r)
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n,m),sep='\n')

# import random
#
# n = 10
# k = 0
# s0 = 1
# for _ in range(n):
#     x = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
#     y = random.uniform(0, 1)     # случайное число с плавающей точкой от 0 до 1
#
#     if y <= x**2:                # если попадает в нужную область
#         k += 1
#
# print((k/n)*s0)

# import random
#
# n = 10**6
# k = 0
# s0 = 4
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#
#     if x**2 + y**2 <= 1:
#         k += 1
#
# print((k/n)*s0)

# from decimal import *
#
# num = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
#
# if num == 0:
#     print('YES')
# else:
#     print('NO')
# from decimal import *
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'.split()
#
# print(sum([Decimal(i) for i in s]))
# for i in sorted(s)[len(s)-1:len(s)-5:-1]:
#     print(i,end=' ')

# from decimal import *
# num = Decimal(input())
# num1=num.as_tuple().digits
# num1=[min(num1),max(num1)]
#
# if int(num)==0:
#     num1 = list(num.as_tuple().digits + (0,))
#     num1 = [min(num1), max(num1)]
# print(sum(num1))

# from decimal import *
# print(getcontext())
# d = Decimal(input())
# print(Decimal.exp(d)+Decimal.ln(d)+Decimal.log10(d)+Decimal.sqrt(d))

# from fractions import Fraction
#
# num1 = Fraction(5, 1)        # 5/1 = 5
# num2 = Fraction('0.95')
# n=num2.numerator# 23/23 = 1
#
# print(num1, num2,n, sep='\n')

# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# print(*[f'{i} = {Fraction(i)}' for i in numbers],sep='\n')

# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# v = [Fraction(i) for i in s.split()]
# mn=min(v)
# mx=max(v)
#
# print(*[f'{sum([mn,mx])}'])

# from fractions import Fraction
#
# n,m=int(input()),int(input())
#
# print(Fraction(n,m))
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# print(gcd(n,m))


# from fractions import Fraction
#
# a1 = input()
# b1 = input()
# a = Fraction(a1)
# b = Fraction(b1)
#
# sum_fraction = a + b
# print(f"{a1} + {b1} = {sum_fraction}")
#
# diff_fraction = a - b
# print(f"{a1} - {b1} = {diff_fraction}")
#
# mult_fraction = a * b
# print(f"{a1} * {b1} = {mult_fraction}")
#
# div_fraction = a / b
# print(f"{a1} / {b1} = {div_fraction}")


# from fractions import Fraction
#
# n = int(input())
#
# res = 0
# for i in range(1, n + 1):
#     res += Fraction(f'1/{i**2}')
#
# print(res)
#
# from fractions import Fraction
# import math
# n = int(input())
#
# print(sum([Fraction(1,math.factorial(i)) for i in range(1,n+1)]))

# from fractions import Fraction
#
# n = int(input())
# l=[]
# for i in range(1,n-1):
#     for j in range(i+1,n):
#         k=Fraction(i,j)
#         if k.numerator+k.denominator==n:
#             l.append(k)
# print(max(l))

# from fractions import Fraction
#
# n = int(input())
# s=set()
# for i in range(1,n):
#     for j in range(i+1,n+1):
#         s.add(Fraction(i,j))
#
# print(*sorted(s),sep='\n')

# n=int(input())
# a=input().split()
# l=set()
# for i in range(n):
#     l.add(int(a[i])+int(a[-(1+i)]))
# if len(l)==1:
#     print(*l)
# else:
#     print('-1')
#
# n = int(input())
# a = input().split()
# l = set(int(a[i]) + int(a[-(1 + i)]) for i in range(n))
# print(*l) if len(l) == 1 else print('-1')

# n=input().split()
# p=len(max(n[0],n[1]))
# l1=set([f'{i:0{p}}' for i in range(int(n[0]))])
# l2=[f'{j:0{p}}' for j in range(int(n[1]))]
# l3=set(j[::-1] for j in l2)
#
# print(len(l1&l3))

# n=input().split()
# p=len(max(n[0],n[1]))
# l1={f'{i:0{p}}' for i in range(int(n[0]))}
# l2=[f'{j:0{p}}' for j in range(int(n[1]))]
# l3={j[::-1] for j in l2}
#
# print(len(l1&l3))

# def count_palindrome(n, m):
#     max_length = len(str(max(n,m)))
#
#     n=int(n)
#     m = int(m)
#     count = 0
#     for hour in range(n):
#         for minute in range(m):
#             hour_str = str(hour).zfill(max_length)
#             minute_str = str(minute).zfill(max_length)
#             if hour_str==minute_str[::-1]:
#                 print(hour_str,minute_str)
#
#                 count += 1
#     return count
# n, m = input().split()
# result = count_palindrome(n, m)
# print(result)

# z1 = complex(input())
# z2 = complex(input())
#
#
# print(f'{z1} + {z2} = {z1+z2}')
# print(f'{z1} - {z2} = {z1-z2}')
# print(f'{z1} * {z2} = {z1*z2}')

# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# maximum = max(numbers, key=abs)
# print(maximum)
# print(abs(maximum))

# n = int(input())
# z1 = complex(input())
# z2 = complex(input())
#
# z11 = z1.conjugate()
# z22 = z2.conjugate()
#
# result = z1**n + z2**n + z11**n + z22**(n + 1)
# print(result)

# import turtle
#
# turtle.Screen().addshape('cherep.gif')  # регистрируем изображение
# turtle.shape('cherep.gif')              # устанавливаем изображение
# w,h=int(input()),int(input())
#
# def rectangle(w, h):
#   turtle.forward(w)
#   turtle.right(90)
#   turtle.forward(h)
#   turtle.right(90)
#   turtle.forward(w)
#   turtle.right(90)
#   turtle.forward(h)
#
# rectangle(w,h)

# def rectangle(width, height):
#   for _ in range(4):
#     turtle.forward(width)
#     turtle.left(90)
#     width, height = height, width
#
# width = int(input())
# height = int(input())
# rectangle(width, height)
#
# window = turtle.Screen()
#
# window.mainloop()
# import turtle
# def triangle(side):
#   for _ in range(3):
#     turtle.forward(side)
#     turtle.left(120)
# side = int(input())
# triangle(side)
# window = turtle.Screen()
# window.mainloop()

# import turtle
# square = turtle.Turtle()
# square.shape("turtle")
# square.color('red', 'green')
# square.begin_fill()
# for j in range(3):
#     square.left(20)
#
#     for i in range(4):
#         square.forward(100)
#         square.left(90)
# square.end_fill()
# turtle.exitonclick()

# import turtle as t
#
# t.shape('turtle')
# t.speed(0)
# t.width(40)
# colors = ['gold', 'tan', 'gold', 'burlywood', 'gold', 'goldenrod']
# def hexagon2(side):
#   for i in range(6):
#     t.right(60)
#     t.forward(side)
# n = 55
# for i in range(6):
#   t.pencolor(colors[i])
#   hexagon2(n)
#   t.backward(n)
#   t.right(60)
#
# t.exitonclick()

# import turtle
# import random
# screen = turtle.Screen()
#
# # Setting the screen color-mode
# screen.colormode(255)
# turtle.speed(0)
# turtle.pencolor('white')
# for i in range(60):
#
#
#   turtle.fillcolor(random.randrange(256), random.randrange(200), random.randrange(200))
#   turtle.begin_fill()
#   for _ in range(2):
#     turtle.forward(80-i)
#     turtle.left(60)
#     turtle.forward(90-i)
#     turtle.left(120)
#   turtle.end_fill()
#   turtle.left(21)
# turtle.exitonclick()


# import turtle
#
# turtle.Screen().setup(400, 400)               # устанавливаем размер граф. окна
# turtle.Screen().addshape('cherep.gif')    # добавляем форму черепашки
#
#            # устанавливаем фоновое изображение
# turtle.shape('cherep.gif')                # устанавливаем форму черепашки
# turtle.pencolor('green')
# turtle.pensize(5)
#
# for _ in range(4):
#
#   turtle.forward(150)
#   turtle.left(90)
#
# turtle.exitonclick()

# import turtle, math
# turtle.speed(0)
# turtle.up()
# def dart():
#     turtle.speed(0)
#     turtle.goto(0, -50)
#     turtle.down()
#     turtle.pensize(5)
#     turtle.left(45)
#     turtle.forward(150)
#     turtle.left(180)
#     turtle.forward(50)
#     turtle.left(180)
#     for _ in range(5):
#         x, y = turtle.pos()
#         turtle.left(45)
#         turtle.forward(15)
#         turtle.goto(x, y)
#         turtle.right(90)
#         turtle.forward(15)
#         turtle.goto(x, y)
#         turtle.left(45)
#         turtle.forward(10)
#     turtle.up()
#     turtle.goto(-56, -106)
#     turtle.left(180)
#     turtle.down()
#     turtle.forward(60)
#     turtle.shape('arrow')
#     turtle.stamp()
# def heart():
#     turtle.speed(0)
#     turtle.fillcolor('red')
#     turtle.begin_fill()
#     for t in range(630):
#         t *= 0.01
#         x = 128 * math.sin(t) ** 3
#         y = 8 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t) - 5)
#         turtle.goto(x, y)
#     turtle.end_fill()
# heart()
# dart()
# turtle.exitonclick()

# def matrix(n=1,m=None,s=0):
#     if m==None:
#         m=n
#     matrix = [[s for _ in range(m)] for _ in  range(n)]
#     return matrix
#
# print(matrix(3,4,9))


# def mean(*args):
#     nums = []
#     for arg in args:
#         if isinstance(arg, (int, float)) and not isinstance(arg, bool):
#             nums.append(arg)
#     if len(nums) == 0:
#         return 0.0
#     else:
#         return sum(nums) / len(nums)
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def greet(a,*names):
#     if len(names) == 0:
#         return f"Hello, {a}!"
#     elif len(names) > 0:
#         return "Hello, "+f'{a} and '+" and ".join([i for i in names])+'!'

# def greet(name, *names):
#     return f"Hello, {' and '.join([name] + [*names])}!"
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan', 'Roman', 'Ruslan'))

# def print_products(*args):
#     products = []
#     for arg in args:
#         if isinstance(arg, str) and arg != '':
#             products.append(arg)
#     if len(products) == 0:
#         print("Нет продуктов")
#     else:
#         for i, product in enumerate(products, 1):
#             print(f"{i}) {product}")
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)

# def info_kwargs(**kwargs):
#     keys = sorted(kwargs.keys()) # сортировка ключей по алфавиту
#     for key in keys:
#         print(f"{key}: {kwargs[key]}")
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# def f(x):
#     return sum(x)/len(x)
# min_avg = min(numbers, key=f)
# max_avg = max(numbers, key=f)
#
# print(min_avg)
# print(max_avg)

# import math
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# def f(x):
#     return math.sqrt(x[0]**2 + x[1]**2)
# min_avg = sorted(points,key=f)
# print(min_avg)


# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# def f(x):
#     return min(x) + max(x)
# min_avg = sorted(numbers,key=f)
# print(min_avg)

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# def f1(x):
#     return x[0]
# def f2(x):
#     return x[1]
# def f3(x):
#     return x[2]
# def f4(x):
#     return x[3]
# s=int(input())
# ff=[f1,f2,f3,f4]
# min_avg = sorted(athletes,key=ff[s-1])
# for athlete in min_avg:
#     print(*athlete)
# def compare(x):
#     return x[i-1]
# i=int(input())
# athletes.sort(key=compare)
# for item in athletes:
#     print(*item)

# num = int(input())
# func = input()
#
# import math
# num_functions = {
#     'квадрат': lambda x: x ** 2,
#     'куб': lambda x: x ** 3,
#     'корень': lambda x: x ** 0.5,
#     'модуль': abs,
#     'синус': math.sin
# }
#
# result = num_functions[func](num)
# print(result)

# def sort_by_digit_sum(lst):
#     def digit_sum(num):
#         return sum(int(digit) for digit in str(num))
#
#     return sorted(lst, key=digit_sum)
#
# numbers = input().split()
# numbers = [int(num) for num in numbers]
# sorted_numbers = sort_by_digit_sum(numbers)
# print(' '.join(map(str, sorted_numbers)))

# n = input().split()
# def digits_sum(num):
#     return sum([int(digit) for digit in str(num)])
# sorted_list = sorted(n, key=lambda x: (digits_sum(x), int(x)))
#
# print(" ".join(sorted_list))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def f(x):
#     return round(x, 2)
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# n=map(f,numbers)
#
# print(*n,sep='\n')

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result

# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# def f(n):
#     return (100 <= n <= 999) and n%5==2
# def f1(n):
#     return n**3
# c1=filter(f,numbers)
# c=map(f1,c1)
#
# print(*c,sep='\n')

# def filter_and_map(numbers):
#     filtered_numbers = filter(lambda x: x % 5 == 2 and 99 < x < 1000, numbers)
#     cubes = map(lambda x: x ** 3, filtered_numbers)
#     for cube in cubes:
#         print(cube)
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# filter_and_map(numbers)

#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# def op(n, n1):
#     return n+n1**2
# print(reduce(op,numbers,0))


# def sum_of_squares(acc, item):
#     return acc + item**2
#
# result = reduce(sum_of_squares, numbers, 0)
# print(result)
#
# # С помощью функций map() и sum()
# squared_numbers = map(lambda x: x**2, numbers)
# result = sum(squared_numbers)
# print(result)

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# def is_two_digit(num):
#     return abs(num) >= 10 and abs(num) <= 99
#
# def is_divisible_by_seven(num):
#     return num % 7 == 0
#
# filtered_numbers = filter(lambda x: is_two_digit(x) and is_divisible_by_seven(x), numbers)
# squared_numbers = map(lambda x: x ** 2, filtered_numbers)
# sum_of_squares = sum(squared_numbers)
#
# print(sum_of_squares)

# def func_apply(func, values):
#     return [func(x) for x in values]
#
# def add3(x):
#     return x + 3
#
# def mul7(x):
#     return x * 7
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

# def func(elem1, elem2, elem3):
#     return elem1 + elem2 + elem3
#
#
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [10, 20, 30, 40, 50]
# numbers3 = [100, 200, 300, 400, 500]
#
# new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
#
# print(new_numbers)

# from functools import reduce
# import operator
#
# words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
# numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]
#
# numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
# concat_words = reduce(operator.add, numbers)             #  конкатенация элементов списка
#
#
# print(concat_words)

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2,1), floats))
# filter_result = list(filter(lambda name: name==name[::-1] and len(name)>4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# # Фильтрация городов с населением более 10000000 человек и со значением 'primary'
# filtered_cities = filter(lambda x: x[1] > 10000000 and x[2] == 'primary', data)
#
# # Получение только названий городов
# city_names = map(lambda x: x[0], filtered_cities)
#
# # Сортировка городов в алфавитном порядке
# sorted_cities = sorted(city_names)
#
# # Соединение названий городов через запятую
# result = reduce(lambda x, y: x + ', ' + y, sorted_cities)
#
# print('Cities:', result)

# func = lambda x: 'True' if x%19==0 or x%13==0 else 'False'
# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

# is_non_negative_num = lambda arg: arg.replace('.', '', 1).isdigit() and float(arg) >= 0
#
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

# is_non_negative_num= lambda x: True if x.replace('.','',1).isdigit() and x[0]!='-' and x.count('.') <=1 else False
#
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))
#
# is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()

# is_num = lambda q: q.strip('-').replace('.', '', 1).isdigit() and q.count('-') <=1
# print(is_num('11-'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# print(*sorted(filter(lambda x: len(x)==6,words)))

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# filtered_numbers = list(filter(lambda x: not (x % 2 != 0 and x > 47), numbers))
# mapped_numbers = list(map(lambda x: x // 2 if x % 2 == 0 else x, filtered_numbers))
#
# print(*mapped_numbers)

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# s=sorted(data,key=lambda x: x[1][-1], reverse=True)
# for i in s:
#     print(f'{i[1]}: {i[0]}')

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# print(*sorted(data,key=lambda x: (len(x),x)))

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
# max_value = max(filter(lambda x: isinstance(x, int), mixed_list))
# print(max_value)

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# # d=sorted(filter(lambda x: isinstance(x, int),mixed_list))
# # s=list(filter(lambda x: isinstance(x, str),mixed_list))
# # s1=sorted(s,key=lambda x: (x))
# # print(*(d+s1))
#
# print(*sorted(mixed_list, key=lambda x: isinstance(x, int),reverse=True))

# print(*map(lambda x: str(255 - int(x)),input().split()))


# from functools import reduce
#
# # def evaluate(coefficients, x):
# #     n = len(coefficients) - 1
# #     exponent = map(lambda i: x ** (n - i), range(n+1))
# #     terms = map(lambda a, b: a * b, coefficients, exponent)
# #     result = reduce(lambda a, b: a + b, terms)
# #     return result
#
# def evaluate(coefficients, x):
#     e=list(range(len(coefficients)-1,0,-1))+[0]
#     m=list(map(lambda a,e,x1: a*(x1**e),coefficients,e,[x]*len(coefficients)))
#     result=reduce(lambda a,b: a+b, m)
#     return result
#
# # считываем коэффициенты и значение x
# coefficients = list(map(int, input().split()))
# x = int(input())
#
# # вызываем функцию evaluate и выводим результат
# print(evaluate(coefficients, x))


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# for (c,ca,p) in zip(countries,capitals,population):
#     print(f'{ca} is the capital of {c}, population equal {p} people.')

# abscissas = input().split()
# ordinates = input().split()
# applicates = input().split()
# points = list(zip(abscissas, ordinates, applicates))
# R = 2
# result = all(float(x)**2 + float(y)**2 + float(z)**2 <= R**2 for x, y, z in points)
# print(result)

# ip_address = input().split('.')
#
# valid = all(int(octet) >= 0 and int(octet) <= 255 if octet.isdigit() else False for octet in ip_address)
#
# print(valid)
#
# print(all(map(lambda n: n.isdigit() and 0 <= int(n) <= 255, input().split('.'))))

# a = int(input())
# b = int(input())
#
# result = []
# for num in range(a, b+1):
#     if any(digit == '0' for digit in str(num)):
#         continue
#     if all(num % int(digit) == 0 for digit in str(num)):
#         result.append(str(num))
#
# print(' '.join(result))

# s = input()
# if len(s) >= 7 and any(c.isdigit() for c in s) and any(c.isupper() for c in s) and any(c.islower() for c in s):
#     print("YES")
# else:
#     print("NO")

# n = int(input())
# flag = True
# for _ in range(n):
#     k = int(input())
#     grades = []
#     for _ in range(k):
#         surname, grade = input().split()
#         grades.append(int(grade))
#     if not any(grade == 5 for grade in grades):
#         flag = False
#         break
# if flag:
#     print("YES")
# else:
#     print("NO")

# def display(**kwargs):
#     for i in kwargs:
#         print(i, end=' ')
#
# display(emp='Kelly', salary=9000)

# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number='17'):
#     return f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!'''
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))

# def pretty_print(data, side='-', delimiter='|'):
#     row = ''
#     for item in data:
#         row += f" {delimiter} {str(item)}"
#     row = row.strip()
#
#     print(f" {side * (len(row))}")
#     print(f"{row} {delimiter}")
#     print(f" {side * (len(row))}")
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])


# def concat(*args, sep=' '):
#     return sep.join(str(arg) for arg in args)
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


# from functools import reduce
# def product_of_odds(data):
#     return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data),1)

# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: f'"{x}"',words))

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
#
# print(sorted_numbers)

# def arithmetic_operation(operation):
#     if operation == '+':
#         return lambda x, y: x + y
#     elif operation == '-':
#         return lambda x, y: x - y
#     elif operation == '*':
#         return lambda x, y: x * y
#     elif operation == '/':
#         return lambda x, y: x / y
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))

# s = "cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo"
# print(' '.join(sorted(s.split(), key=str.lower)))

# n = int(input())
# words = []
# for _ in range(n):
#     word = input()
#     hematria = sum(ord(letter) - ord('A') for letter in word.upper())
#     words.append((word, hematria))
#
# words.sort(key=lambda x: (x[1],x[0]))
# for word, _ in words:
#     print(word)

# n = int(input())
# ip_addresses = []
# for _ in range(n):
#     ip_addresses.append(input())
#
# ip_addresses.sort(key=lambda x: sum(int(b) * 256 ** (3 - i) for i, b in enumerate(x.split('.'))))
# for ip in ip_addresses:
#     print(ip)


prices_file = open('prices.txt', 'r')
total_cost = 0

for line in prices_file:
    product, quantity, price = line.strip().split('\t')
    total_cost += int(quantity) * int(price)

print(total_cost)
prices_file.close()

