from bundle import bundling
from request import request
from utils import genRef
import asyncio
import json
import pandas as pd
from pyodide.http import open_url
from pyodide.ffi import create_proxy
from js import document, sessionStorage, JSON


# openAI API를 가져옴
baseurl = sessionStorage.getItem('baseURL')

# TOURISM.csv url 가져옴
url = sessionStorage.getItem('rawURL')

# pandas 패키지로 csv 파일 읽어옴
rawData = pd.read_csv(open_url(url), sep=',', encoding='unicode_escape')

# bundling 알고리즘 실행을 위해 필수적인 attribute인 예상소요시간을 생성, 편의를 위하여 모든관광지를 소요시간을 60분으로 통일
rawData["EXPECTED_TIME_SPENT"] = 60

# bundling 알고리즘에 실행에 필요한 위도 경도, 예상소요 시간 및, ChatGPT에 input으로 넣어줄 attribute들만 선택.
rawData = rawData.loc[:, ["OBJECTID", 'LATITUDE', 'LONGTITUDE', "EXPECTED_TIME_SPENT",
                          "PAGETITLE", "OVERVIEW", "IMAGE_PATH", "ADDRESS", "OPENING_HO"]]

#bundling 알고리즘에 넣어주기 위해 pandas dataframe 을 numpy array로 변환
new_data = rawData.values

# 번들링 알고리즘을 사용하여 위에 데이터를 번들로 묶어준 데이터셋으로 변환. bundle.py 에서 함수를 import 함.
reference = bundling(new_data)

# genRef 함수를 활용하여 리스트 형태로 반환된 번들화된 데이터셋을 딕셔너리 형태로 변환. utils.py 에서 함수를 import 함
ref = genRef(reference)

# 위에 딕셔너리 형태의 파일을 json으로 변환. ChatGPT에 input으로 넣어줄 최종형태
ref = json.dumps(ref)

# 메인 페이지의 form에서 사용자가 입력한 값들을 세션스토리지를 통해 읽어옴.
gender = sessionStorage.getItem('gender')
transports = sessionStorage.getItem('transports')
travelStyle = sessionStorage.getItem('travelStyle')
departure = sessionStorage.getItem('departure')
arrival = sessionStorage.getItem('arrival')
numPeople = sessionStorage.getItem('numPeople')
budget = sessionStorage.getItem('budget')

# ChatGPT에 input으로 넣어줄 데이터 준비 및 답변의 신뢰성을 향상시키기 위한 다양한 테크닉 사용. README.md 파일의 Reference(techniques to improve reliability) 참조
data = [{
    "role": "system", "content": "assistant is tourism professional for Singapore"
},
    # 1. provided user info for personalized answer.
    {

    "role": "user",
    "content": f'please create Singapore travel plan considering following criteria. First, think step by step about each criterion in turn. (1) for a gender of {gender}, {numPeople} people are consist of the group for a trip. (2) their travel style is {travelStyle}. (3) {budget} korean won per person is the budget for entire trip. (4) they will mainly use {transports} to move from one place to another. (5) duration of travel is starting from {departure} to {arrival}.'
},
    # 2. provided pre-processed bundle dataset which consist of 23 bundles. and guideline for usage of bundle.
    {
    "role": "assistant", "content": f'assistant will create travel plan only using bundles which can be found following dataset: {ref}. think step by step following guideline in turn when using bundle. guideline : (1)maximum three bundles can be used in one day. (2)when creating daily plan, only one bundle can be used for each time window (morning, afternoon, evening). (3)when presenting items in a bundle, minimum two items to maximum five items can be selected'
},
    # 3. provided logical steps for answer generation.
    {
    "role": "assistant", "content": f'when creating answer, think step by step. first, plan will be divided such as Day 1, Day 2, Day 3, etc. Second, when creating daily plan, Day will be divided by three time windows(morning, afternoon, evening). Thrid, for each time window, one bundle can be used per time window. Fourth, for items in a bundle, answer format will be (attraction number : attraction name)'
},
    # 4. example questions considering all criterian. (#1, #2, #3)
    {
    "role": "assistant",
    "content": "assistant will create singapore travel plan by thinking step by step. first, consider user criteria provided ahead. second, selecting suitable bundles from bundle list considering guideline. third, generate travel plan based on example."
},
    # 5. translate language from English to Korean.
    {
    "role": "assistant",
    "content": "when return answer, assistant will translate language from English to Korean."
},
    # 6. auto reply after return answer to user.
    {
    "role": "assistant",
    "content": "after return answer to user, assistant will give additional message to user such as '이 계획이 유용하다면 즐거운 여행이 되길 바라며, 더 궁금한 사항이 있으시면 AI에게 추가적으로 질문해 보세요."
},
]

# DOM을 활용하여 요소들을 선택하여 변수로 할당
inputChat = document.querySelector(".textbox")
buttonChat = document.querySelector("button")
chatList = document.querySelector("ul")

# 화면에 뿌려줄 데이터, 질문들
questionData = []

# 화면에 질문 그려주는 함수
def printQuestion():
    li = document.createElement("li")
    li.classList.add("question")
    for el in questionData:
        li.innerHTML = f'<div class="divQuestion">나 : {el["content"]}</div>'
        chatList.appendChild(li)
    questionData.clear()

# 화면에 답변 그려주는 함수
def printAnswer(answer):
    answer = answer.split("\n\n")
    li = document.createElement("li")
    li.classList.add("answer")
    container = document.createElement("div")
    container.classList.add("divAnswer")
    container.innerHTML = 'AI : '
    for _, item in enumerate(answer):
        flexItem = document.createElement('div')
        flexItem.classList.add(f'chat-item')
        flexItem.innerHTML = item
        container.append(flexItem)
        li.append(container)
    chatList.appendChild(li)

# AddEventListener 실행을 위한 콜백함수
def eventPushData(e):
    e.preventDefault()
    userInputData = inputChat.value
    inputChat.value = ""
    data.append({
        "role": "user",
        "content": userInputData})
    questionData.append({
        "role": "user",
        "content": userInputData})
    printQuestion()
    asyncio.ensure_future(main())

# 버튼을 클릭하면 이벤트 활성화되어 콜백함수 실행
eventPush = create_proxy(eventPushData)
buttonChat.addEventListener("click", eventPush)

# ChatGPT API 통신을 위한 함수
async def main():
    headers = {"Content-type": "application/json"}
    body = json.dumps(data)
    response = await request(f"{baseurl}/", body=body, method="POST", headers=headers)
    res = await response.json()
    printAnswer(res["choices"][0]["message"]["content"])
