# Error

# 1. syntax error (문법 오류)
# if True:
#     pass
# else

# print('hi'

# if True print('hello')

# 2. exception (예외)

# ZeroDivisionError
# print(5/0)

# NameError
# print(my_name)

# TypeError
# print(1 + '1')
# print('1' + 1)

import random
# missing 1 required positional argument
# random.sample([1, 2])
# takes 3 positional arguments but 8 were given
# random.sample([1, 2], 1, 1, 1, 1, 1, 1)


# ValueError
# int('3.5')
# numbers = [1, 2, 3]
# numbers.index(100)


# IndexError : list index out of range
# numbers = [1, 2, 3]
# numbers[100]


# KeyError
# my_dict = {
#     'apple': '사과',
#     'banana': '바나나',
# }
# my_dict['melon']


# ModuleNotFoundError: No module named 'asdf'
# import asdf

# ImportError
# from datetime import asdf

# KeyboardInterrupt (ctrl + c 로 종료)
# while True:
#     continue


# 3. 예외 처리
# try:
#   code
# except 예외:
#   code

# try:
#     num = int(input('숫자를 입력해주세요 : '))
#     print(f'입력하신 숫자의 제곱은 {num**2}입니다.')
# except ValueError:
#     print(f'숫자를 입력하라고!')


# try:
#   code
# except (예외1, 예외2):
#   code

# try:
#     num = input('나눌 값을 입력해주세요 : ')
#     100 / int(num)
# except(ValueError, ZeroDivisionError):
#     print('문제발생')

# 각각의 에러를 따로 표현해주기
# try:
#     num = input('나눌 값을 입력해주세요 : ')
#     100 / int(num)
# except ValueError:
#     print('입력한 정보는 숫자가 아닙니다.')
# except ZeroDivisionError:
#     print('수학적으로 0으로 나누는 것은 불가능합니다.')


# 에러 메세지 변수처럼 사용 
# try:
#     my_list = []
#     print(my_list[5])
# except IndexError as err:
#     print(f'{err} : 오류가 발생했습니다.')    


# else 는 위에 except가 모두 동작하지 않으면 마지막에 동작하는 부분
# try:
#     my_list = [1, 2, 3]
#     print(my_list[100])
# except IndexError:
#     print('인덱스 에러입니다.') 
# else:
#     print('else')


# finally는 위에 except가 실행되더라도 동작한다.
# try:
#     my_list = [1, 2, 3]
#     print(my_list[2])
# except IndexError:
#     print('인덱스 에러입니다.') 
# finally:
#     print('finally')


# 강제로 에러가 나게끔 하는 코드 (테스트시 자주 활용)
# raise ValueError('테스트입니다.')


# 연습
# 양의 정수 두개를 받아 몫과 나머지로 출력하는 함수를 정의

def my_div(a, b):
    try:
        result1 = a // b
        result2 = a % b
    except ZeroDivisionError:
        print('수학적으로 0으로 나눌 수 없습니다.')    
    except:
        print('숫자를 입력하세요')
    else:
        return (result1, result2)

     
print(my_div(1, 0))
print(my_div('1', '5'))
print(my_div(6, 2))


