def cyclic_rotation(word, count_num):
    word = list(word)
    for x in range(count_num):
        word.insert(0, word.pop(-1))
    return ''.join(word)