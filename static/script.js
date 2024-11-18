document.getElementById('predict-btn').addEventListener('click', async () => {
    const newsInput = document.getElementById('news-input').value;
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Processing...';

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: newsInput }),
        });

        if (!response.ok) throw new Error('Prediction failed.');

        const data = await response.json();
        resultDiv.textContent = `${data.prediction} (${data.confidence})`;
    } catch (error) {
        resultDiv.textContent = 'Error: ' + error.message;
    }
});
