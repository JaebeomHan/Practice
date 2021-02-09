num = int(input("수를 입력하세요 : "))

numSplit = []
while num != 0:
    numSplit.append(num % 10)
    num = num // 10

numSplit.sort(reverse = True)
print(numSplit)

for num in range (0, len(numSplit)):
    print(numSplit[num], end="")