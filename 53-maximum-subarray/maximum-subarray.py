class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        ans = float('-inf')
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            ans = max(ans,cur_sum)

            if cur_sum<0:
                
                
                cur_sum = 0
            
            
            
        return ans

            
        
        