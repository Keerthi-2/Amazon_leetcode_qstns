from heapq import heapify,heappush,heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key=lambda x:x[1])
        heap=[]

        max_day = 0

        for day,endDay in courses:
            max_day += day
            heappush(heap,-1*day)

            if(max_day>endDay):
                max_day-=-1*heappop(heap)
                
        return len(heap)
        