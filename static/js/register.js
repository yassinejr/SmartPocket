const usernameField = document.querySelector('#usernamefield')
const feedbackField = document.querySelector('.invalid-feedback')
usernameField.addEventListener('keyup', (event) => {
    console.log('typing....','typing....');

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
                if (data.username_error){
                    usernameField.classList.add("is-invalid");
                    feedbackField.style.display = "block";
                    feedbackField.innerHTML=`<p>${data.username_error}</p>`
                }
        });
    }
});