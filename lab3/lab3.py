from random import randint
from math import log, pi 
import time

start = time.time() #время начала работы программы
N = 10**100 #крайняя правая граница выбора двух чисел а и b
M = 10000 #кол-во испытаний

#сравнение остатка от деления с половиной делителя
def comparison(b, N): 
    if N%b < b/2:
        return 1
    else:
        return 0

i = 0
itter = 0
while i < M:
    b = randint(1, N) #генерация случайного числа а
    itter += comparison(b, N) #складываем кол-во итераций, когда остаток от деления меньше половины делителя
    i += 1

print("Кол-во итераций, когда остаток от деления меньше половины делителя: ", itter)
print("Вероятность, что остаток от деления N на b меньше половины делителя: ", itter/M)
print("Теоретическая оценка: ", 2-2*log(2))

if (2-2*log(2)) > (itter/M):
    print("Теоретическая оценка выше экспериментальной.")
else:
    print("Экспериментальная оценка выше теоретической.")
print("Время выполнения: ", time.time() - start, "секунд.")
