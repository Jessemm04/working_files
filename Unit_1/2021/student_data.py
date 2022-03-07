# for each person, produce the number of marks they receive
# and what their average mark was
# write an algorithm for it
# upload algorithm
import statistics

file_name = "text_files/studentdata.txt"

file = open(file_name)
contents = file.readlines()
marks = []
names = []

for line in contents:
    line = line.strip()
    values = line.split(',')
    names = values[0]
    marks = int(values[1:len])
    for i in marks:
        marks = marks.isdigit()
    for m in marks:
        average = statistics.mean(marks)
print(names, "got", len(marks))
print(names, 'got an average mark of', average)
