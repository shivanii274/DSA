class Solution:
    def modify(self, s):
        result = ""

        for ch in s:
            if ch != " ":
                result += ch

        return result


s = input("Enter a string: ")

obj = Solution()
print("Result:", obj.modify(s))