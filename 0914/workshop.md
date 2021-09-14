# WorkShop

## 1. SQL Query

```sqlite
1) CREATE TABLE countries (
   ...> room_num TEXT,
   ...> check_in TEXT,
   ...> check_out TEXT,
   ...> grade TEXT,
   ...> price INT
   ...> );

2) sqlite> INSERT INTO countries (room_num, check_in, check_out, grade, price)
   ...> VALUES ('B203', '2019-12-31', '2020-01-03', 'suite', 900);
sqlite> INSERT INTO countries VALUES('1102', '2020-01-04', '2020-01-08', 'suite', 850);
sqlite> INSERT INTO countries VALUES('303', '2020-01-01', '2020-01-03', 'deluxe', 500);
sqlite> INSERT INTO countries VALUES('807', '2020-01-04', '2020-01-07', 'superior', 300);

3) ALTER TABLE countries RENAME TO hotels;

4) SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

5) SELECT grade, COUNT(*) FROM hotels GROUP BY grade ORDER BY COUNT(*) DESC;

6) SELECT * FROM hotels WHERE grade='deluxe' OR room_num LIKE 'B%';

7) SELECT * FROM hotels WHERE check_in='2020-01-04' AND room_num NOT LIKE 'B%' ORDER BY price;
```



## 2. SQL ORM 비교하기

```sqlite
1) User.objects.all()

2) User.objects.filter(id=19).values('age')

3) User.objects.all().values('age')

4) User.objects.filter(age__lte=40).values('id', 'balance')

5) User.objects.filter(last_name='김', balance__get=500).values('first_name')

6) User.objects.filter(first_name__endswith='수', country='경기도').values('balance')

7) User.objects.filter(Q(balance>=2000) | Q(age<=40)).count()

8) User.objects.filter(phone__startswith='010').count()

9) User.objects.get(name='김옥자').country('경기도')

10) user = User.objects.get(last_name='백', first_name='진호')
	user.delete()
	
11) User.objects.order_by('-balance')[:4].values(first_name, last_name, balance)

12) User.objects.filter(age__lt=30, '123' in phone)

13) ###

14) User.objects.aggregatrre(Avg('age'))

15) User.objects.filter(last_name='박').aggregate(Avg('balance'))

16) User.objects.filter(country='경상북도').aggregate(Max('balance'))

17) User.objects.filter(country='제주특별자치도').order_by('-balance')[0].first_name
```

