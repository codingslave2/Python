# 정렬방법 - 1. 내장함수, 2. 반복조건문
# 리스트의 메소드 sort(), reverse()

a = [1, 5, 4, 15, 6]

n = len(a)

# 1. 내장함수

# a.sort() # 오름차순
# print(a)

# a.sort(reverse=True) # 내림차순
# print(a)

# 2. 반복 조건문(중첩 for)
# 정렬 알고리즘 - 버블 정렬(bubble)
for i in range(0, n):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            # 교환(자리바꾸기)
            # a[j], a[j+1] = a[j+1], a[j]
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(a)


# i=0(1행) a[0] > a[1] False 1, 5
#         a[1] > a[2] True 1, 4, 5
#         a[2] > a[3] False 1, 4, 5, 15