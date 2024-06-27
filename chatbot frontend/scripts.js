async function sendMessage() {
    const messageInput = document.getElementById('message');
    const message = messageInput.value.trim();

    if (!message) return;
    addMessageToChat('user', message);
    messageInput.value = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        addMessageToChat('bot', data.response, ); // Render HTML content directly
    } catch (error) {
        console.error('Error:', error);
    }
}

function addMessageToChat(sender, message) {
    const chatbox = document.getElementById('chatbox');
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', sender);

    // Insert the received message as HTML
    messageElement.innerHTML = message;

    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}