class Solution:
    def removeVowels(self, s):
        vowels = "aeiouAEIOU"
        result = ""

        for ch in s:
            if ch not in vowels:
                result += ch

        return result

s = input("Enter a string: ")

obj = Solution()
print("Result:", obj.removeVowels(s))