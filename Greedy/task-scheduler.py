import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap=[]
        count=Counter(tasks)
        for ele in count:
            heapq.heappush(heap,[-count[ele],ele])
        res=0
        while heap:
            p=n
            res+=1
            most=heapq.heappop(heap)
            cur=[most[1]]
            while p>0 and heap:
                most=heapq.heappop(heap)
                cur.append(most[1])
                p-=1
                res+=1
            while p>0 and len(cur)!=0:
                res+=1
                p-=1
            added=False
            for ele in cur:
                count[ele]-=1
                if count[ele]!=0:
                    heapq.heappush(heap,[-count[ele],ele])
                    added=True
            if added==False:
                res-=(n+1-len(cur))
        return res



