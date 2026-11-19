from collections import Counter

class Solution:
    def secFrequent(self, arr):
        freq = Counter(arr)

        frequencies = sorted(set(freq.values()), reverse=True)

        if len(frequencies) < 2:
            return -1

        return frequencies[1]


arr = input("Enter strings separated by space: ").split()

obj = Solution()
print(obj.secFrequent(arr))