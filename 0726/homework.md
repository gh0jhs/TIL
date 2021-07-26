# 1. 모음은 몇 개나 있을까?

```python
def count_vowels(word):
    result = 0
    result += word.count('a')
    result += word.count('e')
    result += word.count('i')
    result += word.count('o')
    result += word.count('u')
    return result

#이렇게 푸는거 맞나?..
count_vowels('apple')
count_vowels('banana')
```





# 2. 문자열 조작

```
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.
(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를
기준으로 나누어 list로 반환한다. 특정 문자를 지정하지 않으면
공백을 기준으로 나눈다.
(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로
바꿔서 반환한다.
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를
찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다.


(4) 특정 문자를 지정하지 않으면 공백을 제거한다. (4)번이 옳지 않다.
```





# 3. 정사각형만 만들기

```python
def only_square_area(lst1, lst2):
    lst = []
    for i in lst1:
        for j in lst2:
            if i==j:
                lst.append(i**2)
    lst = set(lst)
    lst = sorted(list(lst))
    return lst


print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
```

