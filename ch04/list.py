# 리스트
a = [1, 2, 3, 4]

print(a)

#리스트에 5를 추가
a.append(5) # 맨 뒤에서 추가

print(a)

#5를 삭제

a.pop() # 맨 뒤에서 삭제
print(a)

# 리스트 복사
a2 = [] # 복사하기 위해 빈 리스트 생성
a2 = a
print(a2)

# for ~ in으로 복사

for i in a:
    a2.append(i)
print(a2)

# 리스트에서 홀수만 지정
# a3 = []
# for i in a2:
#     if 1 % 2 != 0:
#         a3.append(i)
# print(a3)

# a 리스트의 합계와 평균
sum_v = 0
for i in a:
    sum_v += i

avg = sum_v / len(a) # 평균
print(f'[a]의 합계 : {sum_v}')
print(f'[a]의 평균 : {avg_v}')

# 내장함수

print(f'sum = {sum(a)}')