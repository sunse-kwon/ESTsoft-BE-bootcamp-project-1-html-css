const loadData = JSON.parse(localStorage.getItem('rawdata'))

const main = document.querySelector('main')

for (i of loadData.data) {
    const flexItem = document.createElement('div')
    flexItem.classList.add('flex-item')
    if (i[4] === null) {
        continue
    }
    const imgItem = document.createElement('img')
    imgItem.classList.add('thumbnail')
    imgItem.setAttribute('alt', "image unavailable")
    imgItem.setAttribute('src', `https://www.visitsingapore.com/${i[4].slice(22)}`)

    const nameItem = document.createElement('h2')
    nameItem.classList.add('placeName')
    nameItem.innerText =` No. ${i[2]}: ` + `${i[7]}`

    const overviewItem = document.createElement('p')
    overviewItem.classList.add('overview')
    overviewItem.innerText = `description : ${i[13]}`

    const addressItem = document.createElement('p')
    addressItem.classList.add('address')
    addressItem.innerText = `address : ${i[11]}`

    const openinghourItem = document.createElement('p')
    openinghourItem.classList.add('open-hour')
    openinghourItem.innerText = `opening hour : ${i[16]}`

    flexItem.append(nameItem,imgItem,overviewItem,addressItem,openinghourItem); 
    main.append(flexItem)
}


