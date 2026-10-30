
class Solution:
    def lastIndex(self, s):
        last = -1

        for i in range(len(s)):
            if s[i] == '1':
                last = i

        return last
s = input("Enter a binary string: ")

obj = Solution()
result = obj.lastIndex(s)

print("Last index of 1:", result)
