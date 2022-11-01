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
def push(arr,val):
    arr.append(val)
    l = len(arr)
    leaf = l//2 - 1 
    for i in range(leaf,-1,-1):
        heapif(arr,i)

arr = [40, 9, 8, 6, 5, 2, 1, 0]
push(arr,-1)
print(arr)