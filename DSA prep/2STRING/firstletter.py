class Solution:
    def firstAlphabet(self, s):
        result = ""

        for i in range(len(s)):
            if i == 0 or s[i - 1] == " ":
                result += s[i]

        return result

s = input("Enter a string: ")

obj = Solution()
print("Result:", obj.firstAlphabet(s))