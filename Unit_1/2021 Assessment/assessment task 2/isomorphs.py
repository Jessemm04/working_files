file_name = "isomorphic_words"

file = open(file_name)
contents = file.readlines()
isomorph = False


def iso_checker(words):
    for words in contents:
        words.split(' ')
        w1 = words[1]
        w2 = words[2]

        found = False
        code1 = " "
        code2 = " "
        if len(w1) == len(w2):
            for i in range(0, (len(w1))):
                for x in range(i + 1):
                    for j in range(i + 1):
                        while j < len(w1) and found is False:
                            if w1[x] == w1[j]:
                                found = True
                                pos = x - i
                                pos = str(pos)
                                code1 += pos
                                code2 += pos
                                if code1 == code2:
                                    isomorph = True
                                else:
                                    isomorph = False

                            else:
                                found = False
                                code1 += '0'
                                code2 += '0'

                            if found is False:
                                print(words, 'are not isomorphs')
                            else:
                                print(words, "are isomorphs with repetition pattern:", code1)
                        j += 1
        else:
            print(words, 'have different lengths')


for words in contents:
    words.split(' ')
    w1 = words[0]
    w2 = words[1]

    print(iso_checker(words))