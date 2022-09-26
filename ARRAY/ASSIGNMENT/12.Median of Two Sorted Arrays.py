class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        ctr1,ctr2 = 0,0
        arr = []
        while(ctr1<l1 and ctr2<l2):
            if(nums1[ctr1]<nums2[ctr2]):
                arr.append(nums1[ctr1])
                ctr1+=1 
            else:
                arr.append(nums2[ctr2])
                ctr2+=1
        while(ctr1<l1):
            arr.append(nums1[ctr1])
            ctr1+=1
        while(ctr2<l2):
            arr.append(nums2[ctr2])
            ctr2+=1
        t1 = l1+l2 
        print(arr)
        if(t1%2==1):
            return arr[t1//2]
        else:
            v1 = arr[t1//2 -1]
            v2 = arr[t1//2]
            return (v1+v2)/2
            