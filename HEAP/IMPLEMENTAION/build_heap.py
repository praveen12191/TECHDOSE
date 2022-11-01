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
arr = [3,6,5,0,8,2,1,9]
leaf = len(arr)//2 - 1
for i in range(leaf,-1,-1):
    heapif(arr,i)
print(arr)