PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


lines_list = PRICE_LIST.splitlines()

# print(lines_list)
# print(type(lines_list))

price_list_dict = {}

for line in lines_list:
    item, price = line.split()
    price = int(price[:-1])
    price_list_dict[item] = price
    
print(price_list_dict)