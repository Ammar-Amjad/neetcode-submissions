class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dic = {}
        for i in range(len(nums)):
            if nums[i] in idx_dic: return [idx_dic[nums[i]], i]  
            idx_dic[target - nums[i]] = i
        return -1