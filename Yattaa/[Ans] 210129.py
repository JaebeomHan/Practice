a=int(input("어떤 값을 정렬할거니?:"))

num1=list(str(a))
num1.sort()
num1.reverse()
num2="".join(num1) #리스트를 문자열로#

print(num2)