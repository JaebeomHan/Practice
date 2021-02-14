#[Qus] 210209
num_input = int(input())
tmp = num_input
resualt = -1
count = 0
while num_input != resualt:
        tmp = (tmp % 10) * 10 + (int(tmp / 10) + tmp % 10) % 10
        resualt = tmp
        count+=1
print(count)