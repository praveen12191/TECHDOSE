s = input()
has = [0]*123 
for i in s:
    has[ord(i)]+=1 
for i in range(123):
    if(has[i]!=0):
        print("frequency of {} is {}".format(chr(i),has[i]))