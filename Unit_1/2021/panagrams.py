file_name = "text_files/panagram_text"

file = open(file_name)
contents = file.readlines()
alpha = set(list('abcdefghijklmnopqrstuvwxyz'))
pangram = False

for line in contents:
    letters = {()}
    for char in line:
        if char.isalpha():
            letters.add(char)

        missing = alpha.difference(letters)

        if len(missing) == 0:
            print('This is a pangram')
        else:
            joined_string = ' '.join(missing)
            print('not a pangram. Does not contain:', joined_string.strip(' '))


    # if pangram == True:
    #     print('This is a pangram')
    # else:
    #     print('not a pangram. Does not contain:', missing)
