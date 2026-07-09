class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        currSum = 0
        minSize = float('inf')

        while r < len(nums):
            currSum += nums[r] 
            while currSum >= target:
                minSize = min(minSize, r - l + 1)
                currSum -= nums[l]
                l += 1
            r += 1
            

        return 0 if minSize == float('inf') else minSize