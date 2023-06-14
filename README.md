# ormi-dev-project-1
## 주제 : chatGPT를 활용한 싱가포르 여행계획 자동생성 플래너 챗봇

### 목표
- openAI 의 Chat Completions API를 활용하여 챗봇을 구현.
- html, css, javascript, pyscript 를 활용하여 웹서비스 구축.
- bundling algorithm을 활용하여 raw dataset 안의 여행지들을 가까운 관광지끼리 묶음.
- user input data와 bundle data를 chatGPT의 input 으로 학습.
- chatGPT의 output 신뢰성을 높이기 위한 다양한 테크닉을 사용 (1.setting rules, guidelines and example. 2.use "Let's think step by step" clause.)
- raw dataset의 관광지들을 card로 만들어 별도 페이지에 출력.
- 모바일 환경을 고려.

### 세부기능
- 관광지 bundling: bundling algorithm을 활용하여 raw dataset(총107개 관광지로 구성) 안의 여행지의 거리 및 관광소요시간을 계산하여 가까운 관광지끼리 하나의 bundle로 묶는다.(총 23개의 번들, 각 번들은 최소 2개 최대 5개의 관광지들로 구성, 거리계산은 최소 5km 최대 10km 인 것들끼리 묶음, 관광소요시간은 편의를 위해 모든관광지를 각 60분으로 통일), raw dataset을 bundle로 변환 후 chatGPT에 전달.
- index 페이지: 첫화면에서 메인페이지로 전환, url을 sessionStorage를 이용하여 chat 및 attraction 페이지에 필요한 url 전송.
- main 페이지: 개인화된 답변을 주기위해 여행에 필요한 정보 입력시, chat 페이지에 전달.
- chat 페이지: 유저 input과 관광지 번들을 활용하여 chatGPT와 API 통신, chatGPT가 개인화된 싱가포르 여행계획 생성.
- attraction 페이지: raw dataset에 있는 총 107개 관광지 정보를 카드형태로 출력.

### 개발환경
- html, css, javascript, pyscript

### 배포 url
- https://sunse-kwon.github.io/ormi-dev-project-1/

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

### 페이지 디자인
- index.html
![index](https://github.com/sunse-kwon/ormi-dev-project-1/assets/94329884/89c11ef4-9c5f-48a2-9f3c-0e23b2d4c4b6)

- main.html
![main](https://github.com/sunse-kwon/ormi-dev-project-1/assets/94329884/bd08f485-04d7-4a97-9b7f-843d6e4a5a17)

- chat.html
![chat](https://github.com/sunse-kwon/ormi-dev-project-1/assets/94329884/7d4fde9d-64dc-415b-8837-b73d5a9aad8f)

- attractions.html
![attractions](https://github.com/sunse-kwon/ormi-dev-project-1/assets/94329884/79f752b7-bc54-4fea-94f1-5e433c97b535)

### Reference
- data source: TOURRISM.csv dataset is originally aquired from https://data.gov.sg/dataset/tourist-attractions and then converted to csv format. 
- techniques to improve reliability: https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md 
