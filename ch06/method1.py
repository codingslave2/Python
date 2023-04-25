# # 함수 - function, method(메소드)

import time

# # 1부터 10까지 출력

# for i in range(1, 10+1):
#     print(i)

# # # 1부터 n까지 출력하는 함수
def get_num(n):
    for i in range(1, n+1):
        print(i)


get_num(20) # 출력

# # 1부터 n까지 합계를 구하는 함수
def get_sum(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v


def get_sum2(n):
    sum_v = (n * (n+1)) // 2
    return sum_v
        

print(f'합계 : {get_sum(10)}')
print(f'합계 : {get_sum2(11)}')


# 계산 복잡도 - 곱셈, 덧셈, 나눗셈 - 3번 : 0(1)
# start = time.time()
# def get_sum2(n):
#     sum_v = (n * (n+1)) // 2
#     return sum_v

# print(f'합계 : {get_sum2(10000000)}')
# end = time.time()
# print(f'소요 시간 : {end-start} 초')