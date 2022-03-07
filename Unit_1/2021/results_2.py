file_name = "text_files/results.txt"

file = open(file_name)
contents = file.readlines()
grade = ' '
names = []
marks = []
A = 0
B = 0
C = 0
fails = 0
for l in range(1,len(contents)+1):
    if l % 2 == 0:
        marks.append(l)
    else:
        names.append(l)
    for l in range(len(names)):
        name = names[l]
        mark = marks[l]
        if mark >= 80:
            grade = 'A'
            A += 1
        elif mark >= 70:
            grade = 'B'
            B += 1
        elif mark >= 50:
            grade = 'C'
            C += 1
        else:
            grade = 'Fail'
            fails += 1
        print(name, 'got', grade)