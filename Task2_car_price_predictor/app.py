from flask import Flask, render_template, request
import pickle
import matplotlib.pyplot as plt


app = Flask(__name__)

model = pickle.load(open('car_price_model.pkl', 'rb'))
# 🔥 HOME ROUTE
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    car_image = None
    graph = None

    if request.method == 'POST':
        year = int(request.form['year'])
        km = int(request.form['km'])
        fuel = int(request.form['fuel'])

        prediction = int(model.predict([[year, km, fuel]])[0] * 100000)

        # image logic
        if fuel == 0:
            car_image = "images/petrol.webp"
        elif fuel == 1:
            car_image = "images/diesel.webp"
        else:
            car_image = "images/cng.webp"

        
      

    return render_template('index.html',
                           prediction=prediction,
                           car_image=car_image,
                           )


# 🔥 COMPARE ROUTE
@app.route('/compare', methods=['POST'])
def compare():
    yearA = int(request.form['yearA'])
    kmA = int(request.form['kmA'])
    fuelA = int(request.form['fuelA'])

    yearB = int(request.form['yearB'])
    kmB = int(request.form['kmB'])
    fuelB = int(request.form['fuelB'])

    priceA = int(model.predict([[yearA, kmA, fuelA]])[0] * 100000)
    priceB = int(model.predict([[yearB, kmB, fuelB]])[0] * 100000)

    better = "Car A" if priceA > priceB else "Car B"

    return render_template('index.html',
                           priceA=priceA,
                           priceB=priceB,
                           better=better)


if __name__ == "__main__":
    app.run(debug=True)