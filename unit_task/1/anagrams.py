def is_anagram(a, b):
    if any(x.isdigit() for x in list(str(a)) + list(str(b))):
        return False
    return sorted(a) == sorted(b)