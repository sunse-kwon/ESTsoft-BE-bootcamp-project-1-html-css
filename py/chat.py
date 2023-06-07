from bundle import bundling
from request import request
import asyncio
import json
import pandas as pd
import numpy as np
from pyodide.http import open_url
from pyodide.ffi import create_proxy
from js import document, localStorage, sessionStorage

url = (
    "https://raw.githubusercontent.com/sunse523/ormi-dev-project-1/master/py/TOURISM.csv"
    )

baseurl = "https://estsoft-openai-api.jejucodingcamp.workers.dev"    


#pre-processing of dataset to create bunddle 
rawData = pd.read_csv(open_url(url), sep=',', encoding= 'unicode_escape')

# expected time spend created and assigned 60 minute to all temporarily
rawData["TIME"] = 60
new_data = rawData.loc[:,["OBJECTID","PAGETITLE","OVERVIEW", "IMAGE_PATH", 'LATITUDE', 'LONGTITUDE',"ADDRESS","OPENING_HO","TIME"]]

localStorage.setItem('rawData', 
new_data.to_json(orient="split"))

new_data = new_data.loc[:,["OBJECTID", "LATITUDE", "LONGTITUDE", "TIME"]]
new_data = new_data.values
reference = bundling(new_data)


ref = json.dumps(reference)



#load form data
gender = sessionStorage.getItem('gender')
transports = sessionStorage.getItem('transports')
travelStyle = sessionStorage.getItem('travelStyle')
departure = sessionStorage.getItem('departure')
arrival = sessionStorage.getItem('arrival')
numPeople = sessionStorage.getItem('numPeople')
budget = sessionStorage.getItem('budget')


# pre-training with bundled dataset
data = [
{"role": "system","content": "assistant is tourism professional for Singapore"},
{"role": "assistant", "content": f'this is bundled data of attractions based on provided raw dataset. each bunddle has at least 2 to 5 attractions in it. assistant will answer based on this data :{ref}'},

{"role": "user", "content": f'please create Singapore travel plan considering following criteria.  for {gender}, {numPeople} group of people will join this trip. their travel style is {travelStyle} with {budget} won per person as a budget. they will mainly use {transports} to go one place to another. duration of travel is starting from {departure.split("T")[0]} to {arrival.split("T")[0]}'},
]


inputChat = document.querySelector("input");
buttonChat = document.querySelector("button");
chatList = document.querySelector("ul");


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


#callback function
def eventPushData(e):
    e.preventDefault();
    userInputData = inputChat.value;
    inputChat.value = "";
    data.append({
        "role": "user",
        "content": userInputData})
    questionData.append({
        "role": "user",
        "content": userInputData})
    print(questionData)
    printQuestion()  
    asyncio.ensure_future(main())
    
# submit button
eventPush = create_proxy(eventPushData)
buttonChat.addEventListener("click", eventPush);


# 화면에 답변 그려주는 함수
def printAnswer(answer):
    li = document.createElement("li")
    li.classList.add("answer")
    li.innerHTML = f'<div class="divAnswer"> AI : {answer}</div>'
    chatList.appendChild(li)        


# chatGPT API communication
async def main():
    headers = {"Content-type": "application/json"}
    body = json.dumps(data)
    response = await request(f"{baseurl}/", body=body, method="POST", headers=headers)
    res = await response.json()
    printAnswer(res["choices"][0]["message"]["content"])
