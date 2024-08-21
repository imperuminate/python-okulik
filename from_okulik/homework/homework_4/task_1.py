my_dict = {'tuple': ('t1', 't2', 't3', 't4', 't1'),
           'list': ['l1', 'l2', 'l3', 'l4', 'l1'],
           'dict': {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
           'set': {'s1', 's2', 's3', 's4', 's1'},
           'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
           }


print(my_dict['tuple'][2:])

my_dict['list'].append(42)
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict']['(\'i am a tuple\',)'] = 8
my_dict['dict'].pop(2)
print(my_dict['dict'])


my_dict['set'].add(43)
my_dict['set'].remove('s2')
print(my_dict['set'])

print(my_dict['str'][:8])
s_lengt = len(my_dict['str'])
start = (s_lengt - 4) // 2
end = start + 4
print(my_dict['str'][start:end])
print([my_dict['str'][i] for i in range(len(my_dict['str'])) if i % 3 == 0])