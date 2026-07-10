class Solution:
    def countBits(self, N: int) -> List[int]:
        if N == 0: return [0]

        Res = [0,1]    
        pSS = 1
        while len(Res) < N + 1: 
            Next = Res[-pSS:] + [i + 1 for i in Res[-pSS:]]
            Res += Next
            pSS = len(Next)

        return Res[:N+1]


        # TC: O(n)
        # SC: O(n)
