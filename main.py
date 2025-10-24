from mylib import myfunc

def main():
    turns = int(input("How many turns you want to run [4]: ") or 4)
    for i in range(1, turns + 1):
        print(myfunc("x", i))

if __name__ == "__main__":
    main()
