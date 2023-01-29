class Solution:
    def uniqueLetterString(self, s: str) -> int:
        '''
        ABCAKLU
        0123456
        for A 
        we have 2 A[0,3]
        with A as uniqu we can form 
        1*(0 to 2) 1) left A right ABC till next A
        (1 to 2)*(4,6) left BC right KLU 

        '''
        has = defaultdict(list)
        sm = 0 
        for i in ascii_uppercase:
            has[i].append(-1)
        for i in range(len(s)):
            has[s[i]].append(i)
        for i in ascii_uppercase:
            has[i].append(len(s))
        for j in ascii_uppercase:
            k = has[j]
            for i in range(1,len(k)-1):
                sm+=((k[i]-k[i-1])*(k[i+1]-k[i]))
        return sm