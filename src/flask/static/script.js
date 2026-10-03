document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const button = document.querySelector(".btn-estimate");

    if (!form || !button) {
        return;
    }

    form.addEventListener("submit", () => {
        button.disabled = true;
        button.style.opacity = "0.75";
        button.style.cursor = "wait";

        const buttonText = button.childNodes[0];

        if (buttonText) {
            buttonText.textContent = "Calculating...";
        }
    });
});