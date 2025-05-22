class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #bucket approach for top k freq elemets

        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        
        bucket = [[] for i in range(len(nums)+1)]

        for val,freq in d.items():
            bucket[freq].append(val)
        
        res = []
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res
        
        return []

        
        



        return sortedD[:k]