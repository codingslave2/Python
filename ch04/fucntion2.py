#함수 - return()이 있는 함수

def one_up(): # 1을 더하는 함수
    x = 0     # 지역 변수
    x = x + 1
    return x

def square(x): # 제곱수를 계산
    val = x*x
    return val

def add(x, y): #두 수를 더하는 함수
    val = x + y
    return val

# print(one_up())
# print(one_up())

# square 함수
# print(square(5))
# result = square(3)
# print(result)

#add 함수
print(add(3, 4))