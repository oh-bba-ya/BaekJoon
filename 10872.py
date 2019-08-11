N = int(input())            #입력값
result = 1                  #1은 곱셈에 영향을 주지않으므로.
for i in range(1,N+1):      #반복문 범위를 통해 1~N까지 result에 차례대로 곱해준다.
    result *= i             #팩토리얼은 1~N까지 하든 N~1까지 하든 결과에 영향을 끼치지 않으므로 범위 순서는 상관없다.
print(result)


#반복문의 범위가 역순이여도 결과에 영향이 없다는것을 확인 할 수 있다.

N = int(input())            #입력값
result = 1                  #1은 곱셈에 영향을 주지않으므로.
for i in range(N,0,-1):      #반복문 범위를 통해 1~N까지 result에 차례대로 곱해준다.
    result *= i             #팩토리얼은 1~N까지 하든 N~1까지 하든 결과에 영향을 끼치지 않으므로 범위 순서는 상관없다.
print(result)
