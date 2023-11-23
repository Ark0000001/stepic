# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print(3)
# elif a == b != c or a != b == c or a == c != b:
#     print(2)
# else:
#     print(0)

# n = int(input())

# for i in range(1, n + 1):
#
#     if i >= 5 and i<=9:
#         continue
#     if  i>= 17 and i<=37:
#         continue
#     if i >= 78 and i<=87:
#         continue
#     print(i)

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n=int(input())
# count=0
# for i in range(n):
#     for j in range(i+1):
#         count+=1
#         print(count, end=' ')
#     print()


# n=int(input())
#
# for j in range(n,0,-1):
#     for i in range(1,j+1):
#         print(i, end='')
#
#     for i in range(j-1,0,-1):
#         print(i, end='')
#     print()


# n=int(input())
#
# while n>9:
#     s=0
#     while (n>0):
#         l=n%10
#         s+=l
#         n=n//10
#     n=s
# print(n)


# n=int(input())
# t=0
# f=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         f*=j
#     t+=f
#     f=1
# print(t)


#
# n = int(input())
# s = 0
# while n > 0:
#     p=n%10
#     if p % 2 == 0:
#         s +=p
#
#     n //= 10
# if s>0:
#     print(s)
#
#
#
# n = int(input())
# s = 0
# while n != 0:
#     p = n % 10
#     if p % 2 == 0:
#         s += p
#     n //= 10
# if s > 0:
#     print(s)

# рамка
# n = int(input())
# for i in range(n):
#     for j in range(19):
#         if i == 0 or j == 0 or i == (n - 1) or j == 18:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# n = int(input())
# count3 = 0
# lastCount = 0
# chCount = 0
# sum5 = 0
# mult7 = 1
# count05 = 0
# l = n % 10
#
# while n > 0:
#     x = n % 10
#     if x == 3:
#         count3 += 1
#     if x == l:
#         lastCount += 1
#     if x % 2 == 0:
#         chCount += 1
#     if x > 5:
#         sum5 += x
#     if x > 7:
#         mult7 *= x
#     if x == 0 or x == 5:
#         count05 += 1
#     n //= 10
#
# print(count3)
# print(lastCount)
# print(chCount)
# print(sum5)
# print(mult7)
# print(count05)



# def find_interesting_numbers():
#     i = 1
#     while i<50000:
#         count = 0
#         for x in range(1, int(i**(1/3))+1):
#             for y in range(x, int(i**(1/3))+1):
#                 if x**3 + y**3 == i:
#                     count += 1
#                     if count == 2:
#                         print(i)
#                         break
#             if count == 2:
#                 break
#         i += 1
# find_interesting_numbers()

# a=input().lower()
# g1=0
# s1=0
# s='бвгджзйклмнпрстфхцчшщ'
# g='ауоыиэяюёе'
# for i in a:
#     for j in g:
#         if i==j:
#             g1+=1
#     for m in s:
#         if i == m:
#             s1 += 1
#
# print(f'Количество гласных букв равно {g1}')
# print(f'Количество согласных букв равно {s1}')


# n = int(input())
# b = ""
#
# while n > 0:
#     r = n % 2
#     b = str(r) + b
#     n = n // 2
#
# print(b)


s = input()
n = len(s)
half = n // 2
if n % 2 == 0:
    part1 = s[:half]
    part2 = s[half:]
else:
    part1 = s[:half+1]
    part2 = s[half+1:]
result = part2 + part1
print(result)