#문제를 읽어보면 조건문이 보인다.
N = list(map(int,input().split()))
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

if N == ascending :            #오름차순.
    print("ascending")
elif N == descending:          #내림차순.
    print("descending")
else:                           #그외.
    print("mixed")
