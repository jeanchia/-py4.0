#推荐总是使用括号来指明元组的开始与结束
#尽管括号是一个可选选项，但明了胜过晦涩，这很pythonic
zoo = ('python','elephant','panda','monkey')
print('Number of animals in the zoo is',len(zoo))

new_zoo = 'camel','lion',zoo
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][3])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))#== len(new_zoo)-1+len(zoo)