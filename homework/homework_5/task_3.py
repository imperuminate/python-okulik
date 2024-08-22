import random

i = 0
my_list = []
while i < 15:
    my_list.append(round(random.random() * 10))
    i += 1
print(my_list)
print('Максимальное сгенерённое число:\n', max(my_list))
print('Минимальное сгенерённое число:\n', min(my_list))
print('Сумма всех сгенерённых чисел:\n', sum(my_list))
print('Среднее арифметическое:\n', sum(my_list) / i)