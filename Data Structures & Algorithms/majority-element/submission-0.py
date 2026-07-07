class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_count = 1
        maj_num = nums[0]
        for i in range(1, len(nums)):
            if maj_count + 1 == 1: maj_num = nums[i]
            maj_count += 1 if maj_num == nums[i] else -1

        return maj_num