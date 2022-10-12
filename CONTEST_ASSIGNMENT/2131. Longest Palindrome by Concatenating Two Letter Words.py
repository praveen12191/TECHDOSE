class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ctr = 0 
        lis = []
        l = len(words)
        count = Counter(words)
        f = 0
        total = 0
        for i,j in count.items():
            if(i[0]==i[1]):
                total+=j//2
                if(j%2==1):
                    f = 1
            else:
                ctr+= min(count[i[::-1]],count[i])
        print(ctr)
        return ((ctr*2)+(total*4)+(f*2))