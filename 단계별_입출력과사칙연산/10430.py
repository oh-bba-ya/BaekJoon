Num = list(map(int,input().split()))
A = Num[0]
B = Num[1]
C = Num[2]

print((A+B)%C)
print((A%C+B%C)%C)
print((A*B)%C)
print((A%C*B%C)%C)
