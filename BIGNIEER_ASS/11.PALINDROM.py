s = input()
l = len(s)
for i in range(l//2):
    if(s[i]!=s[l-i-1]):
        print("NO")
        break 
else:
    print("YES")