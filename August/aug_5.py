class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        distinct_element = [i for i in arr if arr.count(i) == 1]
        if k > len(distinct_element):
            return ""
        else:
            return distinct_element[k-1]