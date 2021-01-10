

height = int(input("높이를 입력하세요 : "))
string = 0
stringplus = 0

for line_number in range(height+1):

    for blank in range(height - line_number):
        print(end="  ")  # 공백을 먼저 출력한다. 입력받은 높이에서 행 번호를 뺀 만큼.
                         # 예를들면 3을 입력했으면 1행에서는 2의 공백 출력.

    for stringplus in range(line_number):
        print(chr((int(line_number)-1)%26+65), end=" ")
        line_number += height - stringplus -1

    print('')