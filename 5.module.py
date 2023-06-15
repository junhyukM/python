# 1. 모듈

# import fibo

# import로 함수 불러와서 실행하기
# print(fibo.fib_for(5))
# print(fibo.fib_re(3))

# 함수도 변수에 저장 할 수 있다.
# 괄호가 있으면 실행을 한다는 뜻 괄호가 없으면 정의를 가져와서 옆에 변수에 저장하겠다는 뜻
# 만약 괄호가 있다면, 함수의 결과를 변수에 저장하라의 뜻이 된다.
# 괄호를 작성하지 않았으므로 함수자체를 변수에 저장하게 된다.
# my_fib = fibo.fib_for
# print(my_fib(4))


# 2. 패키지

# 패키지 안에 __init__.py가 있어야 패키지로 인식 한다
# myPackage/
#    __init__.py
#    math/
#        __init__.py
#        fibo.py
#        formula.py

# (from 경로) import 모듈 (as 변경할 이름) 괄호는 생략 가능


# import myPackage
# print(myPackage)


# 파일을 불러오는 경우
# from myPackage.math import formula
# print(formula.pi)
# print(formula.my_max(1, 2))


# * 를 이용해 그 파일이 가지고 있는 모든 값을 다 가지고 오는 경우
# from myPackage.math.formula import *
# print(my_max(1, 54))


# 이미 지정해서 사용하던 변수와 파일 명이 같을 때
# formula = 123
from myPackage.math import formula as f
# print(formula)
# print(f)


# 3. 모듈 사용해보기
# 3.1 math

# 파이썬 내장 라이브러리/ 패키지이르모 그냥 호출하면된다
import math

# print(math.pi)
# print(math.e)

pi = math.pi
# print(math.ceil(pi))
# print(math.floor(pi))
# print(math.trunc(pi))

# print(math.pow(2, 5))
# print(math.sqrt(9))


# 3.2 random

import random

# print(random.random())
# print(random.randint(1, 10))

# seed
# 난수를 발생시키지만 동일한 순서로 발생시켜야 할때

# random.seed(2)
# print(random.random())


# shuffle
a = [1, 2, 3, 4, 5]
random.shuffle(a)
# print(a)


# choice
result = random.choice(a)
# print(result)

# sample
result2 = random.sample(a, 2)
# print(result2)


# 3.3 datetime
from datetime import datetime
now = datetime.now()
# print(now)

today = datetime.today()
# print(today)

utc = datetime.utcnow()
# print(utc)

result = now.strftime('%Y년 %m월 %d일')
# print(result)

result2 = now.strftime('%d / %m / %y')
# print(result2)

# 년도
# print(now.year)
# 요일 (0~6 / 월~일)
# print(now.weekday())


birth = datetime(2023, 1, 1, 13, 30)
# print(birth.strftime('%m / %d는 내 생일이야'))


from datetime import timedelta

future = timedelta(days=3)
print(future)

print(birth + future)
print(now + timedelta(days=100))

christmas = datetime(2023, 12, 25)
diff = christmas - now
print(diff.total_seconds())
