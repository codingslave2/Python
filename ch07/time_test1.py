import time


start = time.time()
def getgob(n):
    gob = 1 # 곱셈에서는 1을 기억
    for i in range(1, n+1):    
        gob *= i
        print(i, gob)
    return gob

print(getgob(100))
end = time.time()
print(f'소요 시간 : {end-start}')
