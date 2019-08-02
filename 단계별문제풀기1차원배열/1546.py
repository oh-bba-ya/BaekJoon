count = int(input())
num = list(map(int,input().split()))
result = 0
for i in range(count):                #반복문을 통해 모든 점수를 합했다. 굳이 반복문 말고 sum을 활용해도 된다.
    result += num[i]
result = (result / max(num) * 100)/count        #(모든 점수를 합한 result / 제일높은 점수 * 100) / 과목개수
print('%.2f'%result)            #소수점 2자리까지 표시
