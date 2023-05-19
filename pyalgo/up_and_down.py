# 숫자 추측 게임

# 게임 방법

# - 게임이 시작되면 컴퓨터가 난수(정답)를 생성한다.
# - 사용자의 추측값이 정답과 같으면 '정답!',
# - 추측 값이 정답보다 크면 "너무 커요!",
# - 추측 값이 정답보다 작으면 "너무 작아요!" 출력

import random

attempts = 0
min_v = 1
max_v = 50

com = random.randint(min_v, max_v)


# while True:
#     guess = int(input(f"숫자를 입력하세요.({min_v}~{max_v}): "))

#     if guess == com:
#         print(f"정답! {com}")
#         break
#     elif guess > com:
#         print("커요.")
#         max_v = guess - 1
#     else:
#         print("작아요")
#         min_v = guess + 1


for i in range(0, 10):
    try:
        guess = int(input(f"숫자를 입력하세요.({min_v}~{max_v}): "))

        if guess > 50 or guess < 1:
            print("정상 범위가 아닙니다.")
        elif guess == com:
            print(f"정답! {attempts} 번만에 맞추셨습니다.")
            break
        elif guess > com:
            print("커요.")
            max_v = guess - 1
        else:
            print("작아요")
            min_v = guess + 1

    except ValueError:
        print("유효한 숫자가 아닙니다.")
