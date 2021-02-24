#for과 break을 사용해서 구하자#

a=int(input("무슨 값이 궁금하니?:"))
b=a

for i in range(0,61):
    num1=str(b) #리스트를 만들기 위한 작업#
    num2=(b-b%10)/10+b%10 #각 자릿수를 더하기 위한 작업#
    if b<10: #b가 한자리수면 곤란해짐#
        num3=b*10+num2
    else:
        num3=num1[1]+str(num2%10)
    num4=float(num3) #합쳐진 리스트 요소와 num2를 숫자로 다시 변환#
    i=i+1
    if num4!=a:
        b=num4
    else:
        break
    
print(i)