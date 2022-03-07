#homework: find out how to loop through a dictionary to print the key and the value (e.g: 'Ronan is 17')
# keys = student_ages.keys()
# values = student_ages.values()

student_grades = {
    'Simon':45,
    'Lilly':60,
    'Jackson':78,
    'jamika':20,
    'Allison':90,
    'Colvet':94,
}



for key, values in student_grades.items():
    print(key, 'got', values)

#ask for a name and

name = str(input('Enter a name: '))
if name in student_grades:
    print(student_grades[name])
else:
    print('Name not found')

#print only keys
print(list(student_grades.keys()))

#print only values
print(list(student_grades.values()))

#sort dictionary accoding to student names
print(sorted(student_grades.keys()))
print(student_grades)

#sort dictionary according to grades
print(sorted(student_grades.values()))

#sort dictionary in reverse order of student names
print(list(reversed(sorted((student_grades.keys())))))