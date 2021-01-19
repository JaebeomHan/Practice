input_list = []
for i in range(4):
    input_list.append(int(input(f"{i}번: ")))

sum_list = []
for i in range(4):
    temp = 1
    for j in range(4):
        if i == j:
            continue
        temp *= input_list[j]
    sum_list.append(temp)
print(sum_list)