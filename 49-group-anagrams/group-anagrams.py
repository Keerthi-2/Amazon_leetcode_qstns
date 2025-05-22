class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        d = {}

        for i in range(len(strs)):
            cur=''.join(sorted(strs[i]))

            if cur in d:
                d[cur].append(strs[i])
            else:
                d[cur] = [strs[i]]
        
        res = []
        for val in d.values():
            res.append(val)
        
        return res