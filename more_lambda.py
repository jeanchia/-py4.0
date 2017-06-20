# eg.1
points = [{'x':2,'y':3},
          {'x':4,'y':1}]
points.sort(key=lambda i:i['y'])
print(points)

# eg.2
def make_repeater(n):
    return lambda s:s*n

twice = make_repeater(2)

print(twice('word'))
print(twice(5))