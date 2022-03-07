file_name = "text_files/casting9s"

file = open(file_name)
contents = file.readlines()

for line in contents:
    line = line.strip('\n')
    castout = 0
    for n in line:
        castout += int(n)
        if castout >= 9:
            castout = castout - 9

    print(castout)