def calculator(num):
    result_list = []
    list_inter = []

    for i in range(0,num):
        inter =  num - i # num에 1씩 뺀 값을 계속해서 배열 list_str_inter 에 넣는 코드
        list_inter.append(inter) # 먄약 num이 3이면 list_inter = [3,2,1]

        for order in range (0, len(list_inter)): # list_inter에 3,2,1 이 들어있다고 치면
            inter += list_inter[order] # inter 에다가 3, 2, 1을 한번씩 더할거임
            result = inter # 그 값을 result 에 다시 넣을거임. 일단 3을 더한 결과 6이 result에 들어갈거고

            if (result == num): # 6은 3인가? 에 대한 조건문은 ㄴㄴ 이므로 아래 조건문은 실행되지 않음
       #         print( list_str_inter[len(list_str_inter)]

                result_list.append(list_inter)

                print(result_list)


calculator(216)