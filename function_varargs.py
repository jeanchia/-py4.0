#可变参数
def total(a=5,*numbers,**kw):
    print('a',a)

    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item',single_item)

    #遍历字典中的所有项目
    for first_part,second_part in kw.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=1100,Jean=1000))