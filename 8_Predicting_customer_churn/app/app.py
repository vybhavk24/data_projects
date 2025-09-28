"""
This is a Flask web application that provides an interface and API for predicting customer churn using a pre-trained machine learning pipeline.
	1. It loads a saved churn prediction model pipeline and the corresponding feature schema from disk.
	2. The home page (`/`) renders a form with predefined options for categorical features, allowing users to 
        input customer data for prediction.
	3. The `/predict` route accepts form submissions, processes input values with type coercion and defaults, 
        runs the data through the model, and returns the prediction along with the churn probability in an HTML result page.
	4. The `/api/predict` endpoint accepts JSON requests with the required features, performs prediction using the model, 
        and returns the results as a JSON response for programmatic integration.
	5. Numeric inputs are carefully parsed and converted, including handling special cases like the `SeniorCitizen` field.
	6. The app runs on port 5000, ready to serve both web users and API clients for real-time churn prediction.

In essence, this app provides a user-friendly and API-accessible front end for the churn prediction model, 
enabling easy deployment and interaction with the machine learning solution.
"""

from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os
import json

app = Flask(__name__)

# Loading pipeline
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'churn_pipeline.joblib')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'feature_schema.json')

model = joblib.load(MODEL_PATH)
with open(SCHEMA_PATH, 'r') as f:
    schema = json.load(f)

FEATURES = schema['features']

# Helper to coerce types for numeric columns
NUMERIC = ['tenure','MonthlyCharges','TotalCharges','SeniorCitizen']

def parse_form(form):
    data = {}
    for feat in FEATURES:
        val = form.get(feat)
        if val is None:
            # fallback default
            data[feat] = None
            continue
        # numeric conversion
        if feat in NUMERIC:
            # SeniorCitizen might come as '0'/'1' or 'Yes'/'No'
            try:
                # handle SeniorCitizen string value 'Yes'/'No'
                if feat == 'SeniorCitizen':
                    if val.lower() in ['yes','y','true','1']:
                        data[feat] = 1
                    elif val.lower() in ['no','n','false','0']:
                        data[feat] = 0
                    else:
                        data[feat] = int(val)
                else:
                    if '.' in val:
                        data[feat] = float(val)
                    else:
                        data[feat] = float(val)
            except:
                # fallback to median like default
                data[feat] = 0.0
        else:
            data[feat] = val
    return data

@app.route('/', methods=['GET'])
def index():
    options = {
        'gender': ['Female','Male'],
        'Partner': ['Yes','No'],
        'Dependents': ['Yes','No'],
        'PhoneService': ['Yes','No'],
        'MultipleLines': ['No','Yes','No phone service'],
        'InternetService': ['DSL','Fiber optic','No'],
        'OnlineSecurity': ['Yes','No','No internet service'],
        'OnlineBackup': ['Yes','No','No internet service'],
        'DeviceProtection': ['Yes','No','No internet service'],
        'TechSupport': ['Yes','No','No internet service'],
        'StreamingTV': ['Yes','No','No internet service'],
        'StreamingMovies': ['Yes','No','No internet service'],
        'Contract': ['Month-to-month','One year','Two year'],
        'PaperlessBilling': ['Yes','No'],
        'PaymentMethod': ['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'],
    }
    return render_template('index.html', features=FEATURES, options=options)

@app.route('/predict', methods=['POST'])
def predict():
    form = request.form
    data = parse_form(form)
    df = pd.DataFrame([data], columns=FEATURES)
    proba = model.predict_proba(df)[0,1]
    pred = int(model.predict(df)[0])
    return render_template('result.html', prediction=pred, probability=round(float(proba),4))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    # Accept JSON body
    req = request.get_json()
    if not req:
        return jsonify({'error': 'No JSON body found'}), 400
    # Expect dict with keys = FEATURES
    df = pd.DataFrame([req], columns=FEATURES)
    proba = model.predict_proba(df)[0,1]
    pred = int(model.predict(df)[0])
    return jsonify({'prediction': pred, 'probability': float(proba)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)