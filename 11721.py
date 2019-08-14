alpha = input()                #str을 입력받는다.
for i in range(0,len(alpha),10):        #for문의 범위설정 10칸씩 간격을 둔다.
    print(alpha[i:i+10])            #출력은 0,10,20....늘어나면서 i+10을 설정해둠으로써 10개만 출력된다.
                                    #10이하의 숫자들이 나와도 출력된다.
