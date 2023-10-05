class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        s1 = Counter(word1)
        s2 = Counter(word2)
        s3 = Counter(s1.values())
        s4 = Counter(s2.values())

        for i in range(97, 123):
            c = chr(i)
            if c in s1 and not c in s2:
                return False
            if not c in s1 and c in s2:
                return False
        
        for k in s3:
            if not k in s4:
                return False
            if s4[k] != s3[k]:
                return False
            
        return True
