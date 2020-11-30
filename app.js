const p1Button = document.querySelector('#p1Button');
const p2Button = document.querySelector('#p2Button');
const resetButton = document.querySelector('#reset');

const p1Display = document.querySelector('#p1Display');
const p2Display = document.querySelector('#p2Display');

const playTo = document.querySelector('#playto');

let p1Score = 0;
let p2Score = 0;

p1Display.innerHTML = p1Score;
p2Display.innerHTML = p2Score;

p1Button.addEventListener('click', () => {
    p1Score++;
    p1Display.innerHTML = p1Score;

    if (p1Score >= playTo.value) {
        p1Display.className = "has-text-success";
        p2Display.className = "has-text-danger";
        p1Button.disabled = true;
        p2Button.disabled = true;
    };
});

p2Button.addEventListener('click', () => {
    p2Score++;
    p2Display.innerHTML = p2Score;

    if (p2Score >= playTo.value) {
        p1Display.className = "has-text-danger";
        p2Display.className = "has-text-success";
        p1Button.disabled = true;
        p2Button.disabled = true;
    };
});

resetButton.addEventListener('click', () => {
    p1Score = 0;
    p2Score = 0;
    
    p1Display.innerHTML = p1Score;
    p2Display.innerHTML = p2Score;

    p1Display.className = "";
    p2Display.className = "";

    p1Button.disabled = false;
    p2Button.disabled = false;
});