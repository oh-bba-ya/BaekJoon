size = int(input())
for i in range(size):                #주어진 숫자만큼 반복
    a = list(map(int,input().split()))    #입력받은 숫자를 공백 기준으로 나누고 리스트
    print(sum(a))            #한번씩 반복될때마다 출력
