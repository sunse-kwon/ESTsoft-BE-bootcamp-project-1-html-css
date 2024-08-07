
function getAuthUser() {
    const token = localStorage.getItem('token'); // Get the JWT token from localStorage

    axios.get('http://api.bundletripbychat.com/validate-jwt/', {
        headers: {
            Authorization: `Bearer ${token}`, // Add the token to the request headers
        },
    })
    .then(response => {
        // handle success
        console.log(' sunse kwon!');
        console.log(response);
    })
    .catch(error => {
        // handle error
        location.href=`/html/login.html`
        console.log(error);
    })
    .finally(function () {
        // always executed
    });

}


// 메인 페이지의 form의 input들의 선택된 값을 챗 페이지로 전달해주는 함수
function handleSubmit () {
    const gender  = document.querySelector('input[name="gender"]:checked').value;
    const transports  = document.querySelectorAll('input[type="checkbox"]:checked')
    let output = []
    transports.forEach((item) => {
        output.push(item.value)
    } );
    const travelStyle  = document.querySelector('input[name="travel-style"]:checked').value;
    const departure  = document.querySelector('input[name="departure"]').value;
    const arrival  = document.querySelector('input[name="arrival"]').value;
    const numPeople  = document.querySelector('input[name="num-people"]').value;
    const budget  = document.querySelector('input[name="budget"]').value;

    sessionStorage.setItem('gender',gender )
    sessionStorage.setItem('transports',output )
    sessionStorage.setItem('travelStyle',travelStyle )
    sessionStorage.setItem('departure',departure )
    sessionStorage.setItem('arrival',arrival )
    sessionStorage.setItem('numPeople',numPeople )
    sessionStorage.setItem('budget',budget )

    return ;
}


