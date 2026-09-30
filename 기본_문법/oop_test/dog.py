# from 패키지명 import 클래스명
# from 패키지명 import 함수명

from oop_test.animal import Animal
# ctrl + space: 클래스

# Animal 클래스를 상속받음.
# 파이썬의 상속은 클래스명(상속받을 클래스명)
class Dog(Animal):
    sound = "멍멍!"

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name}: {Dog.sound}")