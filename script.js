//send message

async function sendMessage() {

    const input = document.getElementById("userInput");

    const message = input.value.trim();

    if(message === "") return;

    const chatBox = document.getElementById("chatBox");

    // USER MESSAGE
    const userDiv = document.createElement("div");

    userDiv.classList.add("user-message");

    userDiv.innerText = message;

    chatBox.appendChild(userDiv);

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

    
    // TYPING ANIMATION
    const typingDiv = document.createElement("div");

    typingDiv.classList.add("bot-message");

    typingDiv.innerHTML = `
        <span class="typing">
            <span></span>
            <span></span>
            <span></span>
        </span>
    `;

    chatBox.appendChild(typingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    // FETCH RESPONSE
    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    // DELAY FOR REALISTIC EFFECT
    setTimeout(() => {

        typingDiv.innerText = data.response;

        chatBox.scrollTop = chatBox.scrollHeight;

    }, 1500);
}
    

// ENTER KEY SUPPORT
document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("userInput");

    if(input){

        input.addEventListener("keypress", function(e){

            if(e.key === "Enter"){
                sendMessage();
            }

        });
    }
});


// QUICK REPLY
function quickReply(text){

    document.getElementById("userInput").value = text;

    sendMessage();
}

function newChat(){

    const chatBox = document.getElementById("chatBox");

    chatBox.innerHTML = "";

}

// THEME TOGGLE

const themeToggle = document.getElementById("themeToggle");

if(themeToggle){

    themeToggle.addEventListener("click", () => {

        document.body.classList.toggle("light-mode");

        // SAVE THEME
        if(document.body.classList.contains("light-mode")){

            localStorage.setItem("theme", "light");

            themeToggle.innerText = "☀️";

        } else {

            localStorage.setItem("theme", "dark");

            themeToggle.innerText = "🌙";
        }
    });

    // LOAD SAVED THEME
    window.addEventListener("load", () => {

        const savedTheme = localStorage.getItem("theme");

        if(savedTheme === "light"){

            document.body.classList.add("light-mode");

            themeToggle.innerText = "☀️";
        }
    });
}