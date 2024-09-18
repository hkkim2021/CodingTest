#[21년 재직자 대회 예선] 회의실 예약(level2)
n,m=map(int, input().split())

a=[input() for _ in range(n)]#회의실 입력
#a=[list(map(str, input().split())) for _ in range(n)] 
a.sort() #회의실 오름차순 정렬

#각 회의실의 전체 시간대
#모든 회의실에 대해 9시부터 18시까지 가능으로 놓는다.
t=[[1]*9 for _ in range(n)]

for i in range(m):
    name, start, end=input().split()
    start=int(start)
    end=int(end)
    for j in range(n):
        if str(name)==a[j]:
            for k in range(start-9, end-9):
                t[j][k]=0


for i in  range(n):
    sum=0
    print('Room '+ a[i]+':')
    available_times=[]
    j=0

    while j<9:
        if t[i][j]==1:
            start_time=j
            while j<9 and t[i][j]==1:
                j+=1
            end_time=j
            available_times.append(f'{start_time+9:02d}-{end_time+9:02d}')
        else:
            j+=1

    if available_times:
        print(len(available_times), "available")
        for time_range in available_times:
            print(time_range)
    else:
        print('Not available')
    print('-----')
