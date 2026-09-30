# 리스트의 함축 문법
# [    i 처리식 for i in 리스트 조건문   ]
# range(10)를 이용해서 회전수를 정한다.
# 0~9까지 총 10회 루프
# for i in range(10):
#     print(i)

# 문제 1. [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 을 생성
s = [i**2 for i in range(10)]
print(s)

# 문제 2. [0, 4, 16, 36, 64] 을 생성
s = [i**2 for i in range(10) if i % 2 == 0]
# for i in range() 뒤에 cond. filter가 붙고 순서는 for i in range() -> if -> 맨 앞 i

# 문제 3. str="All good things must come to an end."를 단어별로 나누고
# 각 단어의 첫 글자만 리스트로 저장 (결과는 소문자로)

str = "All good things must come to an end."

# 1. str을 공백 기준으로 배열로 변환
# 2. 순회하면서 각 배열 요소의 첫 번째 인덱스에 해당하는 문자를 소문자
result = str.split(" ")
r = [word[0].lower() for word in str.split()]
# print(r)
r_1 = list()
for w in result:
    r_1.append(w[0].lower())
print(r_1)

# 문제 4. 1~20 사이의 숫자 중 3의 배수만 골라 리스트로 만들기
arr = [i for i in range(1, 21) if i % 3 == 0]
print(arr)

# 문제 5. 단어 리스트에서 길이가 5 이상인 단어만 대문자로 변환하기
words = ["cat", "python", "dog", "elephant", "ai"]
arr = [word.upper() for word in words if len(word) >= 5]
print(arr)

# 문제 6. 1~20 사이의 홀수만 리스트로 생성하시오.
arr = [i for i in range(1, 21) if i % 2 == 1]
print(arr)

# 문제 7. 단어 리스트의 각 단어 길이를 저장한 리스트를 생성하시오.
words = ["apple", "banana", "kiwi", "grape"]
words_length = [len(word) for word in words]
print(words)

# 문제 8. 문자열에서 숫자만 추출하여 리스트를 생성하시오.
text = "a1b2c3d4e5"
digit_text = [t for t in text if t.isdigit()]
print(digit_text)

# 문제 9. 단어 리스트에서 길이가 4 이상인 단어만 저장하시오.
words = ["cat", "python", "dog", "elephant", "ai"]
arr = [word.upper() for word in words if len(word) >= 4]
print(arr)

# 문제 10. 문자열의 각 문자를 소문자로 변환하여 리스트를 생성하시오.
text = "PyThOn"
s = [text.lower() for text in text.split()]
print(s)

lower_text = [ch.lower() for ch in text]
print(lower_text)

# 문제 11. 1~10 사이 숫자 중 3의 배수만 리스트로 생성하시오.
result = [i for i in range(3, 11, 3)]
print(result)

# 문제 12. 단어 리스트의 첫 글자만 저장하시오.
words = ["apple", "banana", "kiwi", "grape"]
r = [word[0] for word in words]
print(r)

# 문제 13. 문자열에서 알파벳만 추출하여 리스트를 생성하시오.
text = "a1b2c3d4"
alpha_text = [t for t in text if t.isalpha()]
print(alpha_text)

# 문제 14. 단어 리스트를 모두 대문자로 변환하시오.
words = ["python", "java", "c"]
s = [words.upper() for words in words]
print(s)

# 문제 15. 1~10의 제곱값을 리스트로 생성하시오.
# 결과: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
r = [i**2 for i in range(1, 11)]
print(r)

# 문제 16. 문자열이 팰린드롬(회문)인 단어만 골라내시오.
words = ["level", "python", "noon", "hello", "racecar"]
r = [w for w in words if w == w[::-1]]
print(r)

# 문제 17. 구구단 2단을 리스트로 생성하시오 (2×1 ~ 2×9).
# 결과: [2, 4, 6, 8, 10, 12, 14, 16, 18]
r = [i*2 for i in range(1, 10)]
print(r)

# 문제 19. 숫자 리스트에서 짝수는 "짝수", 홀수는 "홀수"로 변환하시오.
nums = [1, 2, 3, 4, 5]
# 결과: ['홀수', '짝수', '홀수', '짝수', '홀수']
r = ["짝수" if i % 2 == 0 else "홀수" for i in nums]
print(r)

# 문제 20. 단어 리스트에서 각 단어가 "a"로 시작하면 그대로, 아니면 빈 문자열로 저장하시오.
words = ["apple", "banana", "avocado", "grape", "ant"]
x = [x if x.startswith("a") else "" for  x in words ]
print(x)

# 결과: ['apple', '', 'avocado', '', 'ant']