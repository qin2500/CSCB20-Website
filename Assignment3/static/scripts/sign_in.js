

var element = document.getElementById("authForm");
checkAuth();
element.onclick = function () {
    checkAuth();
}

var error = document.getElementById('error');

// function showError() {
//     error.style.display = "block";
// }
// function hideError() {
//     error.style.display = "none";
// }

function checkAuth() {
    var select = document.getElementById('auth');
    var value = select.options[select.selectedIndex].value;
    var studentForm = document.getElementById("studentSignUp");
    var instructorForm = document.getElementById("instructorSignUp");
    if (value == "s") {
        instructorForm.style.display = "none";
        studentForm.style.display = "block";
    }
    if (value == "i") {
        studentForm.style.display = "none";
        instructorForm.style.display = "block";
    }

}

