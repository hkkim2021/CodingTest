#백준 14503_로봇청소기 
n,m=map(int, input().split())
x,y,dir=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int, input().split())))
#a=list(map(int,input().split())) for _ in range(n)

dx=[-1, 0, 1, 0]
dy=[0,1,0,-1]

#a[x][y]==0 청소하지 않은 공간
#a[x][y]==1 벽
#a[x][y]==2 청소한 공간

while True:
    if a[x][y]==0:
        a[x][y]=2

    #4방향이 다 청소가 되어 있거나 벽인 경우
    if a[x-1][y] !=0 and a[x+1][y] !=0 and a[x][y-1] !=0 and a[x][y+1] !=0 :
        #뒤로 후진도 할 수 없는 경우
        if a[x-dx[dir]][y-dy[dir]]==1:
            break
        #뒤로 후진은 할 수 있는 경우
        else:
            x-=dx[dir]
            y-=dy[dir]

    #4방향중 청소할 공간이 있다면
    else:
        dir=(dir+3)%4
        if a[x+dx[dir]][y+dy[dir]]==0:
            x+=dx[dir]
            y+=dy[dir]

cnt=0
for i in range(n):
    for j in range(m):
        if a[i][j]==2:
            cnt+=1

print(cnt)