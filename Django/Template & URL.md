# Django template system
- HTML의 컨텐츠를 변수 값에 따라 변경하기
```css
/* 기존 html은 변경이 안된다 */
<body>
  <h1>Hello, django!</h1>
</body>
```

```py
def index(request):
    # 딕셔너리 이름
    context = {
        'name': 'Jane',
    }
    return render(request, 'articles/index.html', context)
```
```css
/* 파이썬 딕셔너리를 이용하면 변경이 된다 */
<body>
  <h1>Hello, {{name}}</h1>
</body>
```

1. Variable
- render 함수의 세 번째 인자로 **딕셔너리**사용
- .을 이용하여 속성에 접근 가능
- `{{variable.attribute}}`

2. Filters
- 표시할 변수 수정
- 내장함수 같은건가?
- `{{variable|filter}}`

3. Tag
- 반복, 논리 수행 >> 제어 흐름 만듬
- `{% tag %} {% endtag %}`: tag >> if로 시작해서 endif로 끝남

4. 주석
- `{% comment %} {% endcomment %}`

## Template 상속
- `{% extends 'path'%}`
- 맨 위에 작성
- path에서 상속받음

- `{% block content %} {% endblock content %}`

## 요청과 응답
- form 태그 사용
  - 가짜 네이버 사이트 만들기
  `https://search.naver.com/search.naver ? where=nexearch & sm=top_hty & fbm=0 & ie=utf8 & query=gd`
  - 메인사이트, ?이후로 key:value, 마지막은 검색어
  - name 속성 값으로 query를 받음

### action, method
- action: 입력 데이터가 전송될 url 지정
  - https://search.naver.com/search.naver
- method: get, post 방식


### input
- name: 입력한 데이터의 key
  - key=value & ...
  - sm=top_hty & fbm=0

### request
- **오늘 배운 것 중 throw-catch가 가장 중요**
- throw 응답을 catch에서 받아서 그대로 출력
``` py
print(request) # <WSGIRequest: GET '/catch/message=hi'>
print(type(request)) # <class 'django.corehandlers.wsgi.WSGIRequest'>

# 자료유형: 딕셔너리
print(request.GET) # <QueryDict: {'message':['hi']}>

# 딕셔너리에 get 메서드 사용
rint(request.GET.get('message')) # hi: 내가입력한 것
message = request.GET.get('message')
context = {
    'message': message,
}
return render(request, 'articles/catch.html', context)
```

# Django URL
- 요청을 view 함수에 분배함
- app이 많아지면 관리가 힘들어짐
- 결론: url을 app과 1대1로 분리해주자

## Variable Routing
- 변수는 view함수의 인자로 전달
- `path('articles/<path_converter:변수이름>', views.detial)`

## URL Naming
- path 함수에서 url에 이름 부여
- `path('index/', views.index, name='index')`

- app_name 부여
- app_name = 'index'

- html에서 사용: {% url 'articles:index' %}


# 전체 흐름
- urls에 있는 주소면 views.py 호출
- views.py에서 해당하는 함수(index) 호출
- 해당하는 함수(index)에서 (index).html 호출


## 1. 상속
1. settings.py > TEMPLATE > DIR에서 BASE_DIR 설정
2. 루트폴더에 template와 base.html 생성
3. 상속주고 싶은 부분 {block 이름} {endblock 이름}
4. 상속 받는 아이들은 {extends 이름}으로 시작
  - {block 이름} 원하는 작업 수행 {endblock 이름}

## 2. 상속 + 동작(요청, 응답)
1. 요청해야 하는 html에 form 생성
```html
<!-- action:
method: 
type:
name: 들어온 데이터의 이름
value: submit 블럭 이름 -->
<form action="/todos/" method="GET">
  <input type="text" name="work">
  <input type="submit" value="제출">
</form>
```

2. 응답해야하는 view함수에 데이터 처리
```py
def index(request):
    work = request.GET.get('work')
    context = {
        'work': work, 
    }
    return render(request, 'todos/index.html', context)
```

3. 응답해야하는 html에 데이터 전달
```django
{% block content %}
  <h1>할 일 목록 관리 프로젝트 메인 페이지</h1>
  <p>이 곳에서 할 일 목록을 관리합니다.</p>
  <ol>{{work}}</ol>
{% endblock content %}
```

4. url에서 변수를 같이 받는 경우
- <변수> 꺾쇠로 변수를 받는다
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('introduce/<username>', views.introduce),
    
]
```
## url 권한 분배
1. 루트 urls.py에서 경로 설정
```py
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls'))
]
```

2. 하위 url(articles에 있는 urls.py)에서 특정 기능 수행
```py
from django.urls import path
# 현재 디렉토리에서 view.py 호출
from . import views

app_name = 'articles'

# 경로가 articles/index/로 호출되면 views.py에서 index() 호출 
urlpatterns = [
    path('index/', views.index, name='index')
    
]
```

3. 그 뒤로는 html 부르고 똑같다
```py
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
```

4. base에서 사용할 때 url이름:경로이름으로 사용
```html
<a href="articles:index"></a>
```