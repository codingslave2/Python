#입력
name = input("이름 : ")
user_id = input("아이디 : ")
pw = input("비밀번호 : ")
id_number1 = input("주민등록번호 앞자리 입력 : ")
id_number2 = input("주민등록번호 뒷자리 입력 : ")
print('='*30)

#출력
print("이름 : {}".format(name))
print("아이디 : {}".format(user_id))
pw = '*' * len(pw)
print("비밀번호 : {}".format(pw))
id_number2 = id_number2[0] + ('*' * 6)
print("주민등록번호 : {0}-{1}".format(id_number1, id_number2))