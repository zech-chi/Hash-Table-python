class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Dict = {}
        for n in nums:
            if not n in Dict:
                Dict[n] = 0
            Dict[n] += 1
        
        ans = []
        c = len(nums) // 3
        for k, v in Dict.items():
            if v > c:
                ans.append(k)
        
        return ans
