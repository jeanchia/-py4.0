# encoding=UTF-8

class ShortInputException(Exception):
    '''一个由用户定义的异常class'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter somthing -->')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
    # 其他工作能在此次继续运行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was'+
           '{} long,expected at least {}')
          .format(ex.length,ex.atleast))
else:
    print('No exception was raised.')