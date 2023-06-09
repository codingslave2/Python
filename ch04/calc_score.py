# 학생의 4명 성적 통계

student = [
    {"name" : "이대한", 'kor':80, 'eng':80, 'math':75},
    {"name" : "박민국", 'kor':70, 'eng':100, 'math':100},
    {"name" : "이대한", 'kor':65, 'eng':75, 'math':100}
]

# print(student[0])
print(len(student))
print("== 개인별 성적표 ")
print("이름 국어 영어 수학")
for std in student:
    # print(std['name'], std['kor'], std['eng'], std['math'])
    print(f"{std['name']} {std['kor']} {std['eng']} {std['math']}")

print("== 개인별 총점과 평균 ==")
print("이름  총점  평균")
for std in student:
    total = std['kor'] + std['eng'] + std['math']
    avg = total / 3
    print(f"{std['name']} {total} {avg: 2f}")

# 과목별 총점과 평균
sum_subj = [0, 0, 0] # 국어총점, 영어총점, 수학총점
avg_subj = [0.0, 0.0, 0.0] #국어평균, 영어평균, 수학평균

for std in student:
    sum_subj[0] += std['kor']
    sum_subj[1] += std['eng']
    sum_subj[2] += std['math']

print("== 과목별 총점 ==")
print(f"국어 총점 : {sum_subj[0]}")
print(f"영어 총점 : {sum_subj[1]}")
print(f"수학 총점 : {sum_subj[2]}")

# 과목별 평균
for avg in student:
    avg_subj[0] = sum_subj[0] / len(student)
    avg_subj[1] = sum_subj[1] / len(student)
    avg_subj[2] = sum_subj[2] / len(student)
    

print("== 과목별 평균 ==")
print(f"국어 평균 : {avg_subj[0]}")
print(f"영어 평균 : {avg_subj[1]}")
print(f"수학 평균 : {avg_subj[2]}")
