names = []

enter_name = str(input('Enter a name or quit: ').strip())
while enter_name.lower() != 'quit':
    if enter_name.title() not in names:
        names.append(enter_name.title())
    else:
        print('That name already exists.')
    enter_name = str(input('Enter a name nor quit: ').strip())

if len(names) > 0:
    names.sort()
    for n in names:
        print(n)
else:
    print('There are no names to output')