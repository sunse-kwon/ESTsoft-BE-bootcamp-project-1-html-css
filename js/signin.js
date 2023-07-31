function validatePassword() {
    let password = document.getElementById('password').value;
    let repeatPassword = document.getElementById('repeat-password').value;
    if (password != repeatPassword) {
        alert('비밀번호가 일치하지 않습니다.');
        return false;
    }
    return true;
}


const signinForm = document.getElementById('signinForm');

    signinForm.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the default form submission

      // Get form data
      const formData = new FormData(signinForm);
      const userEmail = formData.get('userEmail');
      const userPw = formData.get('userPw');
      const userPwVal = formData.get('userPwVal');
      const userName = formData.get('userName');

      // Make API call using Axios
      axios.post('http://www.bundletripbychat.com/user/register/', {
        email: userEmail,
        password: userPw,
        name: userName,
      })
      .then(response => {
        console.log('register successful!');
        console.log(response);
        // 페이지전환
        location.href=`/html/login.html`
        // 쿠키 저장, 로컬스토리지 저장해서 
        // Handle the response or redirect to a different page
      })
      .catch(error => {
        console.error('Registration failed:', error);
        alert("회원가입실패",error)
        // Handle the error, show error messages, etc.
      });
    });