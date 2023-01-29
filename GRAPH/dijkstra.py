def find_min(dis,vis):
    m = float('inf')
    l = len(dis)
    for i in range(l):
        if(dis[i]<m and vis[i]==False):
            m = dis[i] 
            val = i
    return val

def prims(mat,n,start,parent):
    parent = [float('inf') for i in (n)]
    distance = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    distance[start] = 0
    parent[0] = -1
    for i in range(n-1):
        val = find_min(distance,visited)#min node
        visited[val] = True
        for j in range(n):
            if(mat[val][j]!=0 and visited[j]==False and (distance[val]+mat[val][j]<distance[j])):
                distance[j] = mat[val][j]
                parent[j] = val 
    print(distance)

no_of_nodes = int(input())
mat=[]
for i in range(no_of_nodes):
    k = list(map(int,input().split()))
    mat.append(k)
start = int(input())
prims(mat,no_of_nodes,start)
