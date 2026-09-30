# 18_module_test.py를 현재 파일로 끌어온다.
# import는 완성된 파이썬 파일(라이브러리)를 가져온다.
# 우리가 만든 모듈은 같은 폴더에 존재해야 한다.
import greeting

print("main_test.py에서 __name__ 값:", __name__)
print("import만 했을 뿐, hello()가 자동 실행되지 않은 것을 확인하세요.")
greeting.hello()