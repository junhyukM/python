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
# 리스트에 해당! 변수는 아니다. 근데 다른 자료구조는 어떤지 모른다. 알아봐야될듯
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










