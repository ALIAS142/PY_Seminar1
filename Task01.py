# Задача №1. Решение в группах Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: n = 700 m = 750 Output: 2

print("Enter first number - km in day:  ")
n = int(input())
print("Enter second number - km in day:  ")
m = int(input())

day = int(24)

day2 = (m - n) / day

print(round(day2))