Num_input = int(input("가장 작은 생성자를 알고 싶은 숫자: "))
for i in range(Num_input):
    N_sum = i
    temp = i
    while True:
        if (int(temp / 10) != 0):
            N_sum += (temp % 10)
            temp = int(temp / 10)
            continue
        else:
            N_sum += temp
            break
    if N_sum == Num_input:
        print(f"{Num_input}의 가장 작은 생성자: {i}")
        quit()
print("0")