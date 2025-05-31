class SegmentTree:

    def __init__(self,nums):
        self.nums=nums
        self.n = len(self.nums)

        self.seg =  [0]*(4*self.n)
        self.build(0,0,self.n-1)

    def build(self,ind,left,right):
        if left == right:
            self.seg[ind] = self.nums[left]
            return
        mid = (left+right)//2

        self.build(2*ind+1,left,mid)
        self.build(2*ind+2,mid+1,right)

        self.seg[ind] = self.seg[2*ind+1]+self.seg[2*ind+2]
    
    def findSum(self,ind,low,high,l,r):
        if (l>high or r<low):
            return 0

        if(l<=low and r>=high):
            return self.seg[ind]
        mid = (low+high)//2
        left_sum = self.findSum(2*ind+1,low,mid,l,r)
        right_sum = self.findSum(2*ind+2,mid+1,high,l,r)
        return left_sum+right_sum
    
    def update(self,ind,low,high,pos,val):
        if(low==high):
            self.seg[ind] = val
            return
        
        mid = (low+high)//2
        if(pos<=mid):
            self.update(2*ind+1,low,mid,pos,val)
        else:
            self.update(2*ind+2,mid+1,high,pos,val)
        
        self.seg[ind] = self.seg[2*ind+1]+self.seg[2*ind+2]


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(self.nums)
        self.segmentTree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segmentTree.update(0,0,self.n-1,index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segmentTree.findSum(0,0,self.n-1,left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)