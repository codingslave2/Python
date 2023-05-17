# 가위 바위 보 게임 만들기

# '''
# - 게임 방법
# 1. 당신(you)은 가위, 바위, 보 중 하나를 입력한다.
# 2. 컴퓨터(com)은 가위, 바위, 보 중 하나를 랜덤 생성한다
# 3. 결과 출력은 무승부, 패, 승이다.
# 4. 잘못 입력한 경우, "잘못된 입력입니다. 다시 입력해주세요"

# '''

import pygame
import random

rps = ("가위", "바위", "보")

# 초기화
pygame.init()

# 화면 크기
# screen_width = 640
# screen_height = 480
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("가위 바위 보 게임")



# 게임 루프
while True:
    player = None
    comp = random.choice(rps)

    while player not in rps:  

        player = input("가위, 바위, 보 중에서 선택하세요. 종료하려면 '종료'를 입력하세요: ")

        if player == "종료":
            print("게임을 종료합니다.")
            exit()

        if player == comp:
            print("무승부!")
        elif player == "가위" and comp == "보":
            print("승리!")
        elif player == "바위" and comp == "가위":
            print("승리!")
        elif player == "보" and comp == "바위":
            print("승리!")
        else:
            print("패배!")


    print(f"당신 : {player}")
    print(f"컴퓨터 : {comp}")


# 게임 종료
pygame.quit()
