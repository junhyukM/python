# 함수 (function)

height = 100
width = 50
# 사각형의 둘레: 300, 넓이는 5000입니다.
## print(f'사각형의 둘레: {2*(height + width)}, 넓이: {(height * width)}입니다.')
# perimeter = 2 * (height + width)
# area = height * width
# print(f'사각형의 둘레: {perimeter}, 넓이: {area}입니다.')
# 같은 기능을 다른 변수로 하길 원하는 경우가 있다. 이럴때 기능의 재사용을 위해 함수를 이용한다.


# 1. 함수의 선언
# parameter -> 매개변수
# def func(parameter1, parameter2...):
#     code line1
#     code line2
#     ...
#     return value

def rectangle(height, width):
    perimeter = 2 * (height + width)
    area = height * width
    print(f'사각형의 둘레: {perimeter}, 넓이: {area}입니다.')

# 2. 함수의 호출
# argument -> 인수
# func(args1, args2) 

# rectangle(100,100)
# rectangle(200,100)

# 3. 연습

# print(max(10, 5))
# def my_max(num1, num2):
#     if num1 - num2 > 0:
#         print(f'{num1}이 더 큽니다.')
#     elif num1 - num2 < 0:
#         print(f'{num2}이 더 큽니다.')
#     else:
#         print('두 수가 같습니다.')    
    # return None
    # 리턴을 작성하지 않으면 파이썬은 자동으로 return None을 하게된다.

# result = my_max(34, 34)
# print(result)

# 4. return
def my_max(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return num1

# result = my_max(1, 2)
# print(result)


# 5. 인자 (parameter)

# 5.1 위치 인자

# def cylinder(r, h):
#     return r**2 * h * 3.14 

# print(cylinder(5, 10))
# print(cylinder(10, 5))
# print(cylinder(1))


# 5.2 기본값
# def func(args=value):
#     return args

def greeting(name='이름없음'):
    print(f'{name}님 안녕하세요!')

# greeting('홍길동')
# greeting('이순신')
# 아무것도 입력하지 않으면 기본값이 자동으로 들어가서 호출한다
# greeting()

# 기본값이 있는 args 앞에 작성하면 안된다.
# def greeting(name='이름없음', location): XX
#     print(f'{name}님 {location}에서 접속했습니다.')
# greeting('홍길동', '서울') 
# greeting('서울')


# def greeting(location, name):
#     print(f'{name}님 {location}에서 접속했습니다.')

# 순서달라도 이렇게 억지로 파라미터를 지정하면 사용 가능
# greeting(name='홍길동', location='서울')
# 근데 이건 안됨. 항상 위치인자를 먼저 사용해야하기 때문에
# greeting(location='서울', '홍길동')


# print(*objects, sep= ' ', end='\n', file=None, flush=False)
# print('hello')
# print('hello', end='????')
# print('hello', 'hi', sep='/')

# 5.3 가변 인자 리스트
# def func(*args):
#     code...
#     return ...

# 내가 푼 답.. 틀림
def my_max(*numbers):
    # 빈 리스트 생성
    result = [0]
    for n in numbers:
        if n > result[0]:
            result[0] = n
    return result[0]

# print(my_max(1, 2, 3, 5, 245, 5, 6))
# print(my_max(1, 2, 26, 7, 8))
# print(my_max(-1, -2, -3, -4, -5))

# 강의 풀이
def my_max(*numbers):
    result = 0
    
    for idx, number in enumerate(numbers):
        # 만약 for문의 첫번째 라면 제일 큰 수로 설정
        if idx == 0:
            result = number
        # 만약 첫번째가 아니라면 비교
        else:
            if result < number:
                result = number

    return result        

# result = my_max(1, 2, 3, 4, 5, 100, 1000)
# print(result)
# result = my_max(-1, -2, -3, -4, -5)
# print(result)


# 5.4 정의되지 않는 키워드 인자 처리

# def func(**kwargs):
#    code...

def fake_dict(**kwargs):
    result = []
    for k, v in kwargs.items():
        result.append(f'{k}: {v}')
    print(', '.join(result))


# fake_dict(name='홍길동', location='서울')

# def user(username, password, password_confirm):
#     if password == password_confirm:
#         print(f'{username}님 회원가입이 완료되었습니다.')
#     else:
#         print('비밀번호가 일치하지 않습니다.') 

# user('홍길동', '1234', '12034')

# my_user = {
#     'username': '이순신',
#     'password': 'qwer',
#     'password_confirm': 'qwer',
# }
# # 정의 할떄 말고 이렇게 사용도 가능한데 거의 안씀
# user(**my_user)


# 6. lambda
# lambda parameter: expression(표현식, 코드)

# def my_sum(a, b):
#     return a + b

# result = my_sum(1, 5)
# print(result)

# print((lambda a, b: a + b)(1, 2))


def make_incrementor(n):
    return lambda x: x + n

# 변수에 함수 저장
f = make_incrementor(42)
# 아래와 같다
#f = lambda x: x + 42
# 아래와 같은 느낌
##def f(x):
##    return x + 42

# print(f(100))



# 7. 이름공간 및 스코프(scope)
# LEGB
# 1번부터 우선순위
# 1. Local : 정의된 함수 내부
#   - 함수가 실행된 시점 이후부터 리턴 할 때 까지 존재
# 2. Enclosed : 상위 함수 (람다 때 참고)
#   - 함수가 실행된 시점 이후부터 리턴 할 때 까지 존재
# 3. Global : 함수 밖 or import 된 모듈
#   - 모듈이 호출된 시점 이후 끝까지 존재
# 4. Built-in : 파이썬에 내장되어있는 함수 혹은 변수
#   - 파이썬이 실행된 이후 끝까지 존재

# 기존의 함수와 같은 이름으로 변수를 만들어 보면
# 문제가 생긴다.
# Local scope 에서 print를 변수로 저장했기 때문이다.
# print = 'hello'
# print(print)

a = 1
def localscope(a):
    print(a)
# localscope(10)

# 전역 변수 건드린다.
# 아래와 같이 하면 전역 변수가 수정이 일어난다.
global_a = 1
def localscope2():
    global global_a
    global_a = 2
    print(global_a)

# localscope2()
# print(global_a)



# 8. 재귀 함수 (recursive function)

# 팩토리얼 반복문
def fact(n):
    #1부터 n까지의 수를 곱하기
    result = 1
    for i in range(1, n+1):
        result *= i
    return result    
# print(fact(5))

# 팩토리얼 재귀
# f(3)
# 3 * f(2)
# 3 * 2 * f(1)
# 3 * 2 * 1
# 3 * 2
# 6
# 팩토리얼 함수 안에서 다시 팩토리얼 함수를 return
# 함수안에 함수안에 함수안에 함수안에 함수안에 함수안에 함수안에 ...

def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)

# print(factorial(5))


# 피보나치 수열 반복문
def fib(n):
    result = [1, 1]
    for i in range(1, n):
        end1 = result[-1]
        end2 = result[len(result) - 2]
        fib_num = end1 + end2
        result.append(fib_num)

    return result[-1]

# print(fib(1000))
    
# 피보나치 수열 재귀
def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
   
# print(fib(10))




















