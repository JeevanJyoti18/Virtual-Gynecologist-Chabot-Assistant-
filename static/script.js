document.addEventListener("DOMContentLoaded", function() {
    // Autofocus input field on page load
    const userInput = document.getElementById("user_input");
    if (userInput) {
        userInput.focus();
    }

    // Submit form on Enter key (if not already submitting)
    if (userInput) {
        userInput.addEventListener("keydown", function(event) {
            if (event.key === "Enter") {
                event.preventDefault();
                document.getElementById("ask_form").submit();
            }
        });
    }

    // Scroll chat history to the bottom
    const chatHistory = document.getElementById("chat_history");
    if (chatHistory) {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
});
