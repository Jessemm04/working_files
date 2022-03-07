file_name = 'text_files/luhn_alg'
file = open(file_name)
contents = file.readlines()
odd = ()
even = ()
msg = " "

class Luhn:
    def __init__(self):
        for i in range(line(len)):
            odd = ord(line[-1] - ord(line(2)))
            odd = odd.split('\n')
            even = ord(line[-2] - ord(line(2)))
            even = even.split('\n')
            esum = even * even
            if esum > 9:
                enum = esum.split('\n')
                e1 = enum[0]
                e2 = enum[1]
                esum = e1 + e2
            for i in range(even(len)):
                esum = esum + esum
            for x in range(odd(len)):
                osum = odd + odd
            for j in range(line(len)):
                sum = esum + osum
    def encode:
        if line[0] == 'E':
            msg = Luhn

    def valid:
        if Luhn % 10 == 0:
            msg = 'valid'
        else:
            msg = 'invalid'

print(msg)




