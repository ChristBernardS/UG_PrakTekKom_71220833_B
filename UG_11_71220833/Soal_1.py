print('select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide')
choice = int(input('Enter choice(1/2/3/4): '))
firstnumber = float(input('Enter first number: '))
secondnumber = float(input('Enter second number: '))


def Add():
    x, y = firstnumber, secondnumber
    addxy = x+y
    print(f'{x} + {y} = {addxy}')
    return addxy


def Substract():
    x, y = firstnumber, secondnumber
    substractxy = x-y
    print(f'{x} - {y} = {substractxy}')
    return substractxy


def Multiply():
    x, y = firstnumber, secondnumber
    multiplyxy = x*y
    print(f'{x} * {y} = {multiplyxy}')


def Divide():
    x, y = firstnumber, secondnumber
    dividexy = x/y
    print(f'{x} / {y} = {dividexy}')
    return dividexy


if choice == 1:
    Add()
elif choice == 2:
    Substract()
elif choice == 3:
    Multiply()
elif choice == 4:
    Divide()
else:
    ('Pilihan menu tidak tersedia\nUlangi program dan pilih (1/2/3/4)')
