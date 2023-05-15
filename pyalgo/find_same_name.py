

def find_same_name(a):
    same_name = set() # 중복값을 넣을 빈 집합 생성
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                #중복값 추가
                same_name.add(a[i])
    return same_name


# 동명 이인 찾기 -중복값 찾기
name = ['흥부', '콩쥐', '놀부', '콩쥐']
# same_name = set()
# print(same_name)
# n = len(name)
print(find_same_name(name))