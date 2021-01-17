## 입력받은 수 거꾸로 뒤집는 함수
def reverse_plz(num):

    num_length = (len(str(num))-1)
    rev = []   # rev 배열은 reverse의 약자로 입력된 숫자의 각 자릿수를 배열 형식으로 저장하는 공간입니다.

    while num_length >= 0 :
        res = num // 10**(num_length)  # res 변수는 int 형식으로 입력된 숫자를 자릿수별로 구해서 저장하는 공간입니다.
        rev.append(res)  # rev 배열에 int 형식의 res 변수 값들이 들어갑니다.
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
