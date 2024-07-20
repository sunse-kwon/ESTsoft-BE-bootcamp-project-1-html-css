# ESTsoft-BE-bootcamp-project-1-html-css
## 주제 : ChatGPT를 활용한 싱가포르 여행계획 자동생성 플래너 챗봇 - Frontend

### 목표
- openAI 의 Chat Completions API를 활용하여 챗봇을 구현.
- HTML, CSS, Javascript, Pyscript 를 활용하여 웹서비스 구축.
- Bundling algorithm을 활용하여 raw dataset 안의 여행지들을 가까운 관광지끼리 묶음.
- User input data와 bundle data를 ChatGPT의 input 으로 학습.
- ChatGPT의 output 신뢰성을 높이기 위한 prompt engineering 테크닉을 사용(1. setting rules, guidelines and example. 2. use "Let's think step by step" clause.)
- Raw dataset의 관광지들을 Card로 만들어 별도 페이지에 출력.
- 모바일 환경을 고려.

### 세부기능
- 관광지 Bundling: Bundling algorithm을 활용하여 Raw dataset(총107개 관광지로 구성) 안의 여행지의 거리 및 관광소요시간을 계산하여 가까운 관광지끼리 하나의 Bundle로 묶기, Bundle로 변환 후 ChatGPT에 전달.
  * 총 23개의 번들, 각 번들은 최소 2개 최대 5개의 관광지들로 구성, 거리계산은 최소 5km 최대 10km 인 것들끼리 묶음, 관광소요시간은 편의를 위해 모든관광지를 각 60분으로 통일 
- index 페이지: 첫화면에서 메인페이지로 전환, url을 sessionStorage를 이용하여 chat 및 attraction 페이지에 필요한 url 전송.
- main 페이지: 개인화된 답변을 주기위해 여행에 필요한 정보 입력, 이를 chat 페이지에 전달.
- chat 페이지: 유저 input과 관광지 번들을 활용하여 ChatGPT와 API 통신, ChatGPT가 개인화된 싱가포르 여행계획 생성.
- attraction 페이지: raw dataset에 있는 총 107개 관광지 정보를 카드형태로 출력.
- signin 페이지: 회원가입 기능
- login 페이지: 로그인 기능

### 개발환경
- HTML, CSS, Javascript, Pyscript

### 배포 URL
- http://bundletripbychat.com/

### 개발 일정
- 2023년 5월 30일 ~ 2023년 6월 15일

### 프로젝트 구조
```
📦 
├─ index.html
├─ .DS_Store
├─ README.md
├─ css
│  ├─ .DS_Store
│  ├─ attractions.css
│  ├─ chat.css
│  ├─ common.css
│  ├─ font
│  │  ├─ .DS_Store
│  │  ├─ NanumGothic-Bold.ttf
│  │  ├─ NanumGothic-ExtraBold.ttf
│  │  ├─ NanumGothic-Regular.ttf
│  │  └─ OFL.txt
│  ├─ index.css
│  └─ main.css
├─ data
│  └─ TOURISM.csv
├─ html
│  ├─ attractions.html
│  ├─ chat.html
│  └─ main.html
├─ img
│  ├─ .DS_Store
│  ├─ index.jpg
│  ├─ main.jpg
│  └─ world-tour-icon.svg
├─ js
│  ├─ .DS_Store
│  ├─ PapaParse-5.0.2
│  │  ├─ .eslintrc.js
│  │  ├─ .gitignore
│  │  ├─ .npmignore
│  │  ├─ .travis.yml
│  │  ├─ Gruntfile.js
│  │  ├─ LICENSE
│  │  ├─ README.md
│  │  ├─ bower.json
│  │  ├─ docs
│  │  │  ├─ CNAME
│  │  │  ├─ Caddyfile
│  │  │  ├─ demo.html
│  │  │  ├─ docs.html
│  │  │  ├─ faq.html
│  │  │  ├─ favicon.ico
│  │  │  ├─ index.html
│  │  │  └─ resources
│  │  │     ├─ css
│  │  │     │  ├─ common.css
│  │  │     │  ├─ demo.css
│  │  │     │  ├─ home.css
│  │  │     │  ├─ tomorrow.highlight.css
│  │  │     │  └─ unsemantic.css
│  │  │     ├─ files
│  │  │     │  ├─ big.csv
│  │  │     │  ├─ malformed.tsv
│  │  │     │  └─ normal.csv
│  │  │     └─ js
│  │  │        ├─ common.js
│  │  │        ├─ demo.js
│  │  │        ├─ highlight.min.js
│  │  │        ├─ home.js
│  │  │        ├─ jquery.min.js
│  │  │        ├─ lovers.js
│  │  │        ├─ papaparse.js
│  │  │        └─ skrollr.min.js
│  │  ├─ package.json
│  │  ├─ papaparse.js
│  │  ├─ papaparse.min.js
│  │  ├─ player
│  │  │  ├─ player.css
│  │  │  ├─ player.html
│  │  │  └─ player.js
│  │  └─ tests
│  │     ├─ .eslintrc.js
│  │     ├─ long-sample.csv
│  │     ├─ node-tests.js
│  │     ├─ sample.csv
│  │     ├─ test-cases.js
│  │     ├─ test.js
│  │     ├─ tests.html
│  │     └─ verylong-sample.csv
│  ├─ attractions.js
│  ├─ main.js
│  └─ url.js
└─ py
   ├─ .DS_Store
   ├─ bundle.py
   ├─ chat.py
   ├─ request.py
   └─ utils.py
```

### 페이지 구현

#### 인덱스
<img width="1440" alt="image" src="https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/21de0733-6621-4a36-807e-b40334fd18fe">

#### 회원가입
![회원가입](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/2f7616a1-92fc-4914-909d-5e9e0a54e289)

#### 로그인
![로그인-1](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/b56b2e0b-0b18-4f05-a24b-547204cde696)

#### 사용자정보 입력
![사용자정보](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/e1c80ae5-f1f2-4751-af1c-88928451cf24)

#### Chat
![chat1](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/e170e17e-2b9d-46a1-9b7e-c31389888f55)
![chat2](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/e07fb1f9-bb46-4e19-90a4-1409319a8158)

#### 여행지 상세정보
![attraction-1](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/dd55ca6a-f58a-4dd2-b37c-b7176cdf69c4)

### Reference
- Data Source: TOURRISM.csv 은 싱가포르 공공데이터에서 가져왔으며, CSV 형식으로 변환하였습니다. https://data.gov.sg/dataset/tourist-attractions 
- Prompt Engineering: openAI의 techniques to improve reliability 문서를 참조하였습니다. https://github.com/openai/openai-cookbook/blob/main/articles/techniques_to_improve_reliability.md
