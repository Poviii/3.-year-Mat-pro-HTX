from flask import Flask, render_template, request
import pandas as pd
import joblib
import pickle

app = Flask(__name__)

# Load the trained model and prepare the DataFrame
model = pickle.load(open('model.pkl', 'rb'))
selected_features = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)']

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_data = [request.form[feature] for feature in selected_features]
        prediction = model.predict([input_data])[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)