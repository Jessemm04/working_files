file_name = "text_files/results-1line.txt"

file = open(file_name)
contents = file.readlines()
grade = ' '
A = 0
B = 0
C = 0
fails = 0
for line in contents:
    line = line.strip()
    values = line.split(',')
    name = values[0]
    mark = int(values[1])
    if mark >= 80:
        grade = 'A'
        A +=1
    elif mark >= 70:
        grade = 'B'
        B += 1
    elif mark >=50:
        grade = 'C'
        C += 1
    else:
        grade = 'Fail'
        fails += 1
    print(name, 'got',grade)

print('A:',A)
print('B:', B)
print('C:', C)
print('Fails:', fails)





