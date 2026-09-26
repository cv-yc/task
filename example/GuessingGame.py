from random import randint

def set_range():
    while True:
        try:
            lower = int(input("输入下界（整数）："))
            upper = int(input("输入上界（整数）："))
            if lower > upper:
                print("下界不能大于上界，请重新输入")
            else:
                break
        except ValueError:
            print("输入的不是有效数字")
    return randint(lower, upper)


def get_guess():
    while True:
        try:
            return int(input("请输入猜测的数字（整数）："))
        except ValueError:
            print("输入的不是有效数字")


def game_loop(secert_num):
    total = 0
    while True:
        user_guess = get_guess()
        total += 1
        if user_guess < secert_num:
            print("小了")
        elif user_guess > secert_num:
            print("大了")
        else:
            print("猜对啦！")
            print(f"共猜测{total}次")
            break


def main():
    print(
        "这是一个猜数游戏输入你要猜的数字范围（整数）\n系统会随机生成一个整数\n你来猜这个数字是多少。"
    )
    secert_num = set_range()
    game_loop(secert_num)


if __name__== "__main__":
    main()
#面向AI    
#ruff
#pytest
#mypy
#justfile=makefile
