# HomeWork

1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가?

   form.is_valid() 메소드에서 유효성 검사를 진행할 때 만약에 유효성에서 통과되지 못하면 

   create 함수가 그냥 종료되기 때문에 context가 if else구문과 동일한 레벨에 작성되어 있다.



2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?

   http method에는 POST GET 이외에도 PUT DELETE가 있다. 만약에 GET를 먼저 사용한다면

   else를 통해 POST를 받는 것이 아닌 GET이 아닌 모든 것을 받아들이기 때문에 PUT이나 DELETE가 와도 else문이 실행되어진다. 따라서 POST를 먼저 작성한다.
