str_1 = "PYTHON!"

# 파이썬의 모든 문자열을 담고 있는 변수는 오브젝트이다.

print(str_1[0])
print(str_1[-1]) # 음수의 색인은 맨 뒤부터 앞으로 진행

# 문자열의 슬라이싱
# 전체 출력
print(str_1[0:])
print(str_1[:-1])
# 파이썬에서 색인 범위를 지정: 시작 값~(끝값-1)
# 0~2번: PYT가 출력
print(str_1[0:3])

# YTHO
print(str_1[1:5])

#ON!
print(str_1[4:])
print(str_1[-3:])

# 색인의 구조 (시작:끝:중분)
print(str_1[::2])
# 문자열을 거꾸로 출력하기
print(str_1[::-1])