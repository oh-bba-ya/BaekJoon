#반복문을 한개만 쓰고 일일히 출력함.
A = int(input())
B = int(input())
C = int(input())
N = A * B * C
result = []
for i in range(len(str(N))):
    result.append(str(N)[i])
print(result.count('0'))
print(result.count('1'))
print(result.count('2'))
print(result.count('3'))
print(result.count('4'))
print(result.count('5'))
print(result.count('6'))
print(result.count('7'))
print(result.count('8'))
print(result.count('9'))


#출력을 반복문으로.
A = int(input())
B = int(input())
C = int(input())
N = A * B * C
N = str(N)
for i in range(10):
    print(N.count(str(i)))
