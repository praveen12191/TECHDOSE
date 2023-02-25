def heap(arr,ind):
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
    heap(arr,mx)
def heapify(arr):
    l = len(arr)
    ind = l//2 - 1 
    for i in range(ind,-1,-1):
        heap(arr,i)
def heap_pop(arr):
    arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
    del arr[-1]
    heap(arr,0)
arr = [1,10,4,2,8,5,20,54]
heapify(arr)
print(arr)
# heap_pop(arr)
# print(arr)
# heap_pop(arr)
# print(arr)