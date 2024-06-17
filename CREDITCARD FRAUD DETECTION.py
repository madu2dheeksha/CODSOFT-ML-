<!DOCTYPE html>
<html>
<head>
    <title>Credit Fraud Detection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 500px;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            margin-bottom: 10px;
        }
        .form-group input[type="text"],
        .form-group input[type="number"] {
            width: 100%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .form-group input[type="submit"] {
            width: 100%;
            height: 40px;
            background-color:rgb(137, 219, 134);
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .form-group input[type="submit"]:hover {
            background-color: rgb(137, 219, 134)
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Credit Fraud Detection</h2>
        <form id="credit-fraud-form">
            <div class="form-group">
                <label for="credit-limit">Credit Limit:</label>
                <input type="number" id="credit-limit" name="credit-limit">
            </div>
            <div class="form-group">
                <label for="age">Age:</label>
                <input type="number" id="age" name="age">
            </div>
            <div class="form-group">
                <label for="income">Income:</label>
                <input type="number" id="income" name="income">
            </div>
            <div class="form-group">
                <label for="employment-status">Employment Status:</label>
                <select id="employment-status" name="employment-status">
                    <option value="employed">Employed</option>
                    <option value="unemployed">Unemployed</option>
                </select>
            </div>
            <div class="form-group">
                <label for="credit-history">Credit History:</label>
                <select id="credit-history" name="credit-history">
                    <option value="good">Good</option>
                    <option value="bad">Bad</option>
                </select>
            </div>
            <div class="form-group">
                <input type="submit" value="Detect Fraud">
            </div>
        </form>
        <div id="result"></div>
    </div>

    <script>
        const creditFraudForm = document.getElementById('credit-fraud-form');
        const resultDiv = document.getElementById('result');

        creditFraudForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const creditLimit = document.getElementById('credit-limit').value;
            const age = document.getElementById('age').value;
            const income = document.getElementById('income').value;
            const employmentStatus = document.getElementById('employment-status').value;
            const creditHistory = document.getElementById('credit-history').value;

            // Send the data to the server for classification
            const response = await fetch('/classify', {
                method: 'POST',
                body: JSON.stringify({
                    creditLimit,
                    age,
                    income,
                    employmentStatus,
                    creditHistory,
                }),
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();

            // Display the classification results
            const result = document.createElement('p');
            result.textContent = `The credit fraud detection result is: ${data.result}`;
            resultDiv.appendChild(result);
        });
    </script>
</body>
</html>
