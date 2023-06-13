'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

입력의 마지막에는 0 두 개가 들어온다.

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력 1
1 1
2 3
3 4
9 8
5 2
0 0
예제 출력 1
2
5
7
17
7
'''

# 반복되는 횟수를 모르는 반복. -> 종료 조건이 주어짐 (break)
# 무한 반복
while True:
    A, B = map(int, input().split())  # 1 1 -> split 쪼개고 int로 숫자 변환
    # print(A + B)  # A+B? 0+0? => 출력
    if A == 0 and B == 0:
        break # 더 이상 반복하지 않겠다
    print(A + B)  # A+B?
    # 무한 반복? 어디선가 break
