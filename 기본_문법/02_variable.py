# 일반적인 주석
"""
큰따옴표 3개는 주석의 영역
이 안의 내용을 모두 주석
"""
# 올바른 변수명
# 변수명은 무조건 영문, _, 한글 변수명 지원
# snake_case 일반으로 표현
user_name = "홍길동"
_score = 90
나이 = 25
print("이름:", user_name)
print("나이:", 나이)

# 실수
grade = 3.7
print("grade:", grade)

# 논리값
result = True
print("Result:", result)

# 재할당
result = "결과"
print("Result:", "결과")

# 메모리에서 명시적으로 변수 할당 삭제
y = 100
del y
print(y)