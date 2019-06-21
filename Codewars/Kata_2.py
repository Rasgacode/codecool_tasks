sentence = 'lol mekkora szar vagy'
def spin_words(sentence):
    l = sentence.split(' ')
    print(l)
    for x in range(len(l)):
        if len(l[x])>=5:
            l[x] = ''.join(reversed(l[x]))
    sentence = ' '.join(l)
    return sentence