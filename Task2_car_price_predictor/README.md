# 🚗 Car Price Predictor | OIBSIP Task 2

> 💡 A Machine Learning powered web application that predicts car prices and compares vehicles instantly.

---

## ✨ Key Highlights

✔ 🔮 Predict car price in seconds
✔ ⚖️ Compare two cars side-by-side
✔ ⛽ Fuel-based dynamic car images
✔ 💰 Prices displayed in ₹ (Indian format)
✔ 🎨 Clean and user-friendly UI

---

## 🧠 How It Works

This app uses a trained **Machine Learning model (Random Forest Regressor)** to estimate car prices based on user inputs.

The model is trained on historical car data and learns patterns to predict accurate prices.

---

## 📥 Input Features

The model takes the following inputs:

* 📅 **Year of Manufacture** – Car manufacturing year
* 🚘 **Kilometers Driven** – Total distance covered
* ⛽ **Fuel Type** – Petrol / Diesel / CNG

---

## 📤 Predicted Output

* 💰 **Estimated Car Price (₹)**
* ⚖️ **Comparison Result (if two cars selected)**

---

## 🛠️ Tech Stack

| Technology        | Purpose         |
| ----------------- | --------------- |
| 🐍 Python         | Backend logic   |
| 🌐 Flask          | Web framework   |
| 🤖 Scikit-learn   | ML model        |
| 📊 Pandas & NumPy | Data processing |
| 🎨 HTML/CSS       | Frontend UI     |

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask pandas numpy scikit-learn
```

---

## 🚀 Run Locally

```bash
# Run the application
python app.py
```

👉 Open in browser:
http://127.0.0.1:5000

---

## 📁 Project Structure

```
Task2_Car_Price_Predictor/
│
├── app.py
├── train_model.py
├── car_price_model.pkl
├── car_data.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── images/
│       ├── petrol.png
│       ├── diesel.png
│       └── cng.png
```

---

## 🎯 Project Objective

To build a simple, interactive, and user-friendly Machine Learning web application that helps users:

* Estimate car prices instantly
* Compare vehicles easily
* Understand ML-based predictions

---

## 🚀 Future Improvements

🔹 Add more features like:

* Transmission type (Manual/Automatic)
* Car brand & model

🔹 Improve model accuracy using:

* Larger dataset
* Advanced algorithms (XGBoost, Gradient Boosting)

🔹 Deploy the application online (Render / Railway / AWS)

🔹 Add user login & history tracking

🔹 Enhance UI with charts and analytics

---

## 👨‍💻 Author

**Sumit Tiwari**
B.Tech Computer Science (2025)
📍 Bangalore, karnataka
📧 [sumittiwari62642004@gmail.com](mailto:sumittiwari62642004@gmail.com)

