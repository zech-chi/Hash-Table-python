class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        Dict = {}
        for pair in adjacentPairs:
            x, y = pair
            if not x in Dict:
                Dict[x] = []
            if not y in Dict:
                Dict[y] = []
            Dict[x].append(y)
            Dict[y].append(x)
        
        res = []
        visited = set()
        cur = None
        for x in Dict:
            if len(Dict[x]) == 1:
                cur = x
                break
          
        while (cur != None):
            res.append(cur)
            visited.add(cur)
            if not Dict[cur][0] in visited:
                cur = Dict[cur][0]
            elif len(Dict[cur]) == 2 and not Dict[cur][1] in visited:
                cur = Dict[cur][1]
            else:
                cur = None
        
        return res
