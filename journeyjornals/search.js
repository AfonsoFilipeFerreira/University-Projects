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
    like.addEventListener('click', function () {
        this.style.display = "none";
        this.nextElementSibling.style.display = "inline";
    });
});

likeds.forEach(liked => {
    liked.addEventListener('click', function () {
        this.style.display = "none";
        this.previousElementSibling.style.display = "inline";
    });
});