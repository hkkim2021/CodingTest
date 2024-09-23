#[21년 재직자 대회 예선] 이미지 프로세싱
dx=[-1, 0, 1, 0] #북->동->남->서 방향
dy=[0, 1, 0, -1]

h,w=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(h)]

k=int(input())
b = [list(map(int, input().split())) for _ in range(k)]

#런타임 에러 -> 파이썬은 재기함수 제한있음
#def change(x, y, before ,after):
#    if x<0 or x>=h or y<0 or y>=w:
#        return
#    if a[x][y] != before:
#        return
#    a[x][y]=after

#   for i in range(4):
#        change(x+dx[i], y+dy[i], before, after)

#stack을 이용한 DFS
def change(x,y, before, after):
    stack=[(x,y)]

    while stack:
        x,y=stack.pop()
        if x<0 or x>=h or y<0 or y>=w:
            continue
        if a[x][y]!=before:
            continue
        a[x][y]=after
        
        for i in range(4):
            nx, ny=x+dx[i],y+dy[i]
            stack.append((nx,ny))

for i in range(k):
    x=b[i][0]-1
    y=b[i][1]-1
    before=a[x][y] #현재 색상
    after=b[i][2] #바꿔야되는 색상
    if before !=after:
        change(x, y, before, after)


for row in a:
    print(' '.join(map(str, row)))


