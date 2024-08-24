from random import choice, random, randint, randrange
from helper import helper as hp

print(random())
print(f'Your price is {int(random() * 100)}')

print(randint(0, 10))  # включительно
print(randrange(0, 10))  #  нe включительно
print(randrange(0, 10, 2))  #  не включительно, третий агрумент определяет шаг

users = ['user11', 'user12', 'user100']
print(choice(users))

hp.assist()

