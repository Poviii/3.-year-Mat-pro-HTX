from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model and prepare the DataFrame
model = pickle.load(open('penguin-webapp\model.pkl', 'rb'))
selected_features = ['sepal length', 'sepal width', 'petal length', 'petal width']

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/id/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_data = [request.form[feature] for feature in selected_features]
        prediction = model.predict([input_data])
        print(input_data)

        flower_map = {
            0: 'Iris-setosa',
            1: 'Iris-versicolor',
            2: 'Iris-virginica'
        }
        prediction = flower_map[prediction[0]]
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)

