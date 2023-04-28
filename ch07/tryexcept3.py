# try ~ except ~ else
# error가 있으면 except 구문을 실행하고
# error가 없으면 try ~ else ~를 실행함

try:
    with open ('./py/pyfile/output/kbo2023.txt', 'r') as f:
        team = f.read()

except FileNotFoundError as e:
    print(e)
else:
    for i in team:
        print(i, end='')