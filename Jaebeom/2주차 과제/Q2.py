## 입력받은 수 거꾸로 뒤집는 함수
def reverse_plz(num):

    num_length = (len(str(num))-1)
    rev = []

    while num_length >= 0 :
        res = num // 10**(num_length)
        rev.append(res)
        num = num - res * 10**(num_length)
        num_length -= 1

    rev.reverse()
    return rev

## 결과값 21억 넘는지 검사하고 출력하는 함수
def check_and_print(rev):

    if(rev[0]==2 and rev[1]==1 and num>1000000000):
        print("결과값이 21억 이상이라 출력 불가")
        print()
    else:
        for k in rev:
            print(k,end='')
        print()
        print(sum(rev))

while(True):
    num = int(input("양의 정수를 입력 : "))
    if (num>2100000000):
        print("21억 넘으면 안됨")
        break
    if (num==0):
        print("0을 입력하면 종료")
        break

    check_and_print(reverse_plz(num))
