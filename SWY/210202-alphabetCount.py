# [Qus] 210128
a = input("문자열 입력: ")
count = 1
for i in range(1,len(a)):
    if(a[i]!=a[i-1]):
        print(a[i-1], count, sep='', end='')
        count=1
    else:
        count+=1
    if i==len(a)-1:
        print(a[i], count, sep='')