import sys
time = int(input())
for i in range(time):
    a , b = map(int,sys.stdin.readline().split())
    print(a+b)
    
#input을 활용하여 a,b를 만들었지만 시간초과로 인해 실패하였다.
#검색을 통해 알아보니 블라인드 테스트,코딩 테스트와 같은 곳에서는 input이 시간이 오래걸려 sys를 활용하면 시간이 단축된다고 나와있다.
"""파이썬에서 데이터를 입력받을 때 input()을 이용한다. 
input()을 이용하면 프롬프트를 이용한 입력을 받을 수 있고, 형변환이 되는 이점이 있다. 
하지만 대량의 데이터를 반복적으로 입력받을 때 input()을 이용하지 않고, sys.stdin.readline() 을 이용하면 성능이 향상된다."""
#출처: https://118k.tistory.com/697 [개발자로 살아남기]
