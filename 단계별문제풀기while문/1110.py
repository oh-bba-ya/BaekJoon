num1 = int(input())
num2 = num1
count = 0
while True:
    add1 = num1 // 10        #십의자리.
    add2 = num1 % 10        #일의자리.
    result = add1 + add2
    count += 1                        #반복될때마다 숫자가 올라감.
    num1 = int(str(add2)+str(result%10))        #여기서 부터 다시 숫자 설정하여 조건문에 부합하지 않으면 add1,add2가 다시설정.
    
    if num1 == num2:                #처음 주어진 숫자와 루프후 다시 조합된 숫자가 같으면 탈출.
        break
print(count)
    
    
