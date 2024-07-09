const { PythonShell } = require('python-shell');
const port = process.env.PORT || 3000;
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.static('public'));

app.get('/predict', (req, res) => {
    const { sepal_length, sepal_width, petal_length, petal_width } = req.query;

    const options = {
        mode: 'text',
        pythonOptions: ['-u'],
        args: [sepal_length, sepal_width, petal_length, petal_width]
    };

    PythonShell.run('predict.py', options, (err, results) => {
        if (err) {
            console.error('PythonShell error:', err);
            res.status(500).send('An error occurred during prediction.');
        } else {
            console.log('Prediction results:', results);
            res.send(results[0]);
        }
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
