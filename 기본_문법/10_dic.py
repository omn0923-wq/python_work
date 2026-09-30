# 딕셔너리 자료 구조는 자바의 map과 동일하게 생각
# 키와 값의 쌍으로 구성
# 접근: 이름["키"]
# keys(), values(), items(): 키와 값의 쌍을 얻어오기
# get(key)
# pop(key): 키 값에 저장된 값 얻어온 후 삭제
# key in dict: 키가 존재하는지 확인
# 딕셔너리의 표기법은 json 타입과 동일
person = {"name": "장원영","age": 21, "주소": "서울"}
print(person["name"])
detail = {"국적": "대한민국", "성별": "여자"}

jang = {"name": "장원영","age": 21, "주소": "서울", "detail": detail}
print(jang)
# 값 수정하기
jang.update({"age": 22})
print(jang)

# keys(), values(), items()
print(person.keys())
print(person.values())
print(person.items())

# 키 값 존재 확인
print("age" in person) # True

# 꺼내고 삭제
age_value = jang.pop("age")
print(jang)

# 키 삭제(del)
del jang["detail"]["국적"]
print(jang)

# 리스트 컴프리헨션으로 딕셔너리 만들기
sq = {n: n**2 for n in range(1, 6)}
print(sq)