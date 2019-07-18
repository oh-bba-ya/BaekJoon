time = int(input())
for x in range(1,time+1):
    A , B = map(int,input().split())
    i = A + B
    print("Case #%d: %d" %(x,i))
