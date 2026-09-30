class Animal:
    # 클래스 변수 생성
    # 모든 Animal 타입의 인스턴스가 공유 변수
    species_count = 0
    Kingdom = "동물계" # 고정해서 사용할 변수

    # 생성자
    # 클래스 내에서 사용되는 모든 내부변수는 생성자에서 초기화해야 한다.
    def __init__(self, name, age):
        self.name = name
        self.__age = age # name mangling(캡슐화)
        # 클래스 변수를 1 증가: 생성된 종의 수를 관리
        # 클래스 변수의 접근은 클래스이름.변수명
        Animal.species_count += 1

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age < 0:
            print("나이는 0보다 작을 수 없어요.")
        else:
            self.__age = age

    def make_sound(self):
        print(f"{self.name}이 소리를 냅니다.")

    # toString() 만들기
    def __str__(self):
        return f"[{self.__class__.__name__}] 이름: {self.name}, 나이: {self.__age}"