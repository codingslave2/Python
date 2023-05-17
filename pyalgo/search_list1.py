# 순차 탐색
# 리스트의 첫번째 자료부터 하나씩 비교하면서 같은 값이 나오면
# 그 위치를 돌려주고(반환), 몾찾으면 -1을 반환함

# 학생 번호에 해당하는 이름을 순차 탐색으로 찾아
# 돌려주는 함수를 작성하세요(단, 학생번호가 없으면 '?'를 반환함)


def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return i # 숫자가 있으면 리스트 반환
    return -1 # 없으면 -1 반환


def search_list(a, x):
    same_num = []  # 중복값을 저장할 리스트 생성
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            same_num.append(i)  # 숫자가 있으면 해당 위치를 리스트에 추가
    if len(same_num) > 1:
        return same_num  # 중복값이 2개 이상이면 리스트 반환
    else:
        return -1  # 중복값이 없거나 1개면 -1 반환


v = [60, 5, 33, 12, 97, 24, 5]
name = ['이순신', '강감찬', '서희', '안중근', '유관순']

# for i in range(0, n):
#     if v[i] == 12:
#         print("맞음")
#     else:
#         print("없음")


print(search_list(v, 5)) # -1
print(search_list(v, 12)) # 0
print(search_list(v, 100)) # 0

# 중복값 위치 찾기

print(search_list(v, 5))

