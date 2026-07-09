class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Val = nums[0]

        I = 1 
        while I < len(nums):
            Val ^= nums[I]
            I += 1

        return Val
