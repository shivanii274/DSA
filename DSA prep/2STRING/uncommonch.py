class Solution:
    def uncommonChars(self, s1, s2):
        result = set(s1) ^ set(s2)
        return ''.join(sorted(result))


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

obj = Solution()
print(obj.uncommonChars(s1, s2))