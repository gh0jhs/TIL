# 1. 평균 점수 구하기

```python
def get_dict_avg(dict):
    result = sum(dict.values())/len(dict)
    return result

get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
})
```





# 2. 혈액형 분류하기

```python
def count_blood(lst):
    my_dict = {
        'A' : lst.count('A'),
        'B' : lst.count('B'),
        'O' : lst.count('O'),
        'AB' : lst.count('AB')
    }
    return my_dict




count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB' ,
])
```

