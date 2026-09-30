# 함수의 기본 구조
"""
def 함수 이름(인자1, 인자2):
    본문
    return 결과 값
"""
# 인자와 리턴 값의 타입을 지정(선택)
"""
def 함수 이름(인자1: int, 인자2: str) -> list :
    본문
    return 결과 값
"""

def func_1():
    print("함수 만들기 연습")

func_1()

def func_2(name):
    print(f"{name}이 만든 함수")

func_2("glidong")

# 두 수를 입력받아서 곱해서 리턴해 주는 함수
# 함수의 이름은 multiply
def multiply(x, y):
    return x * y

print(multiply(3, 4))

# Default param.
def study(name, lang="Python"):
    print(f"{name}은 {lang}을 공부함.")

study("glidong")
study("장원영", "Java")

# 가변인자: 여러 인자를 한꺼번에 전달
# args: aguments(인자)
def cal_sum(*args):
    total = 0
    for arg in args:
        total = total + arg

    return total

print(cal_sum(1, 2, 3, 4, 5))

# 가변인자 + 일반 매개변수 전달
# 가변인자 제외 변수는 항상 이름을 함께 전달 규칙
def cal_sum(*args, name):
    total = 0
    for arg in args:
        total = total + arg

    return total

print(cal_sum(1, 2, 3, 4, 5, name="안유진"))

#  매개변수를 Dict 형태로 받기
# **Kwargs: keyword arguments

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="ive", members=5)

info = {"name": "KIM", "age": 21, "city": "BUSAN"}
print_info(**info)

def greet(name: str) -> str :
    return f"Hi! {name}"

print(greet("glidong"))

def calc(x: int, y: int) -> tuple[int, int]:
    return x + y, x * y

x, y = calc(3, 4)
print(f"{x} / {y}")