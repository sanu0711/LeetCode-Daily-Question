class Solution:
    def minSwaps(self, nums) -> int:
        one_count = nums.count(1)
        max_count = count = sum(nums[:one_count])
        length = len(nums)
        for i in range(one_count, length + one_count):
            count += nums[i % length]
            count -= nums[(i - one_count + length) % length]
            max_count = max(max_count, count)
        return one_count - max_count
    
    
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/