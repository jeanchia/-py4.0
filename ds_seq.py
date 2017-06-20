shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

# indexing or 'Subscription' operation #
# 索引或‘下标’操作符 #
print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is', shoplist[-1])
print('Character 0 is',name[0])

# slicing on a list#
print('Item 1 to 3 is',shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串切片 #
print('characters 1 to 3 is',name[1:3])
#类似，不在赘述

# 上面的步长为1 ，步长可以设置
print('每2个item取一个',shoplist[::2])
print('步长为负，倒着取',shoplist[::-2])