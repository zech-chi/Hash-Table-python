class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hashset = set(n for n in range(1, k + 1))
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in hashset:
                hashset.remove(nums[i])
            count += 1
            if hashset == set():
                return (count)
