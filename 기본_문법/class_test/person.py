# 클래스 이름은 Person
# name과 age를 인자로 받아서 생성
# hello() -> 안녕! 장원영, 나이는 21
# update_age() -> 나이를 받아서 수정,
# 음수를 나이로 받으면 raise ValueError("나이는 양수야.")
# dance() -> 장원영이 춤을 춥니다.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def hello(self):
        return f"안녕! {self.__name} 나이는 {self.__age}"
    
    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 양수야.")
        else:
            self.__age = age

    def dance(self):
        return f"{self.__name}이 춤을 춥니다."