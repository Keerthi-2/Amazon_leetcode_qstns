from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g=defaultdict(list)
        ind=[0]*(numCourses)
        for i,j in prerequisites:
            g[i].append(j)
            ind[j]+=1

        q=[]
        for i,val in enumerate(ind):
            if val==0:
                q.append(i)

        numberofnodesvis = 0
        while(q):
            cur=q.pop(0)
            numberofnodesvis += 1
            for neigh in g[cur]:
                ind[neigh]-=1
                if ind[neigh]==0:
                    q.append(neigh)
            

        return numberofnodesvis==numCourses


        