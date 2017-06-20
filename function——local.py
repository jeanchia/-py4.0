x = 50

def func(x):   # 局部变量 func里的变量x 作用域 仅限于函数内
    print('x is',x)
    x = 2
    print('Changed local x to',x)


func(x)
print('x is still',x)
