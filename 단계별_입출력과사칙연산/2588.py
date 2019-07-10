#입력으로 주는 3자리수 2개가 줄로 나뉘어져서 주어지기 때문에 인풋을 2줄로

Num = []
Num.append(int(input()))
Num.append(int(input()))
A = Num[0]
B = Num[1]
B = str(B)            #slicing 사용하기 위해 string
result = A*int(B[2])
result2 = A*(int(B[1])*10)
result3 = A*(int(B[0])*100)
result4 = result+result2+result3
print(result)
print(A*int(B[1]))
print(A*int(B[0]))
print(result4)
