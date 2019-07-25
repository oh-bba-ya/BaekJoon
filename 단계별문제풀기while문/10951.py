#만일 break를 쓰지않는다면 런타임 에러가 나온다.
#따로 종료되는 지점이 없기때문에 try로 정수만을 입력받아 더하고 만일 다른 정수외의 것이 나오면 종료가 된다.
while True:
    try:
        A , B = map(int,input().split())
        print(A+B)
    except:
        break
        
