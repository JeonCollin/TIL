## transformer
- 병렬처리

- 문맥속에서 단어들 사이의 연관관계 파악

- 인코딩: 대량의 데이터를 압축
    - 대량의 데이터 -> 어텐션 매커니즘(weight 계산) -> 모델

- 디코딩: 일부분의 데이터(프롬프트) -> 모델 -> 응답


## API(Applicaion Programing Interface)
- 어떤 기능을 프로그래머가 사용할 수 있도록 만들어 놓은 것

- 이 기능을 사용하려면 API에 정해진 약속대로 요청을 보내야 함.
- ex ) iOS, Android SDK
    - 핸드폰의 각종 기능들(카메라, 사진첩, GPS, 진동 ...)
    - SDK: 각종 기능을 이용할 수 있는 함수 정의
    - iOS(Swift, Objective-C), Android(JAVA, Kotlin)

# API 예시
- 구글 / 네이버로 로그인 >> 인증 서비스를 대신해줌

    - 구글이 API를 만들어 공개

        - 어떻게 요청을 보내면 어떤 식으로 응답하겠다

        - 요청: 구글이 지정한 URL로 자신의 앱 ID, API KEY를 보냄
        - 응답: 올바른 사용자인지, 정보(비밀번호 제외)
- 날씨

**결론: 어떤 기능이 필요할 때 API를 찾아보기**
- 문서에서 어떤 식으로 요청해야 하는지 찾아보기

- 응답을 해석
- 우리 프로그램의 하나의 기능으로 API를 활용하게 됨 
- 자판기 버튼은(API) 누르면 원하는 음료수가(기능) 나온다

## API KEY
- API는 기능이자 자산, 비용이 발생

    - Weather API 입장에서는 데이터베이스가 큰 자산

- 비밀번호같은거 => 절대 소스코드에 포함 X
    - .gitignore로 제외시켜야함
- API키에는 사용량 제한이 있음




## 웹의 구조(서버 - 클라이언트)
- 클라이언트가 HTTP 요청을 보내고 서버는 HTTP 응답을 한다.

- HTTP 프로토콜: 약속(정해진 형식 요청-응답)
- HTTP: 웹, 인터넷을 사용할 때 프로토콜
    - ex ) 네이버 예시
        - 브라우저의 주소창에 https://naver.com 입력하고 엔터치면 서버로 GET 요청(웹 페이지를 달라)을 보냄

    - 네이버 서버가 GET 요청을 받음 >> 웹 페이지의 소스코드(HTML)를 보내줌
    - 브라우저는 받은 코드를 해석해서 렌더링 해서 화면에 보여줌.

## HTML 구조
- HTML
    - head: 화면으로 보여지지는 않음. 탭 제목, 기타 설정에 관한 내용

        - title
    - body: 바디태그 내용이 브라우저 화면 창에 나타나는 내용용
        - div 태그: 박스 == section
        - section
            - top
            - middle
            - bottom

## 챗봇 만들기
- 구조
    - index.html: 웹페이지의 전체적인 구조, 구성(어떤 요소로 이루어져 있는가?)
    - style.css: 각 요소의 스타일(크기, 너비, 높이, 색상, 글꼴...)
    - app.js: 자바스크립트, 각 요소의 기능, 동작 담당 

- res 응답 본문 == res.data == 서버의 응답 본문문
{
    "id": 
    "chatcmpl-AqWKxlojWpj8sZ3k7hMltdnoMVBhF",
    "object": "chat.completion",
    "created": 1737080723,
    "model": "gpt-3.5-turbo-0125",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "알겠어요! 어떤 도움이 필요하신가요?",
                "refusal": null
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 12,
        "completion_tokens": 25,
        "total_tokens": 37,
        "prompt_tokens_details": {
            "cached_tokens": 0,
            "audio_tokens": 0
        },
        "completion_tokens_details": {
            "reasoning_tokens": 0,
            "audio_tokens": 0,
            "accepted_prediction_tokens": 0,
            "rejected_prediction_tokens": 0
        }
    },
    "service_tier": "default",
    "system_fingerprint": null
}
- const: 상수(변수) 선언
    - `const response`를 하게되면 response라는 이름으로 변수 생성 
- response 변수에 응답 내용을 선택하여 저장


## Prompt engineering
- task: 하나의 구체적인 작업을 시키기
- context: 작업과 관련된 상황을 자세히 설명할 수록 좋다.
-페르소나 (역할부여:) 나느 월 1억 전응 M& 전문 애너리스트다
- 예시: 예시를 들어주면 비슷하게 만들어줌
- 형식: 지정된 형식으로 반들어줌

**명시적 지시**
