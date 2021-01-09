
## 배열 만드는 함수
def make_list(sentence):

    length = len(sentence)
    num = 0
    list_result = []
    while( length > 0 ):
        result = [ (sentence[num]) , int(sentence.count(sentence[num])) ] # 각 단어의 개수 배열로 지정
        list_result.append(result)
        length -= 1
        num += 1

    new_list_result = []
    for w in list_result:
        if w not in new_list_result:
            new_list_result.append(w)  # 중복되는 배열 제거
    return new_list_result

## 출력 담당하는 함수
def order_print(new_list_result, count):

    new_list_result.sort(key = lambda x:(x[1], x[0]))  # 순서 지정 (숫자로 오름차순)
    print("[ Sentence %d ]" % count)
    for word in new_list_result:
        print('{} : {}'.format(word[0], word[1]))

## 출력 담당하는 함수 (END 입력 시)
def order_print_END(new_list_result):

    new_list_result.sort(key = lambda x:(x[1], x[0]))  # 순서 지정 (숫자로 오름차순)
    print("[ All Sentence ]")
    for word in new_list_result:
        print('{} : {}'.format(word[0], word[1]))


total_sentence = []
count_a = 1

while True:
    
    sentence = input(str("아무 문장이나 입력 : ")).split()  # 최초 배열

    if (sentence == ["END"]): # END 입력되면
        break

    else: # 정상 진행
        total_sentence += sentence
        order_print(make_list(sentence), count_a)
        count_a += 1

# 위에서 했던 과정 똑같이 반복
order_print_END(make_list(total_sentence))

print("프로그램 종료")