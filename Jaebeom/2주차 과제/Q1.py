
N = str(input("높이를 입력하세요 (자연수)"))

N = int(N)

sum = 0
for n in range(N):
    sum = sum + (n+1)

list_a = []

matrix = [[0 for col in range(N-1)] for row in range(N-1)]   # N-1 크기의 정사각행렬 만듦

for m in range(N):  # m은 0부터 2까지 (N=3일때)
    list_a.append([m])  # 0 1 2
    list_b = sorted(list_a, reverse=True)   # 2 1 0

    print(list_a)
   # print(list_b)

  #  matrix[m][c] = chr(65+n)

  #  print(matrix)



#for sum in range(sum):
 #   list_a.extend([chr(65+sum)])
  #  str_a = "".join(list_a)
   # print(str_a)