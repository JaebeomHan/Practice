num = int(input("양의 정수를 입력"))

num_length = (len(str(num))-1)
rev = []

while num_length >= 0 :
    res = num // 10**(num_length)
    rev.append(res)
    num = num - res * 10**(num_length)
    num_length -= 1

rev.reverse()

for k in rev:
    print(k,end='')

print()
print(sum(rev))