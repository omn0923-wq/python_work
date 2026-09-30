# 조건 판단: if ~ elif ~ else
# continue, break, return

# 점수를 입력받아서 10점이 넘으면 합격입니다. 불합격입니다.
score = int(input("점수 입력: 10점 이상이면 합격"))
if score >= 10:
    print("합격")
else:
    print("불합격")

# 점수를 입력받아서 A, B, C, D, F 중 하나 출력하기
# score = int(input("점수 입력 (0~100)"))

if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")

# 자바: switch ~ case
# 파이썬 3.10 버전 이상: match ~ case
# score = int(input("점수 입력 (0~100)"))

match score:
    case x if 90 <= score <= 100:
        print("A")
    case x if 80 <= score <= 90:
        print("B")
    case x if 70 <= score <= 80:
        print("C")
    case x if 60 <= score <= 70:
        print("D")
    case _:
        print("F")