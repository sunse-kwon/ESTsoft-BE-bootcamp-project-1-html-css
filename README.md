# ESTsoft-BE-bootcamp-project-1-html-css
## Subject : ChatGPT-based Singapore Travel Plan Auto-generation Planner Chatbot - Frontend

## Objectives 
- Implement a chatbot using OpenAI's Chat Completions API
- Build a web service using HTML, CSS, JavaScript, and Pyscript
- Develop a bundling algorithm to group nearby tourist attractions from a raw dataset
- Use user input data and bundled data as input for ChatGPT
- Enhance the reliability of ChatGPT's output using prompt engineering techniques (1. Setting rules, guidelines, and examples 2. Using the phrase "Let's think step by step")
- Display tourist attractions from the raw dataset as cards on a separate page
- Ensure mobile compatibility

### Key Features
- Tourist Attraction Bundling: Utilized a bundling algorithm to calculate distances and travel times for 107 tourist attractions in the raw dataset, grouping nearby attractions together before sending them to ChatGPT.
Created 23 bundles, each containing 2 to 5 attractions, with distances between 5km and 10km, and standardized travel time of 60 minutes per attraction.
- Index Page: Transition from the first screen to the main page, using sessionStorage to send URLs needed for the chat and attraction pages.
- Main Page: Collect travel information from users to provide personalized responses, and pass this information to the chat page.
- Chat Page: Use user input and attraction bundles to communicate with ChatGPT API, generating personalized Singapore travel plans.
- Attraction Page: Display information for all 107 tourist attractions in the raw dataset as cards.
- Sign-up Page: User registration feature.
- Login Page: User login feature.

### Development Environment
- HTML, CSS, JavaScript, Pyscript
### Deployment URL
- http://bundletripbychat.com/
### Development Timeline
- May 30, 2023 ~ June 15, 2023


### Project Structure
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

### Page Implementation

#### Index
<img width="1440" alt="image" src="https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/21de0733-6621-4a36-807e-b40334fd18fe">

#### Sign-up
![회원가입](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/2f7616a1-92fc-4914-909d-5e9e0a54e289)

#### Login
![로그인-1](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/b56b2e0b-0b18-4f05-a24b-547204cde696)

#### User Information Input
![사용자정보](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/e1c80ae5-f1f2-4751-af1c-88928451cf24)

#### Chat
![chat1](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/e170e17e-2b9d-46a1-9b7e-c31389888f55)
![chat2](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/e07fb1f9-bb46-4e19-90a4-1409319a8158)

#### Attraction Details
![attraction-1](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-1-html-css/assets/94329884/dd55ca6a-f58a-4dd2-b37c-b7176cdf69c4)

### Reference
Reference
- Data Source: The TOURISM.csv data was sourced from Singapore's public data and converted to CSV format. [Singapore Tourism Data ](https://data.gov.sg/dataset/tourist-attractions )
- Prompt Engineering: Referenced OpenAI's techniques to improve reliability document. [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/articles/techniques_to_improve_reliability.md)
