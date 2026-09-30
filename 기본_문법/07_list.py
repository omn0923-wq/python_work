# 파이썬 리스트: 삽입/삭제가 자유롭고, 타입에 영향을 받지 않는다.
# 빈 리스트 정의
empty_list_1 = []
empty_list_2 = list()

empty_list_1 = [1, 2, 3]
print(empty_list_1)

empty_list_2 = [1, "hello", 3.14, True]
print(empty_list_2)

# 리스트 접근
sample = [10, 20, 30, 40, 50]
print(sample[0])
print(sample[-1])
# [20, 30] 출력
print(sample[1:3])
# 거꾸로 뒤집기
print(sample[::-1])

# 리스트의 함수
# append(): 맨 끝에 추가
my_list = [10, 20, 30]
my_list.append(40)
print(len(my_list))
# insert(): 위치 지정 삽입
my_list.insert(2, 25)
print(my_list)

# in: 리스트에 특정 엘리먼트가 포함되어 있는지 여부
f = ["바나나", "체리", "사과"]
is_exists = "사과" in f

if "사과" in f :
  index_apple = f.index("사과")
  print(index_apple)

# 블럭은 들여쓰기로...
# 해당 블럭을 벗어나려면 맨 앞으로... 이동...
# 리스트에 사용하는 함수
# sort() / reverse(): 원본을 바꾼다.
# sorted(), reversed(): 파이썬 자체 제공 함수 / 원본 바꾸지 않는다.  
print(f)
f.sort()
print(f)

result = list(reversed(f))
print(result)

# pop(인덱스): 맨 뒤에 꺼내고, 삭제
# remove(인덱스): 원하는 색인 위치 삭제
# max(), min()
# 리스트의 깊은 복사
# copy = list(리스트)