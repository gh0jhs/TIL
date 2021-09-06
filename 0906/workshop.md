# WorkShop

1) Model Form을 정의하기 위해 빈칸에 들어갈 코드 (a), (b)를 작성하시오.

```
(a) forms.ModelForm
(b) Meta
```



2) 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 
서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 
이유와 해결방법을 작성하시오.

```
form_is_valid()에서 유효성검사에서 거짓을 리턴하면 create함수는 그냥 종료가 되어진다.
따라서 else문에 있는 context구문과 리턴구문을 else문 바깥으로 빼주어야 한다.
```



3) 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드 (a), (b)를 작성하시오.

```
(a)form = ReservationForm(request.POST)
(b)form = ReservationForm()
```



4) form 출력을 구현하기 위해 빈칸 (a)에 작성 할 수 있는 코드를 모두 작성하시오.

```
as_p()
as_ul()
as_table()
```

