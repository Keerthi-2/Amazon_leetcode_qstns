class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp=[[0 for i in range(n)]for j in range(m)]
        for x,y in guards+walls:
            dp[x][y]=1
        
        di=[(0,1),(0,-1),(1,0),(-1,0)]
        for x,y in guards:
            for dx,dy in di:
                x1=x
                y1=y
                while(0<=(x1+dx)<m and 0<=(y1+dy)<n and dp[x1+dx][y1+dy]!=1):
                    x1+=dx
                    y1+=dy
                    dp[x1][y1]=2
            
        return sum(1 for i in range(m) for j in range(n) if dp[i][j]==0 )
    
                    
       # return sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0) 
        
        
                