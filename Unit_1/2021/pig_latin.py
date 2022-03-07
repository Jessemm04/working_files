#Q.35
eng = str(input("Enter a word you wish to convert to pig latin: "))
words = eng.split(" ")
pig_latin = " "
for w in words:
    if len(w) == 0:
        latin = w + 'ay'
    else:
        latin = w[1:] + w[0] + 'ay'
        pig_latin = pig_latin + latin + " "
    print(pig_latin.upper())