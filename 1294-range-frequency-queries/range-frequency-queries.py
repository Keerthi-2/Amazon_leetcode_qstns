class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d ={}
        for i in range(len(arr)):
            if arr[i] not in self.d:
                self.d[arr[i]]=[i]
            else:
                self.d[arr[i]].append(i)
            

    def query(self, left: int, right: int, value: int) -> int:
        if value in self.d:
            l = bisect_left(self.d[value],left)
            r = bisect_right(self.d[value],right)
            return r-l
        else:
            return 0
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)