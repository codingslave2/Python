# 가위바위보 게임

import random

print("♠ 가위 바위 보 게임 ♠")
가위바위보 = ['가위', '바위', '보']
result = {0: '무승부', 1:'패', 2:'승'}
state = 0 # 상태 변수 (0/1/2)

while True:
    player = None
    comp = random.choice(가위바위보)


    while player not in 가위바위보:  
        def play(player, comp):
            if player not in 가위바위보: # x in y 문
                print("잘못된 입력입니다. 다시 입력해주세요.")
                return
    
    # 비긴 경우, 이긴 경우, 진 경우

    

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