#커피의 개수
coffee = 5

while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 400:
        print("커피가 나옵니다.")
        coffee -= 1
    elif money > 400:
        print("커피가 나오고, 거스름 돈" + str(money-400) + "원을 돌려 받습니다.")
        coffee -= 1
    else:
        print("커피가 나오지 않습니다.")
    print("남은 커피의 양은" + str(coffee) + "개 입니다.")