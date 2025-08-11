class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        

        mod = 10**9+7

        bins,rep = [],1

        while(n>0):
            if n%2==1:
                bins.append(rep)
            n//=2
            rep*=2

        
        ans=[]
        
        m=len(bins)
        mat=[[0 for i in range(m)]for j in range(m)]

        for i in range(m):
            cur=1
            for j in range(i,m):
                cur*=bins[j]
                mat[i][j]=(cur%mod)
        
        for i in queries:
            x=i[0]
            y=i[1]
            
            ans.append(mat[x][y])


        
        return ans