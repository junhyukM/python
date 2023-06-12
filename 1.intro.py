# 여기는 주석입니다.

# 안녕하세요
# 파이썬입니다.

# a라는 변수에 1이라는 숫자를 저장합니다.
a = 1 # a라는 변수에 1이라는 숫자를 저장합니다. 

# 1. 변수
# 변수이름 = 값
# 변수이름은 어떤 이름이든 상관 없음
# 단, 영어, 숫자, _(언더바)로 구성되어있고 키워드는 사용 불가

# 키워드(식별자)
import keyword
# print(keyword.kwlist)


# 1.1 number 

a = 10000000000000000
# print(type(a))

b = 1.1
# print(type(b))

# 실수 => 부동소수점으로 관리
c = 1.1
d = 1.12
# -0.0200000000018 이라고 뒤에 이상한 수가 붙는다
# print(c - d)

# complex
f = 1 - 4j
# print(type(f))

# 1.2 boolean

a = True
b = False

# print(type(a))
# print(type(b))

c = 1
d = 0

# print(bool(c))

# None
e = None
# print(type(e))

# 1.3 String (문자열)
greeting = 'hello'
name = 'min'

# print(greeting, name)
# print(type(name))

# age = input()
# print(type(age))

intro = '안녕하세요 저는 \'홍길동\'입니다.'
# print(intro)

#docstring
intro = """
안녕하세요
저는 홍길동입니다.
"""
# print(intro)

# string interpolation
dust = 100
message = '오늘 미세먼지 농도는 10입니다.'

message1 = '오늘 미세먼지 농도는 %s입니다.' % dust
# print(message1)

message2 = '오늘 미세먼지 농도는 {}입니다.'.format(dust)
# print(message2)

message3 = f'오늘 미세먼지 농도는 {dust}입니다.'
# print(message3)

# 2. 연산자
# 2.1 산술연산자
# + - * /
a = 10
b = 3

# // 몫
# print(a // b)

# % 나머지
# print(a % b)

# divmod -> 함수로 몫과 나머지 둘다 반환
# print(divmod(a, b))

# ** 거듭제곱
# print(a ** b)

# 2.2 비교연산자
# > < = 
a = 1
b = 2

# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)
# print('hi' == 'hi')
# print('hi' == 'hello')

# 2.3 논리연산자
a = True
b = False

# and (둘다 True이면 True) 
# print(a and a)
# print(a and b)
# print(b and a)
# print(b and b)
# or (둘 중에 하나라도 True이면 True)
# print(a or a)
# print(a or b)
# print(b or a)
# print(b or b)
# not 부정 -> True는 False로 False는 True로 바꿔줌
# print(not a)

# 2.4 복합연산자
# +=, -=, *=, /=, //=, **=
n = 0
# n = n + 1
while n < 5:
    # print(n)
    n += 1

# 2.5 기타연산자
# concatenation -> 문자열끼리 연결 가능 + 로 
#print('hello' + 'hi')

# in -> 앞에있는 무엇이 뒤의 무엇에 포함되어있는지?
# print('hi' in 'hihello')
# print(1 in [1, 2, 3])
# print(1 in range(1, 5))

# is
a = 'hi'
b = 'hi'
#print(a is b)

# 우선순위
# 3을 4제곱 한다음 -를 붙인거
# print(-3 ** 4)
# 괄호로 우선순위 지정
# print((-3) ** 4)

# 3. 형변환
# 3.1 임시적 형변환

# True는 1로 생각하고 계산해줌
# print(True + 3)

a = 3
# if a % 2:
    # print('홀수입니다.')

# 3.2 명시적 형변환
# print('미세먼지 농도 : ' + str(10))
# print(10 + int('20'))
# print(float('3.4'))
# print(float(2))
# print(int('2.5'))

# 4. 시퀀스 데이터
# 리스트(list), 튜플(tuple), 레인지(range), 문자열(string)

# 4.1 리스트
# 수정 가능 
# a = [value1, value2, value3...]
# a[index]
# +a : 파이썬에서는 list, 다른언어들에서는 array / 배열

a = []
b = list()
# print(type(a), type(b))

location = ['서울', '대전', '대구']
# print(location[2])
location[0] = '부산'
# print(location)

# 리스트 안에 다양한 형태
# 한 줄에 하나의 데이터를 작성
a = [
    [1, 2, 3],
    {4, 5, 6},
    (7, 8, 9),
] 

# print(a)

# 4.2 튜플
# 수정불가능(immutable)
# a = (value1, value2...)
# a[index]

a = (1, 2, 3, 4, 5)
# a[1] = 10 과 같이 수정을 하려고 하면 에러가 난다. 
# print(a[2])

# 각각 할당된다 -> 1이 b에 들어가고 2가 c에 들어감
# b, c = (1, 2)
# print(b)

# b, c = c, b
# print(b, c)


# 4.3 레인지
# range(n) : 0부터 n-1까지
# range(n, m) : n부터 m-1까지
# range(n, m, s) : n부터 m-1까지 s간격으로

a = range(5, 10, 2)
# print(list(a))


# 4.4 시퀀스에서 사용 할 수 있는 연산

# in
a = 'a'
b = ['a','p','p','l','e']
c = 5
d = range(10)
# print(a in b)
# print(c in d)

# concatenation
# 연결
a = [1, 2]
b = [3, 4]

# print(a + b)

# 반복
a = 'hi'
b = [123]
# print(a*5)
# print(b*5)

# indexing
# 문자열도 시퀀스 데이터기 때문에 가능
a = [1, 2, 3, 4]
b = 'hello'
c = range(10)
# print(a[1])
# print(b[1])
# print(c[5])
# 음수도 가능
# print(a[-2])
# print(b[-5])

# slicing
a = 'hello'
# print(a[1:3])
b = (1, 2, 3, 4, 5)
# print(b[1:3])
c = '123456789'
# print(c[1:10:2])
# print(c[::2])

# 함수
a = [1, 2, 1, 4, 5]
# print(len(a))
# print(a.count(1))


# 5. 시퀀스가 아닌 자료

# 5.1 set
# a = {value1, value2, ...}
# 순서가 없고 중복이 없음
a = {1, 2, 3, 4, 5, 5} # 5를 중복으로 작성해도 출력하면 하나만 나옴
b = {2, 4, 6, 8}

# 합집합
# print(a | b)
# 차집합
# print(a - b)
# 교집합
# print(a & b)

# 중복 데이터 날리고 list로 다시 바꾸기
a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(list(set(a)))

# 5.2 dictionary
# a = {key1: value1, key2: value2, ...}
# key는 immutable한 것만 가능

a = {}
a = dict()

book = {
    'apple': '사과', 
    'banana': '바나나',
}
# print(book['apple'])

# 뒤에 있는 key의 value가 덮어쓴다
b = {1: 1, 2: 2, 3: 3, 1: 4}
# print(b[1])
# print(b)
# print(b.keys())
# print(b.values())



# 정리

# 1. 시퀀스 (ordered)
# - 'String' : immutable
# - [list] : mutable
# - (Tuple) : immutable
# - range() : immutable

# 2. 시퀀스가 아닌것(unordered)
# - {set} : mutable
# - {Dict: ionary} : mutable
