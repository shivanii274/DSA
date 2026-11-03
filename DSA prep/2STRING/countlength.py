class length():
    def letters(self, s):
        count = 0
        for ch in s:
            count += 1
        return count
s = input("enter the string:")
obj = length()
print("result:", obj.letters(s))       