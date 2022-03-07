# students = []
#
# students.append('Peter')
# students.append('Paul')
# students.append('Mary')
#
# print(type(students))
# print(students)
# print(students[1])
# print(len(students))
# print(students[-1])
#
# for students in students:
#     print(students)
#
# students.append('Jess')
# print(students)
# students.sort()
# print(students)
# students.reverse()
# print(students)
# students.pop()
# print(students)
# x = students.pop()
# print(x, students)
# students.remove('Peter')
# print(students)

##########################

new_students = ['Simon','Andrew','Martha','Andrea']
grades = [23, 45, 79, 32]

for i in range(len(new_students)):
    print(new_students[i], "got the grade", grades[i])


#create a list from a string
name = 'Jessica'
letters = list(name)
print(letters)

#create a list from splitting a string
name = 'Jessica Semmler'
name_parts = name.split()
print(name_parts)
first_name = name_parts[0]
last_name = name_parts[1]
print(last_name.upper(), first_name)