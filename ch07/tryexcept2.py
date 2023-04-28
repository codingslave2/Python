# try ~ except ~ finally 구문

def divide(x, y):
    try:
        result = x/ y
        print(result)
    except ZeroDivisionError as e:
        return e
    finally:
        print("여기는 반드시 수행되는 구간입니다.")

divide(2, 4)
# print(divide(2, 1))
