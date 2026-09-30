weather = "흐림"
temp = 15.8

# % 연산자 (%s: 문자, %d: 정수, %f: 실수)
res_1 = "오늘 날씨는 %s입니다. 기온은 %f도 입니다." %(weather, temp)
print(res_1)

# .format()
res_2 = "오늘 날씨는 {0} 입니다. 기온은 {1}도 입니다.".format(weather, temp)
print(res_2)

# f-string 방식
res_3 = f"오늘 날씨는 {weather}이고, 기온은 {temp}입니다."
print(res_3)

price = 1200
qty = 3
print(f"총 금액은 {price * qty}원 입니다.")

# """ """: system or user prompt 작성 시 자주 사용
name = "홍길동"
age = 20
text = f"""
이름: {name}
나이: {age}
"""
print(text)

# 형변환
num_str = "100"
num_int = int(num_str)
print(num_int + 1)

num_float = float("3.5")
print(num_float * 2)

age = 25
print("나이는 " + str(age) + "살 입니다.")


num_1 = int(input("첫 번째 숫자를 입력하세요. "))
num_2 = int(input("두 번째 숫자를 입력하세요. "))
print(f"두 수의 합은 {num_1 + num_2}입니다.")