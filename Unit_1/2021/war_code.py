code = str(input("Enter your coded message: "))
words = code.split(" ")
eng = " "
for w in words:
    if w[0].isupper():
        eng = eng + w + " "

print(eng.reversed().title())
