from person import Person

if __name__ == "__main__":
    jang = Person("장원영", 21)
    print(jang.hello)

    try:
        jang.update_age(-1)
    except ValueError as e:
        print(f"나이 변경 실패: {e}")

    print(jang.dance())