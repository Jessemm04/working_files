file_name = 'text_files/murlin_url'
file = open(file_name)
contents = file.readlines()

class Hex(object):
    def __init__(self):
        value = {'o':0, 'f':15}
        value = value.lower()
        total = value[0] * 16 + value[1]
        ascii_char = chr(total)
        return


for URL in contents:
    URL = URL.split('\n')
    x = 0
    decode = " "
    while x < len(URL):
        char = URL[x]
        if char = '%':
            hexdeci = URL[x + 1:x + 3]
            char = Hex(hexdeci)
            x = x + 3
        else:
            x = x + 1
        decode += char
    print(decode)