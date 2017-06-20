def print_max(a,b): #在定义时给定的名称为'形参'
    if a > b:
        print(a,'is maximum')
    elif a == b:
        print(a,'is equal to',b)
    else:
        print(b,'is maxmum')

#直接传递字面值
print_max(3,4)# 在调用时你所提供给函数的值为'实参'

x = 5
y = 7

#以参数形式传递变量
print_max(x,y)