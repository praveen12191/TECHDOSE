def heapif(arr,ind):
    mx = ind 
    left,right = ind*2 +1,ind*2 +2
    if(left<len(arr) and arr[left]>arr[ind]):
        mx = left 
    if(right<len(arr) and arr[right]>arr[mx]):
        mx = right 
    if(mx==ind):
        return 
    arr[mx],arr[ind] = arr[ind],arr[mx]
    heapif(arr,mx)
def decrese_key(arr,ind,key):
    arr[ind]-=key 
    heapif(arr,ind)
arr = [40, 9, 8, 6, 5, 2, 1, 0]
decrese_key(arr,3,20)
print(arr)