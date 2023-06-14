# '1'의 메소드 확인 할 수 있는 함수
# print(dir('1'))

# 1. 문자열 메소드

# .capitalize()
# 문자열의 자료구조가 가지고 있는 기능 capitalize 라는 메소드
# greeting ='hello my NAME is junhyuk'
# print(greeting.capitalize())
# print(greeting)

# .title()
# print(greeting.title())

# .upper()
# print(greeting.upper())

# .lower()
# print(greeting.lower())

# .join(iterable : 반복가능한 개체, 시퀀스 데이터)
a = ['hi', 'my', 'name']
# print(', '.join(a))

# .replace(old, new[, count])
# 대괄호는 옵셔널하다 -> 넣어도 되고 안넣어도 된다
# print('wooooooow'.replace('o', '!', 3))


# .strip([chars])
str_l = '            hello\n'
str_r = 'hellohihihihi'
# print(str_l.strip())
# left strip
# print(str_l.lstrip())
# right strip
# print(str_r.rstrip('hi'))


# .find(x)
a = 'apple'
# print(a.find('p'))
# print(a.find('z'))


# .index(x)
a = 'apple'
# print(a.index('a'))
# find 는 에러 발생 X index는 없으면 에러발생
# print(a.index('z'))


# .split(x)
a = 'my_name_is_junhyuk'
# print(a.split('_'))


# .isXXX => True, False를 리턴한다.


# 2. 리스트 메소드 -> 리스트는 뮤터블한 데이터 이므로 메소드를 적용시 데이터가 바뀐다

numbers = [5, 5, 5, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 4, 4]

# .append(x)
numbers.append(6)
# print(numbers)

# .extend(iterable)
# 원하는 리스트를 뒤에 붙이기 - 두 개의 리스트 연결
ex_numbers = [99, 100]
numbers.extend(ex_numbers)
# print(numbers)


# .insert(i, x) -> i번째 자리에 x 데이터를 삽입
# 내가 원하는 위치에 삽입
numbers.insert(3, 3.5)
# print(numbers)


# .remove(x)
numbers.remove(3.5)
# print(numbers)
# 이미 지워서 없는데 또 지우라고 하면 에러 발생
# numbers.remove(3.5)


# .pop(i) -> index
numbers.pop(0)
# print(numbers)


# .index(x)
# x 의 위치 찾기
# print(numbers)
# print(numbers.index(3))


# .count(x)
# print(numbers.count(4))


# .sort()
numbers.sort()
# print(numbers)
numbers.sort(reverse=True)
# print(numbers)


# .reverse()
# 거울 같이 대칭으로 만들어 줌
numbers.reverse()
# print(numbers)


# copy
# 같은 주소를 참조한다.
# 리스트에 해당! 변수는 아니다.
# origin_list = [1, 2, 3]
# copy_list = origin_list

# copy_list[0] = 100

# print(origin_list)
# print(copy_list)
# print(id(origin_list))
# print(id(copy_list))


# copy 복사 방법
# 슬라이싱
a = [1, 2, 3]
b = a[ : ]
# b = list(a) 라고 표현해도 된다.

b[0] = 100

# print(a)
# print(b)


# copy 얕은복사
a = [1, 2, [3, 4]]
b = a[:]

b[2][0] = 100

# print(a)
# print(b)


# copy 깊은복사
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

b[2][0] = 100

# print(a)
# print(b)


# .clear()
a = [1, 2, 3, 4]
a.clear()
# print(a)


# list comprehension

numbers = list(range(1, 11))

# 세제곱 만들기 for
result = []
for i in numbers:
    result.append(i**3)

# print(result)
# 세제곱 만들기 comp
result2 = [i**3 for i in numbers]
# print(result2)


# 짝수만 고르기 for
even_list = []
for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
# print(even_list)

# 짝수만 고르기 comp
even_list2 = [i for i in numbers if i % 2 == 0]
# print(even_list2)


# 연습
# 모음을 제거
words = 'my name is Min'
vowels = 'aeiou'

# 반복문 버전
result = []
for c in words:
    if c not in vowels:
        result.append(c)
        
# print(''.join(result))

# comp 버전
result2 = [c for c in words if c not in vowels]
# print(''.join(result2))


# 3. 딕셔너리 메소드

info = {
    'name': 'Min',
    'location': 'incheon',
    'phone': '123-123-123'
}


# .pop(key[, default])
info.pop('phone')
# print(info)
# print(info.pop('school', 'key가 없습니다.'))
# print(info)


# .update(key=value)
info.update(name='junhyuk')
# print(info)


# .get(key[, default])
# print(info['name'])
# print(info.get('name'))
# print(info['school'])
# print(info.get('school'))


# dictionary comprehension
# {1: 1, 2: 8, 3: 27}
cube_dict = {}
for i in range(1, 4):
    cube_dict[i] = i**3
# print(cube_dict)

cube_dict2 = {i: i**3 for i in range(1, 4)}
# print(cube_dict2)


# 연습
dust = {
    '서울': 100,
    '대전': 12,
    '인천': 70,
    '부산': 34,
    '전주': 67,
}

# 50 이상 지역만 뽑아서 새로운 dict 만들기
# for
l_dict = {}
for l, d in dust.items():
    if d >= 50:
        l_dict[l] = d
# print(l_dict)        

# comp 
l_dict2 = {l: d for l, d in dust.items() if d >= 50}
# print(l_dict2)

result3 = {k: '나쁨' if v >= 50 else '좋음' for k, v in dust.items()}
# print(result3)


# 4. 세트 메소드

fruits = {'apple', 'banana', 'melon'}

# .add(x)
fruits.add('watermelon')
# print(fruits)

# .update(*objects)
fruits.update('grape')
fruits.update({'orange', 'pear'})
# print(fruits)


# .remove(x)
fruits.remove('banana')
# print(fruits)
# 없을 때 제거하려면 에러 
# fruits.remove('dog')

# .discard(x)]
# 없어도 에러 안뜸
fruits.discard('dof')
# print(fruits)


# .pop()
# 임의의 원소 제거
# fruits.pop()
# print(fruits)



# 5. map(), zip(), filter()

# map(function, iterable 데이터)
number = [1, 2, 3]

number_str = map(str, number)
# print(number_str)
# print(list(number_str))

def cube(x):
    return x**3

cube_list = list(map(cube, number))
# print(cube_list)


# 1 2 3 4 5 6 7 8 9 10 => [1, 2, 3, 4, 5...]
# => 1 8 27 ... 1000

# numbers = input().split()
# result = map(int, numbers)
# print(list(result))

# numbers = list(map(int, input().split()))
# print(list(numbers))


# zip
a_number = [1, 2, 3]
b_number = [100, 200, 300]

# print(list(zip(a_number, b_number)))



# filter(function, iterable)
# function은 참/거짓이 반환되는 함수여야 한다.

def isodd(x):
#     if x % 2 == 1:
#         return True
#     else:
#         return False
    return bool(x % 2) 

numbers = [1, 2, 3, 4, 5]
result = filter(isodd, numbers)
print(list(result))














