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
class Person:   # => 클래스 정의(선언) : 클래스 객체 생성
    name = 'hong'   # => 속성(attribute) : 변수/값/데이터

    def hello(self):       # => 행동(method) : 함수/기능
        return self.name

p = Person()   # => 인스터스화 했다. 인스턴스 객체를 생성했다.
p.name # => 속성을 호출
p.hello() # => 메소드 호출





















