N=int(input("생성자는 무엇이니?: "))
a=N
list1=[]

for i in range(0,N):
    a=a-1 # 1씩 줄이면서 판별
    N_1=a+int(a/100)+int((a%100-a%10)/10)+a%10 # N_1은 수+각 자리수 합
    if N_1==N:
        list1.append(a)

list1.sort()

print(list1[0])