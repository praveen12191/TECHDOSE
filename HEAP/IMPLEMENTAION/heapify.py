def heapif(arr,ind):
    left = 2*ind + 1 
    right =2*ind + 2 
    '''
            1(0)
     14(1)         10(2)
    '''
    mx = ind 
    if(left<len(arr) and arr[left]>arr[ind]):
        mx = left 
    if(right<len(arr) and arr[mx]<arr[right]):
        mx = right
    if(ind==mx):
        return 
    arr[ind],arr[mx] = arr[mx],arr[ind]
    heapif(arr,mx)
arr = [1,14,10,8,7,9,3,2,4,6]
heapif(arr,0)
print(arr)
arr.pop(0)
heapif(arr,0)
print(arr)