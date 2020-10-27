import math
import random
P = math.pow(10, -6)
V = 11
T = 20160 
Alphabet="0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
S = (V * T) / P
A = len(Alphabet)
L = 0
while math.pow(A, L) <= S:
    L += 1
Pass = ""
for i in range(L):
    Pass += Alphabet[random.randint(0, A-1)]
Vzlom = (A**L * P / V) / 10080
print("S=",S) 
print("Ваш пароль:", Pass)
print("Ваш пароль будет взломан через", Vzlom, "недели")
