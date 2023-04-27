# 재귀 함수
# 종료 조건을 항상 명시(if - else)
# 1부터 5까지 곱하기

def getgob(n):
    gob = 1 # 곱셈에서는 1을 기억
    for i in range(1, 6):    
        gob *= i
        #print(i, gob)
    return gob

# 재귀 함수
# 5*4*3*2*1 = 5!(팩토리얼, 계승)

def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)



# getgob() 호출
getgob(5)
print(getgob(5))

def sos(n):    
    print("help me!")
    # 종료 조건
    if n == 1:
        return ""
    else:
        return sos(n-1)

sos(5)