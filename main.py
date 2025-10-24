import pyperclip

def main():
    while True:
        print("\n===== 🔥히토미 품번복사기!🔥 =====")
        choicevnaqjs = input("품번 입력: ")
        print(f'링크 복사 완료! 품번: {choicevnaqjs}')
        pyperclip.copy(f'https://hitomi.la/galleries/{choicevnaqjs}.html')
        input("\n(ENTER 키를 누르면 종료...)")
        break


if __name__ == "__main__":
    main()