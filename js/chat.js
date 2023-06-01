let $input = document.querySelector("input");
let $button = document.querySelector("button");

let data = [
  {
    role: "system",
    content: "assistant is tourism professional for Singapore",
  },
];

let url = `https://estsoft-openai-api.jejucodingcamp.workers.dev/`;

$button.addEventListener("click", (e) => {
  e.preventDefault();
  userInputData = $input.value;
  $input.value = "";

  data.push({
    role: "user",
    content: userInputData,
  });
  // 답변 목록도 push를 하면 맥락을 이해하여 답변이 가능합니다.
  // DAY 1, DAY 2, DAY 3와 같은 형식으로 답변해줘라고 미리 학습을 시켜놓으면 split('DAY') 이런 식으로 Card를 만들 수 있습니다.

  chatGptAPI();
});

function chatGptAPI() {
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
    redirect: "follow",
  })
    .then((res) => res.json())
    .then((res) => {
      // console.log(res)
      // console.log(res.choices[0].message.content)
      document.querySelector("#contents").innerText =
        res.choices[0].message.content;
    });
  // 아래 코드는 fetch 성공, 실패, 통신 중 여부와 상관없이 실행됩니다. 비동기에요.
  console.log("hello world");
}
