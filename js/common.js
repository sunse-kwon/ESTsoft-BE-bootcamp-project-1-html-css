
function dynamicHeader() {
    const token = localStorage.getItem('token'); // Get the JWT token from localStorage

    axios.get('http://api.bundletripbychat.com/validate-jwt/', {
        headers: {
            Authorization: `Bearer ${token}`, // Add the token to the request headers
        },
    })
    .then(response => {
        // handle success
        const header = document.querySelector('header')
        header.innerHTML = `
        <header class="header">
        <h1></h1>
        <div class="header-left-section">
            <img class="icon" src="./img/world-tour-icon.svg"/>
            <a class="icon-text" href="./index.html">Bundle Trip Planner by Chat</a>
        </div>
        <div class="header-m-r-section">
            <div class="header-middle-section">
            <a href="./html/signin.html">회원가입</a>
            <button type="button">로그아웃</button>
            <a href="./html/main.html">사용자정보 입력</a>
            </div>
            <div class="header-right-section">
            <a href="./html/attractions.html">여행지 상세정보</a>
            </div>
        </div>
        </header>
            
            `;
        console.log(response);
    })
    .catch(error => {
        // handle error
        
        console.log(error);
        
        const header = document.querySelector('header')
        header.innerHTML = `
        <header class="header">
        <h1></h1>
        <div class="header-left-section">
            <img class="icon" src="./img/world-tour-icon.svg"/>
            <a class="icon-text" href="./index.html">Bundle Trip Planner by Chat</a>
        </div>
        <div class="header-m-r-section">
            <div class="header-middle-section">
            <a href="./html/signin.html">회원가입</a>
            <a href="./html/login.html">로그인</a>
            <a href="./html/main.html">사용자정보 입력</a>
            </div>
            <div class="header-right-section">
            <a href="./html/attractions.html">여행지 상세정보</a>
            </div>
        </div>
        </header>
            
            `;
    })
    .finally(function () {
        // always executed
    });

}