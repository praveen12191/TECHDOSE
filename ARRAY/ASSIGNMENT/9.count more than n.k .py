#User function Template for python3
from collections import *

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k1):
        k = Counter(arr)
        ctr = 0
        ind = n//k1
        for x,y in k.items():
            if(y>ind):
                ctr+=1 
        return ctr
        
