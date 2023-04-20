# 1~100까지의 자연수 중 배수와 배수의 개수를 계산하는 함수를 정의하시오.

def times(x):    
    for i in range(1, 101):
        global count
        if i % 3 == 0:
            count += 1
            print(i, end=' ')

count = 0
times(3)
print(f'\n배수의 개수 : {count}')