const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the default form submission

      // Get form data
      const formData = new FormData(loginForm);
      const userEmail = formData.get('userEmail');
      const userPw = formData.get('userPw');

      // Make API call using Axios
      axios.post('http://www.bundletripbychat.com/user/login/', {
        email: userEmail,
        password: userPw,
      })
      .then(response => {
        console.log('Login successful!');
        console.log(response);
        const token = localStorage.setItem('token', response.data.access)
        // 페이지전환
        location.href=`/html/main.html`
        // 쿠키 저장, 로컬스토리지 저장해서 
        // Handle the response or redirect to a different page
      })
      .catch(error => {
        console.error('Login failed:', error);
        alert("로그인실패",error)
        // Handle the error, show error messages, etc.
      });
    });