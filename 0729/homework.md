# 1. Circle 인스턴스 만들기

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

c1 = Circle(3,2,4)
print(c1.area())
print(c1.circumference())

28.259999999999998
18.84
```





# 2. Dog과 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()

#멍멍이! 달린다!
#멍멍이! 짖는다!
#구구! 걷는다!
#구구! 먹는다!
#구구! 푸드덕!
```





# 3. 오류의 종류

```
ZeroDivisionError : 0으로 나누었을 때 나오는 오류
NameError : 어느 곳에서도 정의되지 않은 변수를 호출하였을 경우 나오는 에러
TypeError : 자료형이 올바르지 못한 경우
IndexError : 없는 인덱스를 실행시킬 때 나오는 오류
KeyError : 없는 키 값을 찾을 때 나오는 오류
ModuleNotFoundError : 없는 모듈을 찾아올때 나오는 오류
ImportError : 모듈을 찾았으나 가져오는 과정에서 실패하는 경우(존재하지 않는 클래스/함수 호출)
```



