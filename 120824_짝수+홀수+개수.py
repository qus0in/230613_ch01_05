def solution(num_list):
    # num_list -> 정수가 담긴 리스트
    # 짝수와 홀수의 개수를 담은 -> return
    answer = [0, 0]
    # even = 0 # 짝수의 개수
    # odd = 0 # 홀수의 개수
    for n in num_list: # 처음부터 끝까지 for를 통해서 순회.
        # 짝수라면 even += 1
        print(n)
        if n % 2 == 0:
            print(str(n) + "는 짝수입니다")
            # even += 1
            answer[0] += 1
        else:
            print(str(n) + "는 홀수입니다")
            # odd += 1
            answer[1] += 1
    # print(even, odd)
    # answer = [even, odd]
    return answer