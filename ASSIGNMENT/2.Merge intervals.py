class Solution:
    def merge(self, lis: List[List[int]]) -> List[List[int]]:
        lis.sort()
        k1 = []
        for i in lis:
            if(not k1 or k1[-1][-1]<i[0]):
                k1.append(i)
            else:
                k1[-1][-1] = max(k1[-1][-1],i[1])
        return k1
        '''
        [1,3],[2,6],[4,8],[10,20]
        1st k1 = [1,3]
        2nd else: 3 = max(3,6)->[1,6]
        3rd else: 6 = max(6,8)->[1,8]
        4th [1,8],[10,20]
        '''