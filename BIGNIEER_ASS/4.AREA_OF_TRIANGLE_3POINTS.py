x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
'''
| x1 y1 1 |
| x2 y2 1 |
| x3 y3 1 | 
1/2 * x1(y2-y3) - x2(y1-y3) + x3(y1-y2)

'''
print(0.5 * abs((x1*(y2-y3) - x2*(y1-y3) + x3*(y1-y2))))