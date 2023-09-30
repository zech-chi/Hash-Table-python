class Solution:
    def minOperations(self, nums: List[int]) -> int:
        Dict = {}
        for n in nums:
            if not n in Dict:
                Dict[n] = 0
            Dict[n] += 1
        
        count = 0
        for key, value in Dict.items():
            if value == 1:
                return -1
            while value:
                if value == 2:
                    count += 1
                    value -= 2
                elif value == 4:
                    count += 2
                    value -= 4
                else:
                    count += 1
                    value -= 3
        
        return count
