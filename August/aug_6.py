from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=Counter(word)
        sorted_list=sorted(freq.values(),reverse=True)
        length = len(sorted_list)
        s=0
        for i in range(length):
            s = s + ( sorted_list[i] * ((i//8) + 1))
        return s
# Time complexity: O(NlogN)
# Space complexity: O(N)