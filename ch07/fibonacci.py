# 피보나치 사용 1 1 2 3 5 8 11 ...
# 첫째항 및 둘째항이 1이며, 그 뒤의 항은 바로 앞 두 항의 합임

def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(1)) # 1
print(fibo(2)) # 2
print(fibo(3)) # 3
print(fibo(4)) # 5
print(fibo(5)) # 8
print(fibo(6)) # 11
