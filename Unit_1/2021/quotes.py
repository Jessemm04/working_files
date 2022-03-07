import random
file_name = "text_files/quotes.txt"
file = open(file_name)
contents = file.readlines()

print(type(contents))
print(len(contents))

quote = random.choice(contents).strip()
print(quote)