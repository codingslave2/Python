while True:
    answer = input('반복을 계속할까요?(Y/N)')

    if answer == 'y' or answer == 'Y':
        print('반복을 계속합니다.')
    elif answer == 'n' or answer == 'N':
        print('반복을 중단합니다.')
        break
    else:
        print('정상 답변이 아닙니다.')