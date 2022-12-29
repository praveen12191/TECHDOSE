arr = [10,24,34,10,72,12]
lis = [0]*(50)
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
def build(start,end,seg_ind,lis,arr):
    if(start==end):
        lis[seg_ind] = arr[start]
        return 
    mid = start+(end-start)//2
    build(start,mid,seg_ind*2,lis,arr)
    build(mid+1,end,seg_ind*2+1,lis,arr)
    lis[seg_ind] = gcd(lis[seg_ind*2],lis[seg_ind*2+1])
def add(start,end,s_q,e_q,lis,arr,seg_ind):
    if(s_q>end or e_q<start):
        return 0 
    if(s_q<=start and e_q>=end):
        return lis[seg_ind]
    mid = start+(end-start)//2
    x = add(start,mid,s_q,e_q,lis,arr,seg_ind*2)
    y = add(mid+1,end,s_q,e_q,lis,arr,seg_ind*2+1)
    return gcd(x,y)
def update(start,end,s_q,e_q,lis,arr,seg_ind,val):
    if(s_q>end or e_q<start):
        return
    if(start==end):
        lis[seg_ind] = lis[seg_ind]*val
        return 
    mid = start+(end-start)//2
    update(start,mid,s_q,e_q,lis,arr,seg_ind*2,val)
    update(mid+1,end,s_q,e_q,lis,arr,seg_ind*2+1,val)
    lis[seg_ind] = lis[seg_ind*2]+lis[seg_ind*2+1]

build(0,5,1,lis,arr)
print(add(0,5,1,4,lis,arr,1))
update(0,5,1,4,lis,arr,1,2)
print(add(0,5,1,4,lis,arr,1))

