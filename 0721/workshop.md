# 1. List의 합 구하기

```python
def list_sum(lst):
    total = 0
    for i in lst:
        total+= i
    print(total)
    return total

list_sum([1, 2, 3, 4, 5])
```



# 2. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(my_dict):
    total = 0
    for i in my_dict:
        total+= i['age']
    print(total)
    return total

dict_list_sum([{'name': 'kim', 'age': 12},
               {'name': 'lee', 'age': 4}])

16
```



# 3. 2차원 List의 전체 합 구하기

```python
def all_list_sum(lst):
    total = 0
    cnt = -1
    for i in lst:
        cnt+= 1
        for j in lst[cnt]:
            total+= j

    print(total)
    return total

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
55
```

