
// function to transfer user input from main.html to chat.html page.
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


