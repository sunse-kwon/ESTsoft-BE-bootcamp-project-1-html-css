const loadData = JSON.parse(localStorage.getItem('rawData'))

const body = document.querySelector('body')

for (i of loadData.data) {
    

    const flexItem = document.createElement('div')
    flexItem.classList.add('flex-item')

    
    if (i[3] === null) {
        continue
    }
    const imgItem = document.createElement('img')
    imgItem.classList.add('thumbnail')
    imgItem.setAttribute('alt', " ")
    imgItem.setAttribute('src', `http://visitsingapore.com/${i[3].slice(21)}`)

    const nameItem = document.createElement('h2')
    nameItem.classList.add('placeName')
    nameItem.innerText = `${i[1]}`


    const overviewItem = document.createElement('p')
    overviewItem.classList.add('overview')
    overviewItem.innerText = `description : ${i[2]}`

    const addressItem = document.createElement('p')
    addressItem.classList.add('address')
    addressItem.innerText = `address : ${i[6]}`


    const openinghourItem = document.createElement('p')
    openinghourItem.classList.add('x')
    openinghourItem.innerText = `opening hour : ${i[7]}`


    flexItem.append(nameItem,imgItem,overviewItem,addressItem,openinghourItem); 
    body.append(flexItem)


}


