def build_heap(arr,l):
    leaf = len(arr)//2 - 1 
    for i in range(leaf,-1,-1):
        heapif(arr,i,l)
def heapif(arr,ind,l):
    mn = ind 
    left,right = ind*2 + 1,ind*2 + 2 
    if(left<l and arr[left]<arr[ind]):
        mn = left 
    if(right<l and arr[right]<arr[mn]):
        mn = right 
    if(mn==ind):
        return 
    arr[mn],arr[ind] = arr[ind],arr[mn]
    heapif(arr,mn,l)
def heap_sort(arr,l):
    while(l):
        build_heap(arr,l)
        arr[0],arr[l-1] = arr[l-1],arr[0]
        l-=1 
arr = [1,14,10,8,7,9,3,2,4,6]
l = len(arr)
heap_sort(arr,l)
print(arr)