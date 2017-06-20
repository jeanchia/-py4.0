# 这是一个字符串对象
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes,the string stars with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes,it contans the string "war"')

delimiter = '_*_'    # delimiter分隔符
mylist = ['brazil','china','usa','uk']
print(delimiter.join(mylist))