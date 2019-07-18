time = int(input())
for x in range(1,time+1):            #반복문의 range의 기본설정은 range(time)일경우 0~time-1이다.
    A , B = map(int,input().split())
    i = A + B
    print("Case #%d: %d + %d = %d" %(x,A,B,i))
