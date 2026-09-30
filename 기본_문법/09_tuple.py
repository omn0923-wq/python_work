# tuple: DB에서는 중복을 제거 한 컬럼의 유일값의 모음
# 파이썬: 값의 변경이 불가능한 리스트
# tuple의 선언

empty_tuple = ()
# 1개만 갖고 있는 tuple의 선언( , )를 찍는다.
one_tuple = (1, )
my_tuple = (1, 2, 3)
fruits = ("banana", "apple", "cherry")

# 데이터 추가
# 투플은 불변 데이터라 직접 추가 불가능
# 리스트로 변환 후 추가
list_f = list(fruits)
list_f.append("grape")
list_t = tuple(list_f)
print(list_t)

# 패킹, 언패킹 기능
tp = 1, 2, 3
print(tp) # 패킹

x, y, z = tp # 언패킹(함수의 결과를 여러 변수에 나눠 받을 때)
print(z)

# 두 값을 바꾸기
a = 10
b = 20
a, b = b, a
print(f"a = {a}, b = {b}")

# 투플의 일부를 리스트로 받기
tp = (1, 2, 3, 4, 5, 6, 7, 8)
# tp 값을 변수로 나누어서 할당
v1, v2, v3, *v4, _ = tp
print(v4)

# 함수의 리턴 값을 투플로 받기
# function -> def(define)
def get_min_max(nums):
    return min(nums), max(nums) # 리턴 값을 투플로 전달

low, high = get_min_max([5, 3, 9, 1, 7]) # 함수 실행 결과를 언패킹
print(f"최솟값: {low}, 최대값: {high}")