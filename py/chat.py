from bundle import bundling
from request import request
from utils import genRef
import asyncio
import json
import pandas as pd
import numpy as np
from pyodide.http import open_url
from pyodide.ffi import create_proxy
from js import document, localStorage, sessionStorage

# raw data url
url = (
    "https://raw.githubusercontent.com/sunse523/ormi-dev-project-1/master/data/TOURISM.csv"
)
# openAI baseurl
baseurl = "https://estsoft-openai-api.jejucodingcamp.workers.dev"


# read dataset to create bunddle
rawData = pd.read_csv(open_url(url), sep=',', encoding='unicode_escape')

# save rawData to local storage to be used in other pages
localStorage.setItem('rawdata', rawData.to_json(orient="split"))

# expected time spend created and assigned 60 minute to all temporarily
rawData["EXPECTED_TIME_SPENT"] = 60

# subsetting dataset
rawData = rawData.loc[:, ["OBJECTID", 'LATITUDE', 'LONGTITUDE', "EXPECTED_TIME_SPENT",
                          "PAGETITLE", "OVERVIEW", "IMAGE_PATH", "ADDRESS", "OPENING_HO"]]


# convert pandas dataframe to numpy array to be used in algorithm.
new_data = rawData.values

# bundling process done based on nearst locations
reference = bundling(new_data)
ref = genRef(reference)

# convert numpy array to json file to be used in data for reliability of chatgpt
ref = json.dumps(ref)

# load FORM inputs
gender = sessionStorage.getItem('gender')
transports = sessionStorage.getItem('transports')
travelStyle = sessionStorage.getItem('travelStyle')
departure = sessionStorage.getItem('departure')
arrival = sessionStorage.getItem('arrival')
numPeople = sessionStorage.getItem('numPeople')
budget = sessionStorage.getItem('budget')


#  data preparation to enhance reliability of answer.
data = [{
    "role": "system", "content": "assistant is tourism professional for Singapore"
},
    # 1. provided user info for personalized answer.
    {

    "role": "user",
    "content": f'please create Singapore travel plan considering following criteria. First, think step by step about each criterion in turn. (1) for a gender of {gender}, {numPeople} people are consist of the group for a trip. (2) their travel style is {travelStyle}. (3) {budget} korean won per person is the budget for entire trip. (4) they will mainly use {transports} to move from one place to another. (5) duration of travel is starting from {departure.split("T")[0]} to {arrival.split("T")[0]}.'
},
    # 2. provided pre-processed dataset which consist of bundles. and guideline for usage of bundle.
    {
    "role": "assistant", "content": f'assistant will create travel plan only using bundles which can be found following dataset: {ref}. think step by step following guideline in turn when using bundle. guideline : (1)maximum three bundles can be used in one day. (2)when creating daily plan, only one bundle can be used for each time window (morning, afternoon, evening). (3)when presenting items in a bundle, minimum two items to maximum five items can be selected'
},
    # 3. provided logical steps for answer generation.
    {
    "role": "assistant", "content": f'when creating answer, think step by step. first, plan will be divided such as Day 1, Day 2, Day 3, etc. Second, when creating daily plan, Day will be divided by three time windows(morning, afternoon, evening). Thrid, for each time window, one bundle can be used per time window. Fourth, for items in a bundle, answer format will be (attraction number : attraction name)'
},
    # 4. actual questions considering all criterian. (#1, #2, #3)
    {
    "role": "user",
    "content": "create singapore travel plan by thinking step by step. first, consider user criteria provided ahead. second, selecting suitable Bundles among bundles considering guideline. third, generate travel plan based on example."
},
]


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

    for idx, item in enumerate(answer):
        flexItem = document.createElement('div')
        flexItem.classList.add(f'flex-item-{idx}')
        flexItem.setAttribute(
            'style', "background-color:rgb(250, 188, 240);border-radius:10px;padding:10px;margin:10px;display:flex;justify-content:center;align-items:center")

        flexItem.innerHTML = item
        container.append(flexItem)
        li.append(container)
    chatList.appendChild(li)


# callback function for AddEventListener
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


# submit button
eventPush = create_proxy(eventPushData)
buttonChat.addEventListener("click", eventPush)


# chatGPT API communication
async def main():
    headers = {"Content-type": "application/json"}
    body = json.dumps(data)
    response = await request(f"{baseurl}/", body=body, method="POST", headers=headers)
    res = await response.json()
    printAnswer(res["choices"][0]["message"]["content"])
