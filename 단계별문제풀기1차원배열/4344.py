T = int(input())                    #테스트케이스를 입력받는다.
for i in range(T):                    #T만큼 입력받을 갯수를 반복한다.
    case = list(map(int,input().split()))        #케이스들을 입력받는다.
    aver = sum(case[1:])//case[0]                #케이스의 평균을 구한다.
    result = []                        
    for j in range(1,len(case)):                #받은 각 케이스의 반복문.
        if case[j] > aver :                        #각 케이스의 평균보다 높은 것들은 result에 추가된다.
            result.append(case[j])
    score = len(result)/case[0]*100                    #score = (평균통과자 / 케이스 인원) * 100 , (백분율)
    print('%.3f%%' %(score))            #소수점 3자리까지 표현하고 %를 표현하기 위해 %%를 사용.
