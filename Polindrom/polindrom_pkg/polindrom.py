import sys

def is_polindrom(word):
    return word == word[::-1]

def main():
    print("main started")
    if len(sys.argv) > 1:
        input_word = sys.argv[1]
        if is_polindrom(input_word):
            print("Это палиндром.")
        else:
            print("Это не палиндром.")
    else:
        print("Пожалуйста, укажите слово как аргумент командной строки.")

if __name__ == "__main__":
    main()
