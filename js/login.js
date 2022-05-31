// LOGIN & REGISTER
const sign_in_btn = document.querySelector("#login-btn");
const sign_up_btn = document.querySelector("#regist-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("regist-mode");
});

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("regist-mode");
});