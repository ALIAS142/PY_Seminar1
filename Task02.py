# Задача №3. Решение в группах В некоторой школе решили набрать три новых математических класса и
# оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

print("Enter quantity of puiples in class1:   ")
a = int(input())
print("Enter quantity of puiples in class2:   ")
b = int(input())
print("Enter quantity of puiples in class3:   ")
c = int(input())

people_on_table = int(2)

tables = round(a/people_on_table + b/people_on_table + c/people_on_table)
print(tables)
