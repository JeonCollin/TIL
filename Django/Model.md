# Model.py
- urls.py > view.py <-> **model.py** <-> **migrations** <-> DataBase
- 데이터를 저장하는 테이블: id, title, content
- 설계도 초안

```py
# models.py
from django.db import models

# Create your models here.

# 게시글이 저장될 테이블을 설계하는 클래스
# models에 있는 속성을 Model에 상속함
class Article(models.Model):
    # model Field 클래스들
    # 데이터 유형, 제약 조건 정의
    # 보통 char field는 제약 조건이 있다
    title = models.CharField(max_length=10)
    # 보통 text field는 제약조건이 없다
    content = models.TextField()
```
- 문자필드
  - CharField()
    - 제한된 길이의 문자열 저장(max_length)
  - TextField()
    - 길이 제한이 없는 대용량 텍스트 저장

- 기타: Integer, Float, Date, Time, DateTime, File, Image

- 제약조건
  - null: null 값을 허용할 지 여부
  - blank: 빈 값을 허용하는 지
  - default: 기본 값 설정

# Migrations.py
- model 클래스를 기반으로 최종 설계도 작성
`python manage.py makemigrations`

- 최종 설계도를 db에 전달`
`python manage.py migrate`

## 추가 모델 필드 작성
```py
# models.py
class Article(models.Model):
    # 기본
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 추가
    # 게시글이 언제 만들어졌고 저장되었는지
    # 데이터가 처음 생성됐을 때만 시간 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # 데이터가 저장될 때마다 시간 저장
    updated_at = models.DateTimeField(auto_now=True)
```
- 이미 migration을 한 상태에서 추가 migration을 하면 옵션을 선택해야 한다
  1. Django가 자동으로 해준다
  2. 내가 직접 한다

```py
# 1번 설계도가 없다면 동작할 수 없다
# 1번에 의존함
dependencies = [
    ('articles', '0001_initial'),
]
```

# Automatic admin interface
1. **migrate 이후에 생성 가능하다**. (DB가 존재해야 함)
`python manage.py createsuperuser`

2. 생성된 admin은 DB의 auth_user에서 확인 가능

3. admin에 모델 클래스 등록
```py
# admin.py
from django.contrib import admin
# models에서 Article 클래스 호출
from .models import Article

admin.site.register(Article)
```

# 전체 요약
1. setting에 app 등록

2. models.py에서 model 생성
```py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    기타 등등...
```

3. admin 등록하기
```py
# 클래스 호출
from .models import Article

admin.site.register(Article)
```

4. migration 만들기
`python manage.py makemigrations`

5. db에 model 전송(migrate)
`python manage.py migrate`

5. 슈퍼계정 만들기
`python manage.py createsuperuser`