// Get DOM elements
const englishText = document.getElementById('englishText');
const translateBtn = document.getElementById('translateBtn');
const clearBtn = document.getElementById('clearBtn');
const speakBtn = document.getElementById('speakBtn');
const copyBtn = document.getElementById('copyBtn');
const outputCard = document.getElementById('outputCard');
const kannadaText = document.getElementById('kannadaText');
const charCount = document.querySelector('.char-count');
const errorMessage = document.getElementById('errorMessage');
const successMessage = document.getElementById('successMessage');

let lastTranslation = '';

// Update character count
englishText.addEventListener('input', () => {
    const count = englishText.value.length;
    charCount.textContent = `${count}/500`;
});

// Clear button
clearBtn.addEventListener('click', () => {
    englishText.value = '';
    outputCard.style.display = 'none';
    charCount.textContent = '0/500';
    hideMessages();
    englishText.focus();
});

// Translate button
translateBtn.addEventListener('click', translate);

// Allow Enter key to translate (Ctrl+Enter)
englishText.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        translate();
    }
});

// Speak button
speakBtn.addEventListener('click', speak);

// Copy button
copyBtn.addEventListener('click', copyToClipboard);

// Translate function
async function translate() {
    const text = englishText.value.trim();

    if (!text) {
        showError('Please enter some English text to translate.');
        return;
    }

    // Disable button and show loading
    translateBtn.disabled = true;
    translateBtn.innerHTML = '<i class="fas fa-spinner loading"></i> Translating...';

    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        if (response.ok) {
            kannadaText.textContent = data.kannada;
            lastTranslation = data.kannada;
            outputCard.style.display = 'block';
            hideMessages();
            showSuccess('Translation successful!');
            speakBtn.focus();
        } else {
            showError(data.error || 'Translation failed. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('An error occurred. Please try again.');
    } finally {
        translateBtn.disabled = false;
        translateBtn.innerHTML = '<i class="fas fa-exchange-alt"></i> Translate';
    }
}

// Speak function
async function speak() {
    if (!lastTranslation) {
        showError('No translation to speak. Please translate first.');
        return;
    }

    speakBtn.disabled = true;
    speakBtn.innerHTML = '<i class="fas fa-spinner loading"></i> Speaking...';

    try {
        const response = await fetch('/speak', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: lastTranslation })
        });

        const data = await response.json();

        if (response.ok) {
            showSuccess('Playing Kannada audio...');
        } else {
            showError(data.error || 'Speech failed. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('An error occurred. Please try again.');
    } finally {
        speakBtn.disabled = false;
        speakBtn.innerHTML = '<i class="fas fa-volume-up"></i> Speak';
    }
}

// Copy to clipboard function
function copyToClipboard() {
    if (!lastTranslation) {
        showError('No text to copy.');
        return;
    }

    navigator.clipboard.writeText(lastTranslation).then(() => {
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
        copyBtn.style.background = 'var(--success-color)';
        
        setTimeout(() => {
            copyBtn.innerHTML = originalText;
            copyBtn.style.background = '';
        }, 2000);
    }).catch(err => {
        showError('Failed to copy text.');
    });
}

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'flex';
    successMessage.style.display = 'none';
}

// Show success message
function showSuccess(message) {
    successMessage.textContent = message;
    successMessage.style.display = 'flex';
    errorMessage.style.display = 'none';
    
    // Auto-hide after 3 seconds
    setTimeout(hideMessages, 3000);
}

// Hide all messages
function hideMessages() {
    errorMessage.style.display = 'none';
    successMessage.style.display = 'none';
}

// Focus on input on page load
window.addEventListener('load', () => {
    englishText.focus();
});
