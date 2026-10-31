class Solution:
    def concatenatedString(self, s1, s2):
        set1 = set(s1)
        set2 = set(s2)

        result = ""

        for ch in s1:
            if ch not in set2:
                result += ch

        for ch in s2:
            if ch not in set1:
                result += ch

        return result if result else "-1"
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

obj = Solution()
print("Result:", obj.concatenatedString(s1, s2))