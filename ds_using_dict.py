# 'ab'此处是adress book的缩写

ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'Jean':'jean@jeanch.ore',
    'John':'jhon@ruby-lan.org',
    'Spider':'spider@ss.net'
}

print('Swaroop\'s address is',ab['Swaroop'])


#delete a couple key-value
del ab['Spider']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))

#add a couple key-value
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nGuido\'s address is',ab['Guido'])