class Solution:
    def find(self, txt, pat):
        n = len(txt)
        m = len(pat)

        for i in range(n - m + 1):
            if txt[i:i + m] == pat:
                return i

        return -1
obj = Solution()

print(obj.find("GeeksForGeeks", "Fr"))
print(obj.find("GeeksForGeeks", "For"))
print(obj.find("GeeksForGeeks", "gr"))    