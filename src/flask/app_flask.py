from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask( __name__)


MODEL_PATH ="boston_housing_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")

except Exception as e:
    model = None
    print(f"Error: Could not load model: {e}")


@app.route("/", methods=["GET", "POST"])
def index():

    prediction_text = None
    error = None

    if request.method == "POST":

        if model is None:
            error = "Model is not available."

        else:
            try:
                # Get input values
                rm = float(request.form["rm"])
                lstat = float(request.form["lstat"])
                ptratio = float(request.form["ptratio"])

                # Backend validation
                if rm < 1:
                    raise ValueError(
                        "Average rooms must be at least 1."
                    )

                if lstat < 0:
                    raise ValueError(
                        "LSTAT cannot be negative."
                    )

                if ptratio < 1:
                    raise ValueError(
                        "PTRATIO must be at least 1."
                    )

                # Prepare features
                features = np.array([
                    [rm, lstat, ptratio]
                ])

                # Make prediction
                prediction = model.predict(features)[0]

                # Display prediction
                prediction_text = f"${prediction:,.2f}"

            except ValueError as e:
                error = str(e)

            except KeyError:
                error = "Please provide all required inputs."

            except Exception as e:
                error = f"Prediction failed: {e}"

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)