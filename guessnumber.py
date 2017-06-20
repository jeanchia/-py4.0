number = 66
guess = int(input('Enter an integer:'))

if guess ==number:
    #new block star here!
    print('Congratulations, you guessde it.')
    print("(but you don't win any prizes!)")
    #new block end  here!
elif guess<number:
    #another block
    print('No,it is a little higher than that')
    #you can do anthing in bolck if you want
else:
    print('No,it is a little lower than that')
    #you must guess a number>66 to here

print('Done')
#this code will run after the 'if ' block run over