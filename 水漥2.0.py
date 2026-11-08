N,M=input().split()
N=int(N)
M=int(M)
grid=[]
for i in range(N):
    grid.append(list(input()))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


pond={}
pond_count=0
for i in range(N):
    for j in range(M):
        if grid[i][j]=="W":
            pond_count+=1
            pond[pond_count]=[]
            pond[pond_count].append((i,j))
            for dx,dy in directions:
                ni,nj = i+dx,j+dy
                if 0<=ni<N and 0<=nj<M and grid[ni][nj]=="W":
                    pond[pond_count].append((ni,nj))
                else:continue
        else:continue

while True:
    changed = False
    for key1,value1 in list(pond.items()):
        for key2,value2 in list(pond.items()):
            if key1==key2:continue
            if key1 not in pond or key2 not in pond:continue
            merged = False
            for (x1,y1) in value1:
                for (x2,y2) in value2:
                    if x1==x2 and y1==y2:
                        if key1 < key2:
                            pond[key2].extend(value1)
                            del pond[key1]
                        else:
                            pond[key1].extend(value2)
                            del pond[key2]
                        changed =True
                        merged =True
                        break
                if merged:break
            if merged: break
        if changed: break
    if not changed: break


for a,b in pond.items():
    new_list = []
    for c in b:
        if c not in new_list:
            new_list.append(c)
    pond[a]=new_list


print(pond)
print(len(max(pond.values(),key=len)))
print(len(min(pond.values(),key=len)))
print(len(pond.keys()))