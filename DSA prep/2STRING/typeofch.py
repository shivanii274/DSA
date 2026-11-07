def countCharacters(s):
    lower = 0
    upper = 0
    special = 0
    numeric = 0

    for ch in s:
        if ch.islower():
            lower += 1

        elif ch.isupper():
            upper += 1

        elif ch.isdigit():
            numeric += 1

        else:
            special += 1

    return [lower, upper, special, numeric]
s = input("Enter a string: ")
print(countCharacters(s))