class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # lis = [0]
        # for i in arr:
        #     lis.append(lis[-1]^i)
        # ans = []
        # for x,y in queries:
        #     ans.append(lis[x]^lis[y+1])
        # return ans
        lis = [0]*(len(arr)*4+1)
        def build(seg_ind,start,end):
            if(start==end):
                lis[seg_ind] = arr[start]
                return 
            mid = start+(end-start)//2
            build(seg_ind*2,start,mid)
            build(seg_ind*2+1,mid+1,end)
            lis[seg_ind] = lis[seg_ind*2]^lis[seg_ind*2+1]
        def get(start,end,qs,qe,seg_ind):
            if(qs>end or qe<start):
                return 0 
            if(qs<=start and qe>=end):
                return lis[seg_ind]
            mid = start+(end-start)//2
            x = get(start,mid,qs,qe,seg_ind*2)
            y = get(mid+1,end,qs,qe,seg_ind*2+1)
            return x^y
        build(1,0,len(arr)-1)
        ans = []
        for x,y in queries:
            ans.append(get(0,len(arr)-1,x,y,1))
        return ans
