# while 반복문
# "hello"라는 단어를 10번 출력

# i = 0
# while i <= 10:
#     print("Hello", i)
#     i += i + 1

# 1부터 10까지 더하기
#i = 0
#sum_v = 0
#while i < 10:
#    i += 1
#    sum_v = sum_v + i
#    print("i =", i, "sum=", sum)

#print(f'합계 : {sum_v}')

#반복 조건문(break)

i = 0
sum_v = 0
while True:
    i += 1
    sum_v += i
    if i > 10:
        break
    print(f'i={1}, sum_v={sum_v}')
print(f'합계 : {sum_v}')