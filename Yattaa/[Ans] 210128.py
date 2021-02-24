a=input("어떤 글자들이니?:")
list_a=list(a) #str을 list로 바꿈#
list_a.append(a[len(a)-1]) #for문에서 리스토 요소 하나 부족해서 채움#
count=1 #같은 숫자 몇개인지 세줌#
list_n=[]
num=0

for i in range(0,len(a)):
    if list_a[i]==list_a[i+1]: # 현재 음절이 뒤의 음절과 같은 경우#
        count=count+1
        if i==len(a)-1: #마지막 음절인 경우#
            list_n.append('%c%d' %(list_a[i],count-1)) #마지막에 같은 글자 하나 추가했으므로 카운트-1#
    else:
        list_n.append('%c%d' %(list_a[i],count)) #나중에 리스트 한 줄로 나열할 거임#
        count=1
        num=num+1

Out="".join(list_n)
print(Out)