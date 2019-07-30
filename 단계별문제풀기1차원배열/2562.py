result = []
for i in range(9):          #반복문을 통해 입력값 받기.
    num = int(input())          
    result.append(num)      #입력값을 리스트에 추가 함으로써 max,index사용.
max_result = max(result)
index_result = int(result.index(max_result))+1
print(max_result)
print(index_result)
