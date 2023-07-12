def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    for c in str1:
        if (c not in str2) or (len(str1) != len(str2)):
            return False
    return True
