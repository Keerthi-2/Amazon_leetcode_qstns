class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        d={}
        for char in t:
            d[char] = d.get(char,0)+1

        ans=10**9+7
        #Assuming for t if we have it all
        n=len(s)
        start=0
        end=n

        i=0
        j=0
        n=len(s)
        distinct = len(d)
        while(j<n):
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    distinct-=1
                
                while(distinct == 0):
                    if((j-i+1)<(end-start+1)):
                        start=i
                        end=j
                    
                    if(s[i] in d):
                        d[s[i]]+=1

                        if d[s[i]]==1:
                            distinct+=1
                    
                    i+=1
            j+=1
        
        if end==n:
            return ""
        
        return s[start:end+1]

