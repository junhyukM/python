# 객체지향 프로그래밍
# - 클래스(Class) : 같은 종류의 집단에 속하는 속성(attribute)과 행위(method)를 정의한것 
# - 인스턴스(instance) : 클래스를 실제로 메모리상에 할당한 것
# - 속성(attribute) : 클래스/인스턴스가 가지고 있는 데이터/값
# - 행위(method) : 클래스/인스턴스가 가지고 있는 함수/기능

number = 1 + 2j
# print(type(number))

# 속성(attribute)접근
# print(number.real)
# print(number.imag)

# 메소드 실행
my_list = [1, 4, 2, 3] 
# print(type(my_list))
# my_list.sort()


# 클래스가 없다면
# 다른 사람의 핸드폰을 만들때 이걸 다 복사해서 다 다르게 입력해야한다.
power = False
number = '010-1233-4556'
book = {
    '홍길동': '010-4251-2351',
    '이순신': '010-2541-2536',
}
model = 'iPhone12'

def on():
    global power
    if power == False:
        power = True
        print('핸드폰이 켜졌습니다.')

def off():
    global power
    if power == True:
        power = False
        print('핸드폰이 꺼졌습니다.')

def set_my_number(n):
    number = n

# on()
# off()

# 클래스
# class ClassName:
#   attribute...
#   method...

# 클래스 선언
class TestClass:
    a = 1
    
    def b(self):
        print('b')

# 인스턴스화
class_a = TestClass()
# print(class_a.a)
# class_a.b()


# 클래스가 있다면
class Phone:
    power = False
    number = '010-0125-2021'
    book = {}
    model = ''

    def on(self):
        if self.power == False:
            self.power = True
            print('핸드폰이 켜졌습니다.')

    def off(self):
        if self.power == True:
            self.power = False
            print('핸드폰이 꺼졌습니다.')

    def call(self, target):
        if self.power == True:
            print(f'내 번호는 {self.number}')
            print(f'{target} 전화 거는중')
        else:
            print('핸드폰 전원을 켜주세요')        



my_phone = Phone()
your_phone = Phone()

# my_phone.on()
# my_phone.power = True

# print(my_phone.power)
# print(your_phone.power)
# my_phone.number = '010-999-9999'
# my_phone.call('010-1111-1111')
# your_phone.call('010-2222-2222')


# p1 = Phone()
# self 자리에 들어가는 것은 인스턴스
# 두개의 표현이 같은 실행
# Phone.on(p1)
# p1.on()
# print(p1.power)



# 연습
class MyList:
    data = []

    def append(self, item):
        self.data += [item]
    # data안에 맨 마지막 요소를 삭제하고 삭제된 요소 하나 리턴
    def pop(self):
        num = self.data[-1]
        self.data = self.data[:-1]
        return num

        
list_a = MyList()
# print(list_a.data)
list_a.append(123) 
list_a.append(456) 
list_a.append(875) 
# print(list_a.data)

# print(list_a.data)
# list_a.pop()
# print(list_a.data)


# 정리
# class Person:   # => 클래스 정의(선언) : 클래스 객체 생성
#     name = 'hong'   # => 속성(attribute) : 변수/값/데이터

#     def hello(self):       # => 행동(method) : 함수/기능
#         return self.name

# p = Person()   # => 인스터스화 했다. 인스턴스 객체를 생성했다.
# p.name # => 속성을 호출
# p.hello() # => 메소드 호출


# self : 인스턴스 객체 자기자신 (다른언어에서는 this)
#   - 특별한 상황을 제외하고는 무조건 메소드의 첫번째 인자로 설정한다.
#   - 인스턴스 메소드를 실행할 때 자동으로 첫번째 인자에 인스턴스를 할당한다.

# p1 = Person()
# #이것과
# print(p1.hello())
# #이것은 같은 의미다
# print(Person.hello(p1))

# p2 = Person()

# print(p1.name)
# p2.name = 'kim'
# print(p2.name)
# p2.location = 'seoul'
# print(p2.location)


# 생성자, 소멸자

# def __init__(self):
#    print('생성될 때 호출되는 메서드')

# def __del__(self):
#    print('소멸될 때 호출되는 메서드')

class Person():
    name = ''

    def __init__(self, name='이름없음'):
        self.name = name
        print('생성됨')

    # def __del__(self):
    #     print('소멸됨')

# p1 = Person('junhyuk')  # 이런의미다. Person.__init__(p1, 'junhyuk')
# 인스턴스 삭제
# del p1
# print(p1.name)
# p2 = Person('Lee')
# p2.location = '대전'
# print(p2.name)

# p3 = Person()
# print(p3.name)


# 연습

class Pikachu():

    def __init__(self, name='pikachu'):
        self.name = name
        self.level = 1
        self.hp = self.level * 100

    
    def attack(self, opponent):
        damege = self.level * 5
        opponent.hp -= damege
    

    
p1 = Pikachu()
p2 = Pikachu('chu')

# p1.attack(p2)
# print(p1.hp)
# print(p2.hp)



# 연습2
# Circle 클래스

# 속성
# pi : 원주율 (3.14)

# 인스턴스 속성
# r : 반지름 (필수입력)
# x : x좌표 (default=0)
# y : y좌표 (default=0)

# 메서드
# area() : 원의 넓이를 반환
# center() : 원의 중심을 (x, y) 튜플로 반환
# move(x, y) : 원의 중심을 (x, y)로 변경

## 내가 함 완료 못함
class Circle():
    pi = 3.14

    def __init__(self, r, x=0, y=0):
        self.r = r
        self.x = x
        self.y = y 

    def area(self):
        area = self.pi * self.r**2

    def center(self):
        pass

    def move(self, x, y):
        pass

# 강사님 풀이
class Circle():
    pi = 3.14

    def __init__(self, r, x=0, y=0):
        self.r = r
        self.x = x
        self.y = y

    def center(self):
        return (self.x, self.y)
    
    def area(self):
        return self.r ** 2 * Circle.pi
    
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f'원의 중심이 ({x}, {y})로 이동했습니다.')


c1 = Circle(5)
# print(c1.center())
# print(c1.area())
# c1.move(100, 100)


# 클래스변수
# - 클래스 선언 블록 최상단에 위치
# - ClassName.class_variable 로 접근 / 할당

# 인스턴스 변수
# - self.instance_variable 로 접근 / 할당

class TestClass:
    class_variable = '클래스변수'

    def __init__(self, arg):
        self.instance_variable = arg

    def status(self):
        return self.instance_variable


t1 = TestClass('인스턴스변수')
# 클래스 변수 확인
# print(TestClass.class_variable)
# print(t1.class_variable)
# 인스턴스 변수 확인
# print(t1.instance_variable)



# instance method 
# class ClassName:
#   def func():
#       pass

# class method
# class ClassName:
#   @classmethod
#   def func():
#       pass

# static method
# class ClassName:
#   @staticmethod
#   def func():
#       pass



class MyClass:

    def instanc_method(self):
        return self
    
    @classmethod
    def class_method(cls):
        return cls

    @staticmethod
    def static_method(arg):
        return arg



# m1 = MyClass()
# print(m1.instanc_method())
# print(m1.class_method())
# 클래스 메소드 실행
# print(MyClass.class_method())
# print(m1.static_method('hello'))


# 연습

class Puppy():
    num_of_dogs = 0

    def __init__(self, name):
        self.name = name
        Puppy.num_of_dogs += 1

    @classmethod
    def get_statuts(cls):
        return f'현재 강아지는 {cls.num_of_dogs}마리 입니다.'    
    
    @ staticmethod
    def bark(str='멍멍'):
        return str


p1 = Puppy('인절미')
p2 = Puppy('초코')

# print(Puppy.num_of_dogs)
# print(Puppy.get_statuts())
# print(p1.bark())
# print(p2.bark('그르릉'))


class Person():
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')    

# p1 = Person('홍길동')
# p1.greeting()



# 상속
# Person의 기능을 상속받는다는 의미로 () 안에 클래스명을 작성한다.
class Student(Person):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        Person.population += 1


# s1 = Student('이순신', '12345')
# s1.greeting()
# print(Student.population)


class Soldier(Person):
    # method overriding 메소드 오버라이딩
    def greeting(self):
        print('충성!!!')

# s2 = Soldier('국방이')
# s2.greeting()

# 안좋은 케이스, 오버라이딩을 하지만 중복되게 작성하는 내용이 많다 
class Person():
    def __init__(self, email, phone, location, name):
        self.email = email
        self.phone = phone
        self.location = location
        self.name = name

class Student(Person):
    def __init__(self, email, phone, location, name, id):
        self.email = email
        self.phone = phone
        self.location = location
        self.name = name
        self.id = id


# 좋은 케이스

class Soldier(Person):
    def __init__(self, email, phone, loacion, name, id):
        # super 는 부모객체를 말한다. 여기선 Person
        super().__init__(email, phone, location, name)
        self.id = id



# 다중상속 
class Person():
    def __init__(self, name):
        self.name = name

    def breath(self):
        print('후하')


class Mom(Person):
    gene = 'XX'

    def swim(self):
        print('어푸어푸')

    def greeting(self):
        print('안녀어어어영')

class Dad(Person):
    gene = 'XY'

    def run(self):
        print('다다다')       

    def greeting(self):
        print('안녕!')     

# 상속된 순서에 따라 같은 속성, 데이터, 메소드를 가졌을 때 먼저 작성된 클래스를 우선적으로 저장한다.
class FirstBaby(Mom, Dad):
    pass
b1 = FirstBaby('첫째')
# b1.swim()
# b1.run()
# b1.greeting()
# print(b1.gene)

class SecondBaby(Dad, Mom):
    pass
b2 = SecondBaby('둘째')
# b2.breath()
# b2.run()
# b2.greeting()
# print(b2.gene)



# 연습

class Pocketmon():
    def __init__(self):
        self.level = 1
        self.hp = self.level * 5
        self.exp = 0

    def attack(self, opponent):
        damege = self.level * 2
        opponent.hp -= damege
        if opponent.check_hp():
            self.exp += 5
        print('attack!')
    
    def check_hp(self):
        return True if self.hp <= 0 else False


class Type():
    def __init__(self, type_name):
        self.type_name = type_name

class WaterPocketmon(Pocketmon):
    def heal(self):
        if self.hp <= 3:
            self.hp += 4
            print('heal!')

    def swim(self):
        print('어푸어푸')        
       

class FierPocketmon(Pocketmon):
    def heal(self):
         if self.hp <= 3:
            self.hp += 6
            print('heal!')

    def fly(self):
        print('펄럭펄럭')
        

kobokki = WaterPocketmon()
pairi = FierPocketmon()


print(kobokki.hp)
pairi.attack(kobokki)
pairi.attack(kobokki)
print(kobokki.hp)
kobokki.heal()
print(kobokki.hp)



print(pairi.hp)
kobokki.attack(pairi)
kobokki.attack(pairi)
print(pairi.hp)
pairi.heal
print(pairi.hp)

kobokki.swim()

pairi.fly()





