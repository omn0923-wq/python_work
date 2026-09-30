"""
 try:
    실행 구문
 except:
    예외 처리
 else:
    예외가 일어나지 않았을 때
 finally:
    무조건 실행 처리
"""
# 두 수를 입력받아서 0으로 나눌 때 오류 처리
while True:
 try:
    num1 = int(input("첫 번째 숫자: "))
    num2 = int(input("두 번째 숫자: "))
    result = num1 / num2
 except ValueError:
    print("숫자만 입력하세요.")
 except ZeroDivisionError:
    print("0으로 나눌 수 없어요.")
 else:
    print(f"결과: {result}")
    break
 finally: 
    pass