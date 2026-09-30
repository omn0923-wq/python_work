# for 변수명 in 시퀀스: 
#   반복할 문장
#   break
# else:
#   break가 안 걸리고 for가 종료되었을 때
# enumerate(): 인덱스와 값을 같이 돌릴 때
fruits = ["사과", "바나나", "귤"]

for idx, value in enumerate(fruits, start=1):
    print(idx, value)

nums = [1, 3, 5, 7, 9]
# 리스트 안에 짝수가 발견되면 중간에 빠져나오기
# break가 안 걸리면 "모두 홀수예요."

for n in nums:
    if n % 2 == 0:
        print("짝수 발견")
        break
else:
    print("전부 홀수예요.")

# while
# 1~10까지 더하는 프로그램

total = 0
i = 1
while i <= 10:
    total += i # total + total + 1
    i += 1 # i = i + 1
    pass # 구조 만들어 놓고 나중에 코딩할 때

print(total)