#단순하게 입력값을 10개 받아서 하는방법.

A =int(input())
B =int(input())
C =int(input())
D =int(input())
E =int(input())
F =int(input())
G =int(input())
H =int(input())
I =int(input())
J =int(input())
result = []
result2 = []
result.append(A)
result.append(B)
result.append(C)
result.append(D)
result.append(E)
result.append(F)
result.append(G)
result.append(H)
result.append(I)
result.append(J)
for i in result:
    N = i % 42
    result2.append(N)
s2=set(result2)
print(len(s2))


#반복문과 set함수로 쉽개 해결 할 수 있다.
num_rest = []                 #입력받은 모든값의 나머지를 리스트화하기 위해 만듬.
for i in range(10):            #일일히 한줄씩 입력을 받는것보단 반복문을 통하여 10개를 쉽게 받을 수 있다.
    num = int(input())
    rest = num % 42
    num_rest.append(rest)
set_rest = set(num_rest)
print(len(set_rest))
    


