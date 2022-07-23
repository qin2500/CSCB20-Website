
console.log("RUN DAM IT!!");

var element = document.getElementById("auth");
checkAuth();
element.onclick = function () {
    checkAuth();
}

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

