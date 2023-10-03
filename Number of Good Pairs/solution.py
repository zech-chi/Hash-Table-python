class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        Dict = {}
        for n in nums:
            if not n in Dict:
                Dict[n] = 0
            Dict[n] += 1
        
        count = 0
        for k, v in Dict.items():
            count += (v * (v - 1)) // 2

        return count
