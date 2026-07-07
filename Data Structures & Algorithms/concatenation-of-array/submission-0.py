class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []

        for i in range(2*N):
            ans.append(nums[i%N])

        return ans