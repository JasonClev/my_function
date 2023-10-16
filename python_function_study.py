# 입력값이 없고 출력값도 없는 함수
def my_function():
    print("this is function")


my_function()


# 입력값이 있고 출력값은 없는 함수
def my_function2(x):
    print(x)


my_function2("start")


# 입력값이 있고 출력값도 있는 함수
def my_function3(x):
    return x*3


a = my_function3(7)
print(a)


def my_gugudan(x):
    for i in range(9):
        print((i+1) * x)


my_gugudan(3)


# 재귀함수
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)


print(factorial(5))


k = [i for i in "abcde"]
print(k)
