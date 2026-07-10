class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currSum = nums[0]
        maxSum = nums[0]

        for val in nums[1:]:
            currSum = max(val, currSum + val)
            maxSum = max(maxSum, currSum)

        return maxSum        
        

