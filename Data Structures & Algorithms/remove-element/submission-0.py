class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            while i <= j and nums[j] == val:
                j -= 1
            while i <= j and nums[i] != val:
                i += 1
                
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        return j + 1