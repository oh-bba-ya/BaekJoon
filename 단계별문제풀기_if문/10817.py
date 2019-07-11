#왜 if문 문제인지 모르겠다.

num = list(map(int,input().split()))
num.sort()
print(num[1])

#이건 왜 안되는지 모르겠다. 반론이 있으니깐 안되는거 같은데 왜 안되는거지
num = list(map(int,input().split()))
big = max(num)
for i in num:
    if i == big:
        num.remove(big)
        print(max(num))

