class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        hashset = set()
        for c in s:
            if c in hashset:
                count += 1
                hashset = set()
            hashset.add(c)
        
        return count
