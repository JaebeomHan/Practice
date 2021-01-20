num_input = []
for i in range(3):
    num_input.append(int(input(f"{1}번 숫자: ")))
num_input.sort()
print(num_input[1])