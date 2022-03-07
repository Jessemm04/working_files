file_name = "text_files/plurals"

file = open(file_name)
contents = file.readlines()
vowel = {'a', 'e', 'i', 'o', 'u', 'y'}

for line in contents:
    contents = contents.pop(0)
    line.split(' ')
    num = int(line[0])
    item = line[1]
    if num == '0':
        num = 'no'
    elif num == '1':
        num = 'one'
    else:
        if item[-1] == ('s', 'x', 'z'):
            item = item + 'es'
        elif item[-2:] == ('eh', 'sh'):
            item = item + 'es'
        elif item[-1] == ('o' + item[-2] != vowel):
            item = item + 'es'
        elif item[-1] == 'y':
            item = item[0:-1] + 'ies'
        elif item[-2:] == 'fe' + item[-3] != 'f':
            item = item[0:-2] + 'ves'
        elif item[-1] + item[-2] != 'f':
            item = item[0:-1] + 'ves'
        else:
            item = item + 's'
    print(num + item)

