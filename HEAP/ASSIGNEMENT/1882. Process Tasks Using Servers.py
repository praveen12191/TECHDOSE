class Solution:
    def assignTasks(self, server: List[int], tasks: List[int]) -> List[int]:
        '''
         order the server by server size and index
         for each task need to update the server in has [pop from has and append in using(on process server) if has is empty and still task it to be perform we start poping in using and add in has 
         in some case len od task ne 10 but task might be 20,49,13 so insterd of using len we can use the task]
        '''
        has = [[i,j] for j,i in enumerate(server)]
        heapq.heapify(has)
        ans,using = [],[]
        t = 0 
        for i in range(len(tasks)):
            t = max(i,t)
            if(len(has)==0): #so serevr in process in [using]
                t = using[0][0]
            while(using and t>=using[0][0]): #if t is less so we can pop from using because its time get over
                a,b,c = heapq.heappop(using)
                heapq.heappush(has,[b,c])
            val,ind = heapq.heappop(has)
            ans.append(ind)
            heapq.heappush(using,[t+tasks[i],val,ind])
        return ans