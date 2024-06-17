<!DOCTYPE html>
<html>
<head>
    <title>Spam SMS Detection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 30px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            display: block;
            width: 100%;
            padding: 10px;
            font-size: 16px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        #result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Spam SMS Detection</h1>
        <form id="sms-form">
            <div class="form-group">
                <label for="sms-text">SMS Text:</label>
                <textarea id="sms-text" name="sms-text" placeholder="Enter the SMS text here..."></textarea>
            </div>
            <button type="submit">Detect Spam</button>
        </form>
        <div id="result"></div>
    </div>

    <script>
        const smsForm = document.getElementById('sms-form');
        const resultDiv = document.getElementById('result');

        smsForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const smsText = document.getElementById('sms-text').value;

            // Send the SMS text to the server for classification
            const response = await fetch('/classify', {
                method: 'POST',
                body: JSON.stringify({ smsText }),
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();

            // Display the classification results
            const result = document.createElement('p');
            result.textContent = `The SMS is classified as: ${data.result}`;
            resultDiv.innerHTML = '';
            resultDiv.appendChild(result);
        });
    </script>
</body>
</html>
