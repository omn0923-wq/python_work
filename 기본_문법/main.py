# my_package 내의 두 개 모듈을 임포트 해서 테스트
# from 패키지 import 모듈
from my_package import math_module, string_module
import sys # 모듈
print(sys.path)

if __name__ == "__main__":
    print(math_module.add(3, 4))
    print(string_module.shout("hello"))