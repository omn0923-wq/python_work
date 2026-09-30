from oop_test.dog import Dog
from oop_test.cat import Cat
from oop_test.animal import Animal

def main():
    dog = Dog("초코", 3, "포메라니안")
    cat_1 = Cat("나비", 2)
    cat_2 = Cat("이오", 1)

    dog.make_sound()
    cat_1.make_sound()

    print(dog)
    
    cat_1.set_age(3)
    print(cat_1.get_age())

    # Animal 클래스 변수 확인
    print(f"현재까지 생성된 동물 수: {Animal.species_count}마리")

    # 다형성 테스트
    # 부모 클래스 타입으로 선언 후에 자식을 할당...
    # 파이썬의 경우에는 변수의 타입이 없고, 할당할 때 타입이 결정
    animals = [dog, cat_1, cat_2]

    for x in animals:
        x.make_sound()

if __name__ == "__main__":
    main()