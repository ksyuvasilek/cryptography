from random import randint, randrange
from math import log, pi 
import time

start = time.time() #время начала работы программы
N = 10**100 #крайняя правая граница выбора двух чисел а и b
M = 10000 #кол-во испытаний

#функция для отыскания НОД(a,b) - алгоритм Евклида
def NOD(a, b):
    count = 0
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        count += 1
    return count #возвращаем - кол-во итераций

i = 0
itter = 0
a1 = 0
b1 = 0
while i < M:
    a = randint(1, N) #генерация случайного числа а
    a1 += a
    b = randint (1, N) #генерация случайного числа b
    b1 += b
    itter += NOD(a,b) #складываем кол-во итераций для каждого эксперимента
    i += 1
print("Среднее число а: ", a1/M)
print("Среднее чсло b: ", b1/M)
print("Число делений с остатком: ", itter)
print("Среднее число делений с остатком: ", itter/M)
print("Теоретическая оценка: ", 12*log(2)*log(N)/pi**2)

if (12*log(2)*log(N)/pi**2) > (itter/M):
    print("Теоретическая оценка выше экспериментальной.")
else:
    print("Экспериментальная оценка выше теоретической.")
print("Время выполнения: ", time.time() - start, "секунд.")
