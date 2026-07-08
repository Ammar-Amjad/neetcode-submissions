from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        
        maxHeap = []
        for key, count in freq.items():
            maxHeap.append((-count, key))

        heapq.heapify(maxHeap)

        res = []
        while k > 0:
            if maxHeap == []: break
            count, key = heapq.heappop(maxHeap)
            res.append(key)
            k -= 1
        
        return res