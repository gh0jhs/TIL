# 1. Built-in 함수와 메서드

### sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```python
# .sort()
lst = [5, 3, 1, 4, 2, 6]
result = lst.sort()
print(lst)
print(result)

# sorted()
lst = [5, 3, 1, 4, 2, 6]
result = sorted(lst)
print(lst)
print(result)
```

```py
[1, 2, 3, 4, 5, 6]
None

[5, 3, 1, 4, 2, 6]
[1, 2, 3, 4, 5, 6]
```

```
.sort() 메서드를 사용하면 리스트 원본이 정렬된다. 하지만 return 값은 None이 나온다.
Built-in 함수 sorted()를 사용하면 리스트의 원본은 정렬되지 않고 그대로 값을 유지하며 반환값으로 정렬된 리스트가 나온다. 
```



# 2. .extend()와 .append()

### .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```python
# extend
lst = []
lst.extend('ABC')
lst.extend(['ABC'])
print(lst)

# append
lst = []
lst.append('ABC')
lst.append(['ABC'])
print(lst)
```

```python
['A', 'B', 'C', 'ABC'] #extend

['ABC', ['ABC']] #append
```

```
.extend()를 이용했을 때 'ABC'를 인자로 전달하면 'A', 'B', 'C' 하나씩 나누어서 리스트에 추가가 된다. 리스트에 한 값으로 추가하고 싶을 때는 ['ABC'] 값을 전달해줘야 한다.
.append()를 이용했을 때는 'ABC'를 인자로 전달하면 리스트에 'ABC'가 나뉘어지지 않고 리스트에 추가된다.
리스트를 씌워서 값을 전달할 경우 리스트 자체가 인자로 전달되어 리스트 안에 리스트를 갖는 모습이 나타난다.
```



# 3. 복사가 잘 된 건가?

```python
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a)
print(b)
```

```python
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]
```

```python
# 리스트의 같은 경우 mutable하기 때문에 a와 b는 같은 메모리 주소 공간을 참조한다.
print(id(a), id(b))
2291960218816 2291960218816
따라서 a[2]를 변경시키면 b[2]의 값도 똑같이 변경되게 된다.
```

