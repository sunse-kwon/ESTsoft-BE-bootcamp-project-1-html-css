function dynamicHeaderIdx() {
    const token = localStorage.getItem('token'); // Get the JWT token from localStorage

    axios.get('http://api.bundletripbychat.com/validate-jwt/', {
        headers: {
            Authorization: `Bearer ${token}`, // Add the token to the request headers
        },
    })
    .then(response => {
        // handle success
        const header = document.querySelector('.header-empty-section')
        header.innerHTML = `
            <button type="button">로그아웃</button>
            `;
        console.log(response);
    })
    .catch(error => {
        // handle error
        
        console.log(error);
        
        const header = document.querySelector('.header-empty-section')
        header.innerHTML = `
            <a href="./html/login.html">로그인</a>
            `;
    })
    .finally(function () {
        // always executed
    });

}


function dynamicHeader() {
    const token = localStorage.getItem('token'); // Get the JWT token from localStorage

    axios.get('http://api.bundletripbychat.com/validate-jwt/', {
        headers: {
            Authorization: `Bearer ${token}`, // Add the token to the request headers
        },
    })
    .then(response => {
        // handle success
        const header = document.querySelector('.header-empty-section')
        header.innerHTML = `
            <button type="button">로그아웃</button>
            `;
        console.log(response);
    })
    .catch(error => {
        // handle error
        
        console.log(error);
        
        const header = document.querySelector('.header-empty-section')
        header.innerHTML = `
            <a href="../html/login.html">로그인</a>
            `;
    })
    .finally(function () {
        // always executed
    });

}