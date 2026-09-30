text = "Python is fun, python is powerful"

# len(): 문자열의 길이
print("문자열의 수:", len(text))

# 특정 문자 포함 수: count()
print("Python 수:", text.count("Python"))
print("java 수:", text.count("java"))

# find(): 있을 때 -> index, 없을 때 -> -1 반환
print("Python 존재 여부:", text.find("Python"))
print("fun 존재 여부:", text.find("fun"))
print("java 존재 여부:", text.find("java"))

# 문자인지: isaplpha(), 숫자인지: isdecimal()
print("abc".isalpha()) # True
print("123".isdecimal()) # True

# upper(): 모두 대문자, lower(): 모두 소문자
# strip(): 좌우 공백 제거
# replace(): 변경
print(text.replace("Python", "Java"))
# 파이썬 리스트 => 자바의 Arraylist
# split(","): ,를 기준으로 나눈 후에 리스트를 리턴
print(text.split(","))