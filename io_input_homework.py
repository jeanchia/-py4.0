denotes = ['.',',','!','?',' ']

def normalize(string):
    str = string.strip()
    str = str.lower()
    for note in denotes:
        str = str.replace(note, '')
    return str

def reverse(string):
    str = string[::-1]
    return str

def is_palindrome(string):
    str = normalize(string)
    print('String after normalization: {}'.format(str))
    str_reversed = reverse(str)
    print('String after reversion:{}'.format(str_reversed))
    if str == str_reversed:
        return 0
    else:
        return 1

something = input('Enter text:')
if is_palindrome(something) == 0:
    print('{} is palindrome.'.format(something))
else:
    print('{} is not palindrome.'.format(something))
