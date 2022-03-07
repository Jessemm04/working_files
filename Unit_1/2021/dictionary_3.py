#ask user to enter a sentence. count each number of each word in the sentence.
#for e.g:
#the quick brown fox jumped over the lazy fox which was also brown due to the brown rain
words = {}
sentence = str(input('Enter a sentence: ').lower())
word_list = sentence.split()
for word in word_list:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for k, v in words.items():
    print(k, 'appears in sentence', v, 'times.')
