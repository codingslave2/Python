# # 문자열 1차원 리스트
# ss = "20230419Sunny"

# year = ss[0:4]
# month = ss[4:6]
# day = ss[6:8]
# weather = ss[8:]

# ss2 = year + month + day + weather
# print(ss2)

# #문자열 관련 함수
# #split(구분 기호) -> 문자열이 리스트로 변환
# # 문자열.split()
# fruit = "banana, apple, strawberry"
# fruitlist = fruit.split(" ,")
# # print(fruitlist)
# print(fruitlist[0]) # 1번 인덱스 -> apple

# #replace('이전문자', '새문자')
# str1 = 'Hello, World'
# str1 = str1.replace('World', 'Korea')
# print(str1)

# #format()
# str2 = "My name is {}".format('Mario') #format
# str3 = "My name is %s." % 'Mario' #string
# name = "Mario"
# str4 = f"My nane is {name}" #f-string
# print(str2)
# print(str3)
# print(str4)

# # split() 예제
# string = "a:b:c:d"
# string2 = string.split(' :')
# print(string2)
# print(string2[-1])

#두 수를 동시에 입력받아서 더하기
# n1 = int(input("첫번째 수 입력 : "))
# n2 = int(input("두번째 수 입력 : "))
# print(n1 + n2)

# n1, n2 = input("두 수 입력 : ").split() #공백으로 구분
# add = int(n1) + int(n2)
# print(add)

#find() - 문자열에 존재하는 위치 반환
text = "Hello"
print(text.find('H')) #0
print(text.find('ll')) #2
print(text.find('k')) #-1

print(text.find('Hello'))