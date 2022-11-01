def heapif(arr,ind):
    left = 2*ind + 1 
    right =2*ind + 2 
    mx = ind 
    if(left<len(arr) and arr[left]>arr[ind]):
        mx = left 
    if(right<len(arr) and arr[mx]<arr[right]):
        mx = right
    if(ind==mx):
        return 
    arr[ind],arr[mx] = arr[mx],arr[ind]
    heapif(arr,mx)
def heap_pop(arr):
    arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
    del arr[-1]
    heapif(arr,0)
arr = [1,14,10,8,7,9,3,2,4,6]
heapif(arr,0)
print(arr)
heap_pop(arr)
print(arr)
heap_pop(arr)
print(arr)