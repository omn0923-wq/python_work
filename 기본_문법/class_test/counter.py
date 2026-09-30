# 클래스는 class 키워드로 만든다.
# 클래스의 이름은 카멜케이스를 따른다.(약속)
# 모든 클래스 내의 메서드는 self라는 args를 갖는다.
# self: java의 this랑 같은 개념
# 클래스 내부 변수에 _를 붙이면, private 변수로 간주한다. : 개발자 간의 약속
# 클래스에서 필요한 모든 변수는 __init__에서 초기화해 둔다.
class Counter:
    # 클래스의 생성자
    def __init__(self):
        self._count = 0
        # __를 붙여서 만드는 변수 -> Name Mangling
        # 내부적으로 _클래스이름__변수명 이름을 바꿔치기 해 준다.
        self.__myname = "Kim"

    def reset(self):
        self._count = 0
 
    def increase(self):
        self._count += 1

    def get(self):
        return self._count
    
class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
    
    def set_name(self, name):
        self.__name = name

    def show_info(self):
        return f"name = {self.__name}, age = {self.__age}"
    
    # =========== 윗 공간 코딩
    
# 아래는 main 함수처럼 사용
if __name__ == "__main__":
    # Counter 클래스의 인스턴스를 생성
    my_counter = Counter()
    # self.count = 0 변수 선언과 초기화
    # my_counter.reset()
    my_counter.increase()
    print(f"counter value: {my_counter.get()}")

    my_counter._count += 1
    print(f"counter value: {my_counter.get()}")

    # __name 변수 값 출력
    # print(f"__name 출력: {my_counter.__myname}")
    print(f"__name 출력: {my_counter._Counter__myname}")

    # Student 클래스 인스턴스 생성(홍길동, 25)
    hong = Student("홍길동", 25)
    # 정보 출력
    print(hong.show_info)