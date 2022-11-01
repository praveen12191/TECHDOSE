def increse_key(arr,ind,key):
    while(ind>0 and arr[ind//2]<key):
        arr[ind//2],arr[ind] = key ,arr[ind//2]
        ind//=2 
arr = [9, 8, 5, 6, 3, 2, 1, 0]
increse_key(arr,4,40)
print(arr)

