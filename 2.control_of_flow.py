# 1. 제어문

# 1.1 조건문
# if <조건식>:
#     if의 조건식이 참인경우 실행하는 코드
# elif <조건식>:
#     elif의 조건식이 참인경우 실행하는 코드
# else:
#     거짓인 경우 실행하는 코드

a = 10
if a > 5:
    pass
elif a > 8:
    pass
else:
    pass


# 연습1
# 사용자에게 날짜 입력을 받아서 크리스마스인지 확인하는 코드

# a = input('날짜를 입력하세요(ex: 1/1, 12/12) : ')

# if a == '12/25':
#     print('크리스마스입니다.')
# else:
#     print('크리스마스가 아닙니다.')


# 연습2
# 사용자에게 숫자하나를 입력 받아서 홀수인지 짝수인지 확인하는 코드

# a = int(input('숫자를 하나 입력해주세요 : '))

# if a % 2:
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')


# 연습3
# 사용자에게 1~100 점수를 입력받아서
# 100~90 : A, 89~80 : B, 79~70 : C, 나머지 F
# 95점 이상인 사람에게는 good이라는 문장을 추가로 출력

# a = int(input('점수를 입력하세요 : '))

# if a >= 90:
#     print('A')
#     if a >= 95:
#         print('good')
# elif a >= 80:
#     print('B')
# elif a >= 70:
#     print('C')
# else:
#     print('F')


# 1.2 조건표현식
# true_value if <조건식> else false_value

# 홀수, 짝수 판별
# num = int(input('숫자를 입력하세요 : '))

# result = '홀수' if num % 2 else '짝수'
# print(result)


# 숫자를 입력받아 양수라면 그 값을 음수라면 0으로 받는 조건문
# 조건표현식으로 작성해보기
# num = int(input('숫자를 입력하세요 : '))
# value = num if num >= 0 else 0
# print(value)


# 1.2 반복문

# 1.2.1 while
# while 조건식이 True인 경우 반복적으로 코드를 실행
# while <조건식>:
#     반복할 코드

# n = 0
# while n < 5:
#     print('아직은 5보다 작습니다.')
#     n += 1


# greeting = ''
# while greeting != 'hi':
#     greeting = input('안녕! \n')


# 1.2.2 for
# for variable in sequence:
#     실행할 코드

# for i in range(5):
#     print(i)


# 연습1
# 사용자에게 영단어 하나를 받아서 알파벳 하나씩 출력 시키는 코드

# word = input('단어를 입려해주세요 : ')
# for i in word:
#     print(i)

# 표현시 numbers 와같이 복수형으로 작성해서 for 문에 사용하는것이 보통이다.
# 외부에서 사용하는 변수와 for 문의 variable 변수를 같은 이름으로 쓰면 안된다. 외부에 있는 변수가 바뀌어버린다.
# number = 123
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)
# print(number)


# 연습2
# 반복문과 조건문을 같이 사용해서 1~20까지의 숫자중에
# 홀수만 저장된 numbers 리스트를 출력해주세요

# numbers = []
# for i in range(1, 21):
#     if i % 2:
#         numbers.append(i)
# print(numbers)


# 연습3
# 점심메뉴 리스트를 작성해서 하나씩 출력

menus = ['라면', '김밥', '돈까스', '삼겹살']

# for i in range(len(menus)):
#     print(menus[i])

# for idx, menu in enumerate(menus):
    # idx, menu = (0, '라면')
    # idx, menu = (1, '김밥')
    # idx, menu = (2, '돈까스')
    # idx, menu = (3, '삼겹살')
    # print(idx, menu)


# 1.2.3 dictionary 반복

info = {
    'name': 'min',
    'location': 'seoul',
}

# for i in info:
#     print(f'{i}, {info[i]}')

# 1. dictionary (key 반복)
# for key in info:
#     print(key)

 # 2. key반복
# for key in info.keys():
#     print(key)   

# 3. value 반복
# for value in info.values():
#     print(value)

# 4. key, value 반복
# for key, value in info.items():
#     print(key, value)

# print(info.keys())
# print(info.values())
# print(info.items())


blood_type = {
    'A': 10,
    'B': 8,
    'O': 5,
    'AB': 5,
}

# 1. 혈액형 종류는 다음과 같습니다. A, B, O, AB
# 2. 혈액형 종류는 다음과 같습니다. A, B, O, AB
# 3. 학생수는 28명 입니다.
# 4. A형은 10명입니다...

# 1, 2   keys() 유무가 결과에 영향 X 
# result = []
# for key in blood_type.keys():
#     result.append(key)
# # ', ' 문자열 객체의 join이라는 메소드    
# result = ', '.join(result)
# print(f'혈액형 종류는 다음과 같습니다. {result}')

# 3.
# result = 0
# for value in blood_type.values():
#     result = result + value
# print(f'학생수는 {result}명 입니다.')    

# 4.
# for k, v in blood_type.items():
#     print(f'{k}형은 {v}명입니다.')


# 1.2.4 break

# for i in range(10):
#     if i > 2:
#         print('2초과입니다.')
#         break
#     print(i)    


# 연습
# rice = ['보리', '보리', '보리', '쌀', '보리' '보리']

# for i in rice:
#     if i == '쌀':
#         print('잡았다')
#         break
#     print(i)


# 1.2.5 continue

# for i in range(5):
#     if i % 2:
#         continue
#     print(f'{i}는 짝수입니다.')

# 연습
# 20살 이상이면 '성인입니다' 미만이라면 X
# age = [6, 70, 15, 34, 65, 10, 30, 20, 60, 4]

# for i in age:
#     if i < 20:
#         continue
#     print(f'{i}살은 성인입니다')


# 1.2.6 else

# for i in range(50):
#     print(i)

#     if i == 5:
#         print(f'{i}번째에서 break')
#         break
# else:
#     print('break를 만나지 않았습니다.')

# 연습
numbers = [1, 5, 10]
# print(5 in numbers)

for number in numbers:
    # if문으로 내가 원하는 숫자가 있으면
    if 5 == number:
        print(True)
        break
    # => True
    # 원하는 숫자가 없으면 (끝까지 다 확인했지만 if문을 거치는게 없는 경우)
    # => False
else:
    print(False)
