Num_input = int(input("가장 작은 생성자를 알고 싶은 숫자: "))
result = 0
for i in range(1,Num_input):
    temp = i
    j = i
    while j > 0:
        temp += (j % 10)
        j = int(j / 10)
    if temp == Num_input:
        result = i
        break
print(f"{Num_input}의 가장 작은 생성자: {result}")