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

This app uses a trained **Machine Learning model (Random Forest Regressor)** to estimate car prices based on:

- 📅 Year of Manufacture  
- 🚘 Kilometers Driven  
- ⛽ Fuel Type  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|--------|
| 🐍 Python | Backend logic |
| 🌐 Flask | Web framework |
| 🤖 Scikit-learn | ML model |
| 🎨 HTML/CSS | Frontend UI |

---

## 🚀 Run Locally

```bash
# Install required libraries
pip install flask pandas numpy scikit-learn

# Run the application
python app.py

👉 Open in browser:

http://127.0.0.1:5000

📁 Project Structure
Task2_car_price_project/
│
├── app.py
├── car_price_model.pkl
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
|__ car_data.csv

🎯 Project Objective

To build a simple and interactive Machine Learning web app that helps users estimate car prices and compare vehicles.

👨‍💻 Author

Sumit Tiwari
B.Tech CSE (2025)
