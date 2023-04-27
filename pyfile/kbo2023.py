
# f = open('./output/string.txt', 'w')

# f.write("여름이 온다\n")
# f.write('123')
# val = (12 * 1000) / 5
# f.write(str(val))

# f.close()

# kbo 팀 파일에 기록

team = ['삼성', '롯데', '두산', '한화', '기아',
        '키움', 'NC', 'LG', 'KT', 'SSG']

try:
    with open ('./py/pyfile/output/kbo2023.txt', 'w') as f:
        for i in team:
            if i == team[-1]: #team의 마지막 요소의 쉼표 생략
                f.write(i)

            else:
                f.write(i + ", ")

except:
    print("파일을 쓸 수 없습니다.")


# kbo2023.txt 읽기


try:
    with open ('./py/pyfile/output/kbo2023.txt', 'r') as f:
        team = f.read()
        print(team)

except FileNotFoundError as e:
    print(e)
    print("파일을 읽을 수 없습니다.")