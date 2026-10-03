from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model
try:
    model = joblib.load('boston_housing_model.pkl')
except Exception as e:
    model = None
    print("Error: Could not load 'boston_housing_model.pkl'")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    if request.method == 'POST':
        if model is None:
            prediction_text = "Model is not available."
        else:
            try:
                rm = float(request.form['rm'])
                lstat = float(request.form['lstat'])
                ptratio = float(request.form['ptratio'])

                features = np.array([[rm, lstat, ptratio]])
                prediction = model.predict(features)[0]

                prediction_text = f"Estimated House Price: ${prediction:,.2f}"
            except Exception as e:
                prediction_text = f"Error in inputs: {e}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)