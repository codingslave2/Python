#교통 수단 이용
# 파이썬에서는 &&, !!, || 같은 연산자 사용 안함
# and, or , not으로 사용

# money = 0
# card = False

# if money >= 4000 or card:
#     print("택시를 탄다")
# elif money >= 2000 or not card:
#     print("버스를 탄다")
# else:
#     print("걸어간다.")

pocket = ['paper', '스마트폰', 'money']
# print('paper' in pocket)
# print('coin' in pocket)

if 'paper' in pocket:
    print("버스를 탄다")
else:
    print("걸어간다")

