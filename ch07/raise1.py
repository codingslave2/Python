# 예외 처리 미루기 -raise
# 클래스 상속
class Animal:
    def breathe(self):
        print("동물이 숨을 쉰다")


# 반드시 구형해야되는 매소드
    def cry(self):
        raise NotImplementedError

class Dog(Animal):
    def cry(self):
        print("멍멍")

class Cat(Animal):
    def cry(self):
        print("야옹")

dog = Dog()
dog.breathe()
dog.cry()

cat = Cat()
cat.breathe()
cat.cry()