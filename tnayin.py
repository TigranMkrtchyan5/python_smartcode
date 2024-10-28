#85-109 116,117,118,119,121,124,125,133,134,135
# --------------------------------------------------------------------------------
# N39
# C = int(input('greq jermastichany yst celsiusi:  '))
# fahrenheit = C * 9/5 + 32
# kelvin = C + 273.15
# print(f'celsius {C} , fahrenheit {fahrenheit}, kelvin {kelvin}')
# -------------------------------------------------------
# N40
# dzayn = int(input('greq dzayni ujexutyuny:  '))
# chaguch = 130
# kasilka =  106 
# budilnik = 70 
# datark_senyak = 40
# if dzayn <= 55:
#         print('datark senyak')
# elif dzayn >=56 and dzayn <= 88:
#         print('budilnik')
# elif dzayn >=89 and dzayn<= 118:
#     print('kasilka')
# else:
#     print('chaguch')
# ------------------------------------------------------------------------------------
#N41         
# a = int(input('greq a tivy: '))
# b = int(input('greq b tivy: '))
# c = int(input('greq c tivy: '))
# if a < 0 or b < 0 or c < 0:
#     print('aydpisi erankyun chka')
# elif a > b and a > c and b + c < a or b > c and b > a and a + c < b or c > a and c > b and a + b < c:
#     print('aydpisi erankyun goyutyun chuni')
# elif a == b == c :
#     print('dzer erankyuny havasarakoghm e ')
# elif a == b  or a==c  or b==c  :
#     print('dzer erankyuny havasarasrun e')
# else: 
#     print('sovorakan erankyun e')
# -------------------------------------------------------------------------------------------    
# N46
# tiv=int(input('greq tivy : '))
# tar=input('yntreq tary a,b,c,d,e,f,g,h: ')
# list1=['a','b','c','d','e','f','g','h']
# if tiv > 8:
#     print('dzer tivy 8 ic mets e')
# else:
#     pass
# if tiv % 2 == 1 and tar in  list1[::2]:
#     print('sev vandak')
# elif tiv % 2 == 0 and tar in list1[1::2]:
#     print('sev vandak')
# else:
#     print('spitak vandak')
# --------------------------------------------------------------------------------------------
# N63
# count = 0 
# while True:
#     tiv = int(input('greq tiv: '))
#     if tiv == 0:
#         break
#     count += tiv
#     print(count / 2)
# ----------------------------------------------------------------------------------------------
# N69
# cass = 0
# while True:
#     tariq = int(input('Enter age: '))
#     if tariq == 0:
#         print(cass)
#         break
#     elif 3 > tariq > 0:
#         continue
#     elif 12 > tariq >= 3:
#         cass += 14
#     elif 65 > tariq >= 12:
#         cass += 23
#     else:
#         cass += 18
# ------------------------------------------------------------------------------------------
# N75
# name = input('Enter name: ')
# print((name==name[::-1]))
# ----------------------------------------------------------------------------------------------------
# N81 (nayel em)
# text = input('Enter bin text: ')
# text = text[::-1]
# number = 0
# for i in range(0, len(text)):
#     number += int(text[i]) * 2 ** i
# print(number)
# ------------------------------------------------------
# N82
# n = int(input('Enter decimal number: '))
# s = ''
# while True:
#     if n == 1:
#         break
#     else:
#         s += str(n % 2)
#         n //= 2
# print('1' + s[::-1])
# ------------------------------------------------------
# N83 (nayel em)
# import random

# first_number = random.randint(1, 100)
# print(first_number)
# for i in range(99):
#     number = random.randint(1, 100)
#     if number > first_number:
#         print(number, 'update')
#         first_number = number
#     else:
#         print(number)
# ----------------------------------------------------------------------------
#N84 (nayel em)
#  import random

# for i in range(10):
#     qanak_O = 0
#     qanak_P = 0
#     a = " "
#     while True:
#         if qanak_O == 3 or qanak_P == 3:
#             print(a)   
#             break
#         else:
#             pc = random.choice("OP")
#             a += pc
#     if pc == 'O':
#         qanak_O += 1
#         qanak_P = 0
#     else:
#         qanak_P += 1 
#         qanak_O = 0
# ----------------------------------------------------------------------------
# N110
# list1 = []
# while True:
#     tiv = int(input('greq tiv: '))
#     if tiv == 0:
#         break
#     else:
#         list1.append(tiv)
#         list1.sort()
#         print(list1)
# --------------------------------------------------------------------------------
# N111
# list1 = []
# while True:
#     tiv = int(input('greq tiv: '))
#     if tiv == 0:
#         break
#     else:
#         list1.append(tiv)
#         list1.sort()
    
# print(list1[::-1])
# --------------------------------------------------------------------------------------------------
# N113
# barer = []
# while True:
#     bar = input('greq bary: ')
#     if bar in barer:
#         print(barer)  
#         break
#     elif bar == '':
#         print(barer)
#         break
#     else:
#         barer.append(bar)
#         print(barer)
# ----------------------------------------------------------------------------------------------------
# N114
# bacasakan = []
# drakan = []
# zro = []
# while True:
#     tiv = input('greq tiv: ')
#     if tiv == '':
#         break
#     elif int(tiv) < 0:
#         bacasakan.append(tiv)
#     elif int(tiv) == 0:
#         zro.append(tiv)
#     elif int(tiv) > 0:
#         drakan.append(tiv)
#     print(bacasakan + zro + drakan)
# -----------------------------------------------------
# N115
# arr = []
# tiv = int(input('greq tivy: '))
# for i in range(1,tiv):
#     if tiv % i == 0:
#         arr.append(i)
# print(arr)
# -------------------------------------------------------
# N116
# tiv = int(input('text: '))
# summ = 0
# for i in range(1,tiv//2+1):
#     if tiv % i == 0:
#         summ += i
# print(summ == tiv)
# ----------------------------------------------------------
# N117
# text = "Contractions!. include: don’t,/ .’..isn’t, and wouldn’t."
# text = text.split(' ')
# # mylist = []
# for i in text:
#     while True:
#         if i[0].isalpha() and i[-1].isalpha():
#             mylist.append(i)
#             break
#         elif not i[0].isalpha():
#             i = i[1:]
#         elif not i[-1].isalpha():
#             i = i[:-1]
# print(mylist)
# print(' '.join(mylist))
# ----------------------------------------------------------------------------------------
# N118
# a = input('greq texty: ')
# a = a.split()
# print(a)
# skizb = 0
# verj = len(a) -1
# for i in range(len(a)):
#     if a[skizb] == a[verj]:
#         skizb += 1
#         verj -= 1
#         if skizb == verj or skizb - verj == 1:
#             print('ayo')
#             break
# else:
#     print('che')
# ------------------------------------------------------------------------
















# def nerqnadziq():

#     a = int(input('greq a erkarutyuny: '))
#     b = int(input('greq b erkarutyuny: '))
#     c = (a ** 2 + b ** 2) ** 0.5
#     print(int(c))

# nerqnadziq()
# ------------------------------------------------------------
# N86
# def taxi():

#     heravorutyun = float(input('qani m eq gnum: '))
#     skizb = 4.0
#     while heravorutyun >= 140:
#         tiv = heravorutyun // 140
#         meter_140 = 0.25
#         verj = meter_140 * tiv
#         skizb += verj

#         print(skizb + verj, '$')
#         break
# taxi()


# ----------------------------------------------------
# N87
# def araqum():

#     apranq = int(input('inchqan apranq eq araqum? '))
#     araqum = 10.95
#     araqum_1 = 2.95
#     if apranq == 1:
#         print(int(araqum + araqum_1))
#     elif apranq >= 2:
#         print(float(apranq  * araqum_1 + araqum))

# araqum()
# --------------------88--------------------------------
# def median(a,b,c):
#     list1 = [a,b,c]
#     list1.sort()
#     return list1[1]

# print(median(2,4,5))
# ------------------------------------------------
# import random

# def hamarner():
#     tar = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     return f'{random.randint(0,9)}{random.randint(0,9)} {random.choice(tar)}{random.choice(tar)} {random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
    
# print(hamarner())
# -----------------------------------------------------------------------
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i * j:>4}' , end = " ")
#         print()
# -----------------------------------------------------------------------
# def func():

#     n = int(input('sovorakan tiv: '))
#     s = ''
#     while True:
#         if n == 1:
#             break
#         else:
#             s += str(n % 2)
#             n //= 2
#     print('1' + s[::-1])

# func()
# -------------------------------------------------------------------------------
# def func():
    
#     text = input('Enter bin text: ')
#     text = text[::-1]
#     number = 0
#     for i in range(0, len(text)):
#         number += int(text[i]) * 2 ** i
#     return number

# print(func())
# ----------------------------------------------------------
