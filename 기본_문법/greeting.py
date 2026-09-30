def hello():
    print("안녕하세요.")

# __name__: 현재 실행된 모듈의 이름
print(f"현재 __name__ 값: {__name__}")

# if __name__ == "__main__": 구문은 현재 모듈을 python으로 실행할 떄만 구동
# 현재의 18_moule_test.py가 다른 파이썬 파일에 불려져서
# 호출될 때는 if __name__ == "__main__":가 실행되지 않는다.
if __name__ == "__main__":
    hello()