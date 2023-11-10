document.addEventListener("DOMContentLoaded", function() {
    var dynamicText = document.getElementById("dymanic_text");
    var textArray = ["Welcome!", "Register Now!", "Join Us!"];
    var index = 0;

    setInterval(function() {
        dynamicText.textContent = textArray[index];
        index = (index + 1) % textArray.length;
    }, 1000);
});
