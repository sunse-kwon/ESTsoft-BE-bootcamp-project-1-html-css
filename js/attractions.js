
// get url from session storage
const url = JSON.parse(sessionStorage.getItem('rawURL'))

// use fetch to get csv file from url. to read csv file in javascript, used external library (PapaParse-5.0.2).
fetch(url)
.then(response => response.text())
.then(data => Papa.parse(data, { header: true }).data)
.then(data => {

// creating card by selecting relevant elements in raw dataset. 
const main = document.querySelector("main");
main.classList.add("output-main");

const section = document.createElement("section");
section.classList.add("display-grid");

for (const i of data) {
  const flexItem = document.createElement("div");
  flexItem.classList.add("travel-item");
  if (i['IMAGE_PATH'] === null || i['IMAGE_PATH'] === undefined) {
    continue;
  }
  const imgItem = document.createElement("img");
  imgItem.classList.add("thumbnail");
  imgItem.setAttribute("alt", "image unavailable");
  imgItem.setAttribute(
    "src",
    `https://www.visitsingapore.com/${i['IMAGE_PATH'].slice(22)}`
  );

  const nameItem = document.createElement("h2");
  nameItem.classList.add("place-name");
  nameItem.innerText = ` No. ${i['OBJECTID']} ` + `${i['PAGETITLE']}`;

  const overviewItem = document.createElement("p");
  overviewItem.classList.add("overview");
  overviewItem.innerHTML = `<strong>Description</strong> : ${i['OVERVIEW']}`;

  const addressItem = document.createElement("p");
  addressItem.classList.add("address");
  addressItem.innerHTML = `<strong>Address</strong> : ${i['ADDRESS']}`;

  const openinghourItem = document.createElement("p");
  openinghourItem.classList.add("open-hour");
  openinghourItem.innerHTML = `<strong>Opening hour</strong> : ${i['OPENING_HO']}`;

  flexItem.append(
    nameItem,
    imgItem,
    overviewItem,
    addressItem,
    openinghourItem
  );
  section.append(flexItem);
  main.append(section);
}
})
.catch(error => console.error(error));
