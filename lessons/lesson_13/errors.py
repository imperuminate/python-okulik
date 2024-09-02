def calc(x, y):
    
    try:
        return int(x) / int(y)
    
    except ZeroDivisionError:
        return 'На ноль нельзя делить! '
    except ValueError:
        return 'Ввел не цыфры а хуйню, хуй! '
    
    # except (ZeroDivisionError, ValueError) as err:
    #     print(err)
    #     return 'Ошибка ввода данных. Да, такой не информативный эррор'
    
    # except (ZeroDivisionError, ValueError) as err:
    #     print(x, y)
    #     raise err

print(calc(input('Number: '), input('Number: ')))
print('hello')