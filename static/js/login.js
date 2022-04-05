// modal function to show the registration form
function registerBlock() {
    let registrationForm = document.getElementById("form-modal");
    let loginForm = document.getElementById('login-form');

    console.log(loginForm)

    registrationForm.style.display = 'flex';
    loginForm.style.display = "none";
}


// password validation and submit btn handling disabled on off
const passIn = document.getElementById('password');
const passVar = document.getElementById('password-varify');
const passTag = document.getElementById('pass-tag');
const btnReg = document.getElementById('btn-register')
const passVarTag = document.getElementById('pass-var-tag');

passIn.addEventListener('keyup', (e) => {
    setTimeout(() => {
        if (passIn.value.length < 8) {
            passTag.innerHTML = "Too short minimum 8 charecters";
            passVar.setAttribute('disabled', 'true')
        } else {
            passVar.removeAttribute('disabled')
            passTag.innerHTML = "";

        }
    }, 0)
})

// vlidation on password match
passVar.addEventListener('keyup', (e) => {
    if (passIn.value === passVar.value) {
        btnReg.removeAttribute('disabled')
        passVarTag.innerHTML = ""
    } else {
        passVarTag.innerHTML = "Password does not match"
    }
})