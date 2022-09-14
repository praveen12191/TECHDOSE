row = int(input())
col = int(input())
lis = [list(map(int,input().split())) for i in range(row)]
for i in range(col):
    for j in range(row):
        print(lis[j][i],end=" ")
    print()