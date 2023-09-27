class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_A = set()
        set_B = set()
        common = 0
        res = []
        for i in range(len(A)):
            set_A.add(A[i])
            set_B.add(B[i])
            if A[i] in set_B:
                common += 1
            if B[i] in set_A:
                common += 1
            if A[i] == B[i]:
                common -= 1
            res.append(common)
        
        return res
