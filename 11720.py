T = int(input())        #test케이스 숫자.
N = list(input())       #입력받은것들을 list화 함으로써 한글자씩 나눠지게 된다.
result = 0
for i in N:            #N의 리스트에 있는 글자들을 한개씩 i로 집어넣게 된다.
    result += int(i)        #type(i) = str 이므로 int(i)해야 result와 더할 수 있다.
print(result)
