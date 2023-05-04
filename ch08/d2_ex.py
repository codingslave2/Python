# 2차원 리스트

# d = [
#     [10, 20],
#     [30, 40],
#     [50, 60],
#     [70, 80],
#     [90, 100]
# ]

# # 3행 2열
# print(d[0][0]) # 10
# print(d[1][1]) # 40
# print(d[2][0]) # 50

# # 새 요소 추가
# d.append([110, 120])

# # 2차원 리스트 객체 추가
# print(d)

# # 전체 요소(값) 추가
# for x, y in d:
#     print(x, y)

# 리스트 이름 = [요소1, 요소2. [값1, 값2]]
# e = [7, 3, ['chicken', 'eagle', 'monkey']]

# print(e[1]) # 3
# print(e[2])
# print(e[-1])

# # eagle을 인덱싱
# print(e[2][1]) # 2행 1열 출력
# print(e[-1][1]) # -1행 1열 출력

# 수학 영어 과목의 총점과 평균

score = [
    [80, 70],
    [90, 50],
    [70, 100],
    [65, 85]
]

# 개인별 총점과 평균

total = 0 # 개인별 총점을 저장할 변수

# 수학 - 1열
# 영어 - 2열

print("총점 평균")
math = score[1][0]
eng = score[0][0]

n = len(score)

for i in range(0, n):
    total = score[i][0] + score[i][1]
    print(total)
    print(total / 2)

# 과목별 총점
sum_subj = [0, 0] # sum_subj[0] = 수학 총점, sum_subj[1] = 영어 총점

for i in range(0, n):
    sum_subj[0] += score[i][0] # 수학 점수 누적합
    sum_subj[1] += score[i][1] # 영어 점수 누적합


# print("과목별 총점과 평균")
# print("수학총점 영어총점 수학평균 영어평균")
# print(sum_subj[0], sum_subj[1],
#       sum_subj[0]/len(score), sum_subj[1]/len(score))

print("총점 : 수학 영어")
print(f'\t {sum_subj[0]}, {sum_subj[1]}')

print("평균: 수학 영어")
print(f'\t {sum_subj[0]/n}, {sum_subj[1]/n}')