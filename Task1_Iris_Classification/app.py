from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("iris_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        sl = float(request.form["sl"])
        sw = float(request.form["sw"])
        pl = float(request.form["pl"])
        pw = float(request.form["pw"])

        data = np.array([[sl, sw, pl, pw]])
        prediction = model.predict(data)[0]

        if prediction == 0:
            flower = "Setosa"
            image = "setosa.jpg"
        elif prediction == 1:
            flower = "Versicolor"
            image = "versicolor.jpg"
        else:
            flower = "Virginica"
            image = "virginica.jpg" 

        return render_template("index.html", result=flower, image=image)

    except:
        return render_template("index.html", result="Invalid Input")

if __name__ == "__main__":
    app.run(debug=True)