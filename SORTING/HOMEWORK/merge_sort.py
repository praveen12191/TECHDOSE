def merge_sort(lis,l):
    if(l==1):
        return
    mid = l//2 
    arr1 = lis[0:mid]
    arr2 = lis[mid::]
    merge_sort(arr1,mid)
    merge_sort(arr2,l-mid)
    merge(arr1,arr2,lis)
def merge(arr1,arr2,newarr):
    l1 = len(arr1)
    l2 = len(arr2)
    ctr1 = ctr2 = ptr = 0 
    while(ctr1<l1 and ctr2<l2):
        if(arr1[ctr1] < arr2[ctr2]):
            newarr[ptr] = arr1[ctr1]
            ptr+=1
            ctr1+=1
        else:
            newarr[ptr] = arr2[ctr2]
            ptr+=1
            ctr2+=1
    '''
        [3,6,8]  [10]
        after 1st while [3,10] but we have 6 and 8 so ..
    '''
    while(ctr1<l1):
        newarr[ptr] = arr1[ctr1]
        ctr1+=1 
        ptr+=1 
    while(ctr2<l2):
        newarr[ptr] = arr2[ctr2]
        ctr2+=1 
        ptr+=1
lis  = list(map(int,input().split()))
merge_sort(lis,len(lis))
print(lis)