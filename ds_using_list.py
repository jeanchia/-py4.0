#this is my shopping list
shoplist = ['apple','mango','carrot','banana']

print('I have',len(shoplist),'item to purchase.')

print('These items are:',end=' ')
for item in shoplist:
    print(item,end=' ')

print('\nI also have to buy noodles.')
shoplist.append('noodles')
print('My shoplist is now',shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)

print('The first item I will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)