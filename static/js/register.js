const usernameField = document.querySelector('#usernamefield')
const feedbackField = document.querySelector('.invalid-feedback')
const emailField = document.querySelector('#emailfield')
const emailfeedbackField = document.querySelector('.invalid-email-feedback')
const passwordField = document.querySelector('#passwordfield')
const showpasswordToggle = document.querySelector('.showpasswordToggle')



usernameField.addEventListener('keyup', (event) => {

    const usernameValue = event.target.value;


    console.log("usernameValue",usernameValue);

    usernameField.classList.remove("is-invalid");
    feedbackField.style.display = "none";

    if (usernameValue.length > 0){
        fetch("/authentication/validate_username",{
            body: JSON.stringify({ username : usernameValue}),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data)=> {
                console.log("data", data);
                usernameSuccessOutput.style.display = "none";
                if (data.username_error){
                    usernameField.classList.add("is-invalid");
                    feedbackField.style.display = "block";
                    feedbackField.innerHTML=`<p>${data.username_error}</p>`
                }
        });
    }
});


emailField.addEventListener('keyup', (event) => {
    console.log('typing email....','typing email....');

    const emailValue = event.target.value;

    console.log("emailValue",emailValue);
    emailField.classList.remove("is-invalid");
    emailfeedbackField.style.display = "none";

    if (emailValue.length > 0){
        fetch("/authentication/validate_email",{
            body: JSON.stringify({ email : emailValue}),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data)=> {
                console.log("data", data);
                if (data.email_error){
                    emailField.classList.add("is-invalid");
                    emailfeedbackField.style.display = "block";
                    emailfeedbackField.innerHTML=`<p>${data.email_error}</p>`
                }
        });
    }
});


const handleToggleInput = (e) => {
    if (showpasswordToggle.textContent === 'Show') {
        showpasswordToggle.textContent = 'Hide';

        passwordField.setAttribute("type", "text");
    }else{
        showpasswordToggle.textContent = 'Show'
        passwordField.setAttribute("type", "password");
    }
};

showpasswordToggle.addEventListener("click",handleToggleInput);