largest = None
smallest = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print('Invalid input')
        continue

    if largest is None :
        largest = int(fval)
    elif fval > largest :
        largest = int(fval)

    if smallest is None :
        smallest = int(fval)
    elif fval < smallest :
        smallest = int(fval)

print('Maximum', largest)
print('Minimum', smallest)