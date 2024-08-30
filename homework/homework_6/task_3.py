def add(x, y):
    print(x + y)
    return x + y


def subtract(x, y):
    print(x - y)
    return x - y


def multiply(x, y):
    print(x * y)
    return x * y


def divide(x, y):
    if x == 0:
        print('Ошибка деления на 0 ! ')
    else:
        print(x / y)
        return x / y


print('Выберите операцию: \n'
      '1. Умножение\n'
      '2. Деление\n'
      '3. Сложение\n'
      '4. Вычитание')


operation = int(input('Введите номер операции: '))

if operation in [1, 2, 3, 4]:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
else:
    print('Нет такой операции, брат! ')


if operation == 1:
    multiply(num1, num2)
elif operation == 2:
    divide(num1, num2)
elif operation == 3:
    add(num1, num2)
elif operation == 4:
    subtract(num1, num2)
