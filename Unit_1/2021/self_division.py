file_name = "text_files/self_divi"
file = open(file_name)
contents = file.readlines()
for line in contents:
    line = line.split()
    begin = int(line[0])
    end = int(line[1])
    self_divi = 0
    divisible = True
    #for n in range(len(line)):
    for n in range(begin, end):
        x = str(n)
        h = str(end)
        d = int(end+1)
        if begin % d == 0:
            divisible = True
            #if len(x) > 0:

        else:
            divisible = False
        if divisible == True:
            self_divi += 1
    print(self_divi)
