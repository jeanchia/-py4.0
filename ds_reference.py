print('Simple Assignment')
shoplist = ['apple','mango','carrot','banana']
# mylist just指向同一对象的另一种称呼
mylist = shoplist #区别在这里！！！！

# 我购买了第一个项目，so 在列表内将其删除
del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)
# 注意到 shoplist和mylist都打印出了其中没有apple的列表，因此我们确认他们指向同一对象

print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:] #区别在这里！！！！
# 删除第一个项目
del mylist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)
#  你会发现现在两个列表输出的不一样了！证明二者不是指向同一对象