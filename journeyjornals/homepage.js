//link para registar a conta

const loginDiv = document.getElementById("Login");
const registerDiv = document.getElementById("Registe");
const registLink = document.getElementById("registLink");

registLink.addEventListener("click", function () {
    loginDiv.style.display = "none";
    registerDiv.style.display = "block";
});

//scrip para confrimação da password

const passwordInput = document.getElementById("pass");
const confirmPasswordInput = document.getElementById("passc");
const signupButton = document.getElementById("signup");

signupButton.addEventListener("click", function () {
    const passwordValue = passwordInput.value;
    const confirmPasswordValue = confirmPasswordInput.value;
    const divalert = document.getElementById("alert");

    if (passwordValue === confirmPasswordValue) {
        document.getElementsByTagName("form")[1].submit();
    } else {
        divalert.style.display = "block"
    }
});

// show password

const eyeHides = document.querySelectorAll('img[src="eye hide.png"]');
const eyeShows = document.querySelectorAll('img[src="eye show.png"]');

eyeHides.forEach(eyeHide => {
  eyeHide.addEventListener('click', function() {
    this.style.display = "none";
    this.nextElementSibling.style.display = "inline";
    const input = this.parentElement.querySelector('input[type="password"]');
    input.type = "text";
  });
});

eyeShows.forEach(eyeShow => {
  eyeShow.addEventListener('click', function() {
    this.style.display = "none";
    this.previousElementSibling.style.display = "inline";
    const input = this.parentElement.querySelector('input[type="text"]');
    input.type = "password";
  });
});


//open dialog box log/regist
const myButtons = document.querySelectorAll('#myButton');
const myDialog = document.querySelector('#myDialog');

myButtons.forEach((myButton) => {
myButton.addEventListener('click', (event) => {
 event.preventDefault();
 myDialog.showModal();
});
});

myDialog.addEventListener('click', (event) => {
if (event.target === myDialog) {
 myDialog.close();
}
});

//show maps 
const toggleButtons = document.querySelectorAll('.toggle-button');

toggleButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        button.parentElement.parentElement.classList.toggle('show-map');
    });
});

//likes
const likes = document.querySelectorAll('img[src="like_button-removebg-preview.png"]');
const likeds = document.querySelectorAll('img[src="liked_button-removebg-preview.png"]');

likes.forEach(like => {
like.addEventListener('click', function() {
this.style.display = "none";
this.nextElementSibling.style.display = "inline";
});
});

likeds.forEach(liked => {
liked.addEventListener('click', function() {
this.style.display = "none";
this.previousElementSibling.style.display = "inline";
});
});

