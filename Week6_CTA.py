a = year = input('Year: ')
b = make = input('Make: ')
c = model = input('Model: ')
d = color = input('Color: ')
e = mileage = input('Mileage: ')


class auto:
    def __init__(self, year, make, model, color, mileage):
        print(year)
        print(make)
        print(model)
        print(color)
        print(mileage)


print(a, b, c, d, e)

add_feat = (input('Add a feature? '))

if add_feat == ('yes'):
    a = input('Year: ')
    b = input('Make: ')
    c = input('Model: ')
    d = input('Color: ')
    e = input('Mileage: ')
    print(a, b, c, d, e)

restart = input('Add another vehicle? ')

if add_feat == ('no'):
    print(restart)
if restart == ('yes'):
    print(a, b, c, d, e)
if restart == ('no'):
    input('Press <enter> to Continue')
else:
    a = input('Year: ')
    b = input('Make: ')
    c = input('Model: ')
    d = input('Color: ')
    e = input('Mileage: ')

print(a, b, c, d, e)
input('Press <enter> to Exit')
