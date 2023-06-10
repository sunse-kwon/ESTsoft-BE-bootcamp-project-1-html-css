const loadData = JSON.parse(localStorage.getItem('rawdata'))

const main = document.querySelector('main')
main.classList.add('output-main')

const section = document.createElement("section")
section.classList.add("display-grid")

for (i of loadData.data) {
    const flexItem = document.createElement('div')
    flexItem.classList.add('travel-item')
    if (i[4] === null) {
        continue
    }
    const imgItem = document.createElement('img')
    imgItem.classList.add('thumbnail')
    imgItem.setAttribute('alt', "image unavailable")
    imgItem.setAttribute('src', `https://www.visitsingapore.com/${i[4].slice(22)}`)

    const nameItem = document.createElement('h2')
    nameItem.classList.add('place-name')
    nameItem.innerText =` No. ${i[2]} ` + `${i[7]}`

    const overviewItem = document.createElement('p')
    overviewItem.classList.add('overview')
    overviewItem.innerHTML = `<strong>Description</strong> : ${i[13]}`

    const addressItem = document.createElement('p')
    addressItem.classList.add('address')
    addressItem.innerHTML = `<strong>Address</strong> : ${i[11]}`

    const openinghourItem = document.createElement('p')
    openinghourItem.classList.add('open-hour')
    openinghourItem.innerHTML = `<strong>Opening hour</strong> : ${i[16]}`

    flexItem.append(nameItem,imgItem,overviewItem,addressItem,openinghourItem);
    section.append(flexItem)
    main.append(section)
}


