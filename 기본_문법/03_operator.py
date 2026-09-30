int_value = 40
var = 42

print(var + 10)
print(var - 10)
print(var / 10)
print(var // 10) # //: 몫
print(var % 5) # %: 나머지
# divmod(): 몫과 나머지를 동시에 구하는 함수
a = 17
b = 5
q, r = divmod(a, b)
print(q)
print(r)

# 논리 연산
is_true = True
is_false = False
# 논리 연산자: and, or, not
print(is_true and is_false) # False
print(is_true or is_false) # True
print(not is_true) # False
