class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = [0] + nums
        N = len(nums)

        for i in range(N):
            idx = abs(nums[i])
            nums[idx] = -1 * abs(nums[idx])

        missingNums = []
        for i in range(1, N):
            if nums[i] > 0:
                missingNums.append(i)
        
        return missingNums