stroka = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
stroka_list = stroka.split()
new_sroka = []

for word in stroka_list:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
        new_sroka.append(word)
    elif word.endswith('.'):
        word = word.replace('.', 'ing.')
        new_sroka.append(word)
    else:
        word += 'ing'
        new_sroka.append(word)
final_stroka = ' '.join(new_sroka)
print(final_stroka)

stroka = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
stroka_list = stroka.split()
new_stroka = []

for word in stroka_list:
    suffix = ''
    if word.endswith(','):
        suffix = ','
        word = word.rstrip(',')
    elif word.endswith('.'):
        suffix = '.'
        word = word.rstrip('.')
        
    new_word = word + 'ing' + suffix
    new_stroka.append(new_word)
final_stroka = ' '.join(new_stroka)
print(final_stroka)
