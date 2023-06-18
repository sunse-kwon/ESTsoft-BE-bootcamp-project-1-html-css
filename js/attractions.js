
// 세션스토리지에서 TOURISM.csv url 가져옴
const url = sessionStorage.getItem('rawURL')

// fetch를 사용하여 csv 파일을 가져와서 파싱 함. 외부 라이브러리 사용(PapaParse-5.0.2).
fetch(url)
.then(response => response.text())
.then(data => Papa.parse(data, { header: true }).data)
.then(data => {

// DOM 사용하여 main 요소를 선택함
const main = document.querySelector("main");
main.classList.add("output-main");

// DOM 사용하여 section을 생성하여 그리드로 사용
const section = document.createElement("section");
section.classList.add("display-grid");

// 파싱한 csv 파일의 107개의 데이터를 순회를 돌면서 카드형태로 그리드 안에 넣어줌
for (const i of data) {
  if (i['IMAGE_PATH'] === null || i['IMAGE_PATH'] === undefined) {
    continue;
  } else {

    // 카드 생성
    const flexItem = document.createElement("div");
    flexItem.classList.add("travel-item");

    // 이미지 요소 생성하여 이미지 주소 넣어줌
    const imgItem = document.createElement("img");
    imgItem.classList.add("thumbnail");
    imgItem.setAttribute("alt", "image unavailable");
    imgItem.setAttribute(
      "src",
      `https://www.visitsingapore.com/${i['IMAGE_PATH'].slice(21)}`
    );
    // div 요소 생성하여 관광지 이름 넣어줌
    const nameItem = document.createElement("div");
    nameItem.classList.add("place-name");
    nameItem.innerText = ` No. ${i['OBJECTID']} ` + `${i['PAGETITLE']}`;

    // p 요소 생성하여 관광지 설명 넣어줌
    const overviewItem = document.createElement("p");
    overviewItem.classList.add("overview");
    overviewItem.innerHTML = `<strong>Description</strong> : ${i['OVERVIEW']}`;

    // p 요소 생성하여 관광지 주소 넣어줌
    const addressItem = document.createElement("p");
    addressItem.classList.add("address");
    addressItem.innerHTML = `<strong>Address</strong> : ${i['ADDRESS']}`;

    // p 요소 생성하여 관광지 개장시간 넣어줌
    const openinghourItem = document.createElement("p");
    openinghourItem.classList.add("open-hour");
    openinghourItem.innerHTML = `<strong>Opening hour</strong> : ${i['OPENING_HO']}`;

    // 값을 넣어준 각 요소를 카드에 순서대로 넣어줌
    flexItem.append(
      nameItem,
      imgItem,
      overviewItem,
      addressItem,
      openinghourItem
    );

    // 그리드 안에 카드를 순서대로 넣어줌
    section.append(flexItem);
    
    // 메인페이지에 그리드 넣어줌
    main.append(section);
  }
}
})
.catch(error => console.error(error));
