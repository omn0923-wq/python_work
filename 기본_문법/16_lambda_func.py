# 람다(Lambda) 함수
# 자바(->), 스크립트(=>)와 유사하지만, python은 lambda 키워드를 직접 쓴다.
# 익명 함수: 1회성 실행 함수 작성

def add(x, y):
    return x + y

print(add(3, 4))

add = lambda x, y : x + y
print(add(7, 8))

# 한 줄만 가능 / return 키워드 없음. 간단한 일회성만.
# 짝수, 홀수 구분용 람다 함수
"""
x = 4
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")
"""
is_even = lambda x : "짝수" if x % 2 == 0 else "홀수"
print(is_even(10))

# 여러 개의 매개변수를 받아서 처리하는 람다 함수
# 세 개의 수 곱하기
multiply = lambda x, y, z : x * y * z
print(multiply(1, 2, 3))

# 함수 중에 map(), filter()
# map(): 원본을 특정 과정을 거쳐서 수정
# filter(): 원본 중에 맞는 조건을 걸러내는 역할

# 리스트의 각 요소에 제곱을 해서 변환: map
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x : x**2, nums))
print(squared)

# 짝수만 골라서 리스트로 받아 출력
evens = list(filter(lambda x : x % 2 == 0, nums))
print(evens)