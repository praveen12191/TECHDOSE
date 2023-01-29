from collections import defaultdict
adj = [[0,4,6,0,0,0],[4,0,6,3,4,0],[6,6,0,1,0,0],[0,3,1,0,2,3],[0,4,0,2,0,7],[0,0,0,3,7,0]]
for i in adj:
    print(i)
adj_list = defaultdict(list)
for i in range(6):
    for j in range(6):
        if(adj[i][j]!=0):
            if([j,adj[i][j]] not in adj_list[i]):
                adj_list[i].append([j,adj[i][j]])
            if([i,adj[i][j]] not in adj_list[j]):
                adj_list[j].append([i,adj[i][j]])
print(adj_list)
no_nodes = len(adj)
weight = [float('inf')]*no_nodes
weight[0] = 0 
parent = [-1]*no_nodes
set_mst = [0]*no_nodes
for i in range(5):
    ind = 0 
    mn = float('inf')
    for i in range(6):
        if(mn>weight[i] and set_mst[i]==0):
            mn = weight[i]
            ind = i 
    set_mst[ind] = 1
    for i in range(6):
        if(adj[ind][i]!=0 and set_mst[i]==0):
            weight[i] = min(weight[i],adj[ind][i])
            parent[i] = ind 
# while(f):
#     mn = float('inf')
#     ind = 0 
#     for i in range(6):
#         if(mn>weight[i] and set_mst[i]==0):
#             mn = weight[i]
#             ind = i 
#     print(ind)
#     set_mst[ind] = 1 
#     for x,y in adj_list[ind]:
#         weight[x] = min(weight[x],y)
#         parent[x] = ind
#     k = 0 
#     for i in set_mst:
#         if(i==0):
#             k = 1
#             break 
#     if(k==0):
#         f = 0 
# print(set_mst)
for i in range(6):
    print("{}-->{} = {}".format(i,parent[i],weight[i]))