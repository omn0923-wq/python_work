# 변수의 생명 주기
# 지역변수, 전역변수

# 파이썬의 전역변수: global 키워드를 사용, 매번 써야 됨.

# 기본 전역변수: 현재 모듈에서 공통 사용
# count는 공용의 목적으로 선언
count = 0

def increase():
    # 지역변수
    count = 3
    count += 1
    print(f"increase 함수 안의 count: {count}")

increase()
print(f"밖에서 선언한 count: {count}")

def decrease():
    # 밖에서 선언한 count 변수를 전역변수로 같이 쓸게...
    global count
    count -= 1

decrease()
print(f"밖에서 선언한 count: {count}")