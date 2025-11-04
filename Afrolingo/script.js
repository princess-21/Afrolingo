document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sourceLang = document.getElementById('source-language');
    const targetLang = document.getElementById('target-language');
    const outputDiv = document.getElementById('output');
    const submitButton = document.getElementById('submit-button');

    // Handle the Submit button click
    submitButton.addEventListener('click', () => {
        const text = userInput.value;

        // POST data to the Flask backend
        fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                source: sourceLang.value,
                target: targetLang.value,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Display the translation in the output div
            outputDiv.innerText = data.translation || 'Translation failed.';
        })
        .catch(error => {
            console.error('Error:', error);
            outputDiv.innerText = 'An error occurred.';
        });
    });
});
