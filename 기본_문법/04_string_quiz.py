my_var = "This is my python code."

# 다음 문자만 출력
# 1. p
# 2. . (맨 뒤 period)
# 3. python 출력
# 4. This is 출력

email = "gildong@gmail.com"
# find 함수를 이용: 특정 문자의 index 반환 함수
# 아이디만 출력

# 다음 이름이 거꾸로 해도 같은지 확인(True, False)
name_1 = "이효리"
name_2 = "우영우"

# 1.
print(my_var[11])
# 2.
print(my_var[-1])
# 3.
print(my_var[11:17])
# 4.
print(my_var[:7])
# 5. 
location = email.find("@")
print(email[:location])
# 6.
print(name_1[0:] == name_1[::-1])
print(name_2[0:] == name_2[::-1])