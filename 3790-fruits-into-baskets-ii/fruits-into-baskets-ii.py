class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        

        n=len(baskets)
        count=0
        for f in fruits:
            unset=1

            for i in range(n):
                if f<=baskets[i]:
                    baskets[i]=0
                    unset=0
                    break
            
            count+=unset
        
        return count
