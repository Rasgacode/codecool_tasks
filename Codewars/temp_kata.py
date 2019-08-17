import string

def duplicate_count(text):
    return len([x for x in set(text.lower()) if text.lower().count(x) > 1])


def sort_array(source_array):
    odds = iter(sorted(el for el in source_array if el % 2))
    return [next(odds) if el % 2 else el for el in source_array]

def rot13(message):
    alphabet = list(string.ascii_lowercase) * 2 + list(string.ascii_uppercase) * 2
    return "".join([alphabet[alphabet.index(x) + 13] for x in list(message)])


def iq_test(numbers):
    odd_or_even = ["o" if int(x) % 2 != 0 else "e" for x in numbers.split(' ')]
    return odd_or_even.index("o") + 1 if odd_or_even.count("o") == 1 else odd_or_even.index("e") + 1


def find_uniq(arr):
    return set(arr)[0] if arr.count(set(arr)[0]) == 1 else set(arr)[1]


def countBits(n):
    return list(format(n, "b")).count(1)

print(list(format(10, "b")).count("1"))

