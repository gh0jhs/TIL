# HomeWork

## 1. Model 반영하기

```python
# Migration
```



## 2. Model 변경사항 저장하기

```python
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate articles 0001

BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL);
COMMIT;
```



## 3. Python Shell

```py
python -i
```



## 4. Django Model Field

```python
BooleanField
CharField
DateField
DateTimeField
EmailField
```

