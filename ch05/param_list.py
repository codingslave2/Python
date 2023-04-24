# v = [1, 2, 3, 4]


# 리스트의 합계, 최대값, 최소값

# 입력
# v = [1, 2, 3, 4]
# sum_v = 0

# # print(sum(v))
# # print(max(v))
# # print(min(v))

# 리스트의 합계 연산하는 함수 정의 - get_sum()
def get_sum(a):
    sum_v = 0
    for i in v:
        sum_v += i
    return sum_v

# 리스트의 평균을 계산하는 함수
def get_avg(a):
    sum_v = 0
    for i in a:
        sum_v += i
    return sum_v / len(a)

# 리스트의 최대값을 구하는 함수
def get_max(a):
    max_v = a[0] # 리스트의 첫번째 값을 최대값으로 설정
    for i in v:
        if max_v < i:
            max_v = i
    return max_v

    
# 리스트의 최대값의 위치 구하는 함수
def get_max_idx(a):
    max_idx = a[0] # 첫번째 값을 최대값의 위치로 설정
    n = len(a)
    for i in range(1, len(a)):
        if a[max_idx] < a[i]:
            max_idx = i
        return max_idx # for문 종료시 return


v = [1, 2, 3, 4, 5]
print("리스트의 개수 : ", len(v))
print("합계 : ", get_sum(v))
print("평균 : ", get_avg(v))
print("최대값 : ", get_max(v))

# 최대값
v = [1, 3, 9, 7, 5]


# 연산
# for i in v:
#     if max_v < i:
#         max_v = i
    
# 출력


# # 합계 연산
# for i in v:
#     sum_v += i 



# # 출력
# print(sum_v)