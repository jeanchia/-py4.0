class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('Hello,my name is',self.name)


p = Person('Jean')
p.say_hi()
# 前两行 == Person('Jean').say_hi()
