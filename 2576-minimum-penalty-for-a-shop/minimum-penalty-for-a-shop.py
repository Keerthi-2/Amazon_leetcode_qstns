class Solution:
    # verygood question to solve and complete logic in o(n) time
    
    def bestClosingTime(self, cus: str) -> int:
        n=len(cus)
        y=0
        
        for i in cus:
            y+=(1 if i=='Y' else 0)
            
        min_p=n
        hour=n
        y_found=0
        n_found=0
        for h in range(0,n+1):
            
            y_remain=y-y_found
            pen=n_found+y_remain
            
            y_found+=(1 if h<n and cus[h]=='Y' else 0)
            n_found+=(1 if h<n and cus[h]=='N' else 0)
        
            if pen<min_p:
                min_p=pen
                hour=h
        
        return hour
            