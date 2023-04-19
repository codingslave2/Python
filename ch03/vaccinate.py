while True:
    try:

        birth_year = input("출생년도 입력 : ")
        if birth_year == "q":
            break
        
        #나이 계산
        age = 2023 - int(birth_year) + 1

        #연산 및 출력
        if age >= 20 and age <= 65:
            print("백신 접종 대상")
            if birth_year[-1] == "1" or birth_year[-1] == "6":
                print("월요일")
            elif birth_year[-1] == "2" or birth_year[-2] == "7":
                print("화요일")
            elif birth_year[-1] == "3" or birth_year[-2] == "8":
                print("수요일")
            elif birth_year[-1] == "4" or birth_year[-2] == "9":
                print("목요일")
            elif birth_year[-1] == "5" or birth_year[-2] == "10":
                print("금요일")
        else:
            print("하반기 일정 확인")

    except:
            print("생년월일을 입력하세요")
