class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        Dict = {}
        for n in nums:
            if not n in Dict:
                Dict[n] = 0
            Dict[n] += 1

        Max = 1
        for n in Dict:
            Max = max(Max, Dict[n])
        
        output = [[] for _ in range(Max)]
        for k, v in Dict.items():
            for i in range(v):
                output[i].append(k)
                
        return output
