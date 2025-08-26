class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        def diaglength(x,y):
            return (x*x+y*y)
        

        res=-1
        diag=-1
        for i,j in dimensions:
            leng = diaglength(i,j)

            if leng>diag:
                diag=leng
                res=i*j
            elif leng==diag:
                res=max(res,i*j)
        
        return res


