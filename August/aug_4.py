class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        length = len(nums)
        subarray = []
        for i in range(length):
            for j in range(i,length):
                if i == j :
                    subarray.append(nums[j])
                else:
                    subarray.append(sum(nums[i:j])+nums[j])
        sorted_arr = sorted(subarray)
        return sum(sorted_arr[ left-1 : right]) % (10**9 + 7)

# obj = Solution()
# print(obj.rangeSum([1,2,3,4], 4, 1, 5))
