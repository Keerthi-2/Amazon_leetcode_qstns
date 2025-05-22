class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        d={}

        for i in s:
            d[i] = d.get(i,0)+1
        
        d1 = {}
        for i in t:
            d1[i] = d1.get(i,0)+1

        for i in range(len(s)):
            if s[i] in d and s[i] in d1:
                if d1[s[i]] != d[s[i]]:
                    return False
            else:
                return False
            
        return True
            
      