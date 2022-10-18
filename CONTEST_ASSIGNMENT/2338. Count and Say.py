class Solution:
    def countAndSay(self, n: int) -> str:
        s = ""
        ctr = "1"
        for i in range(1,n):
            l = len(ctr)
            has = defaultdict(int)
            has[ctr[0]] = 1
            val = ""
            for i in range(1,l):
                if(ctr[i] in has):
                    has[ctr[i]]+=1 
                    if(i==l-1):
                        val = val + str(has[ctr[i]]) + ctr[i] 
                        del has[ctr[i]]
                else:
                    if(ctr[i-1] in has):
                        k = has[ctr[i-1]]
                        val = val + str(k) + ctr[i-1] 
                        del has[ctr[i-1]]
                    else:
                        val = val + "1" + ctr[i]
                    
                    has[ctr[i]] = 1
            if(ctr!="1"):
                for i,j in has.items():
                    val+=str(j)+i
            if(ctr=="1"):
                ctr = "11"
            else:
                ctr = val
        return ctr