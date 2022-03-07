file_name = "text_files/foldcipher"
file = open(file_name)
contents = file.readlines()

first_letter = ord(contents[0]) - 64
cipher = (first_letter % 3) + 3
num = (len(contents) // cipher) # = 23
across = len(contents)
clmsg = ""

if across % cipher == 0:
    num += 1

for i in range(num):

    for x in range(1, across):
        clmsg = (i + num)

print(clmsg)


