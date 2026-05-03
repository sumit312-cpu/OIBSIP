# 🌸 Iris Flower Classification Web App | OIBSIP Task 1

> 💡 A Machine Learning-based web application that predicts the species of an Iris flower using user input features.

---

## ✨ Key Highlights

✔ 🔍 Predict Iris flower species instantly
✔ 🎯 High accuracy using Logistic Regression
✔ 🌐 Interactive Flask-based web app
✔ 🎨 Clean and user-friendly UI
✔ 📊 Real-time prediction with ML integration

---

## 🧠 How It Works

This application uses a trained **Logistic Regression model** to classify Iris flowers into different species based on input measurements.

The model is trained on the **Iris Dataset (from Scikit-learn)** and then saved using pickle for deployment in a Flask web application.

---

## 📥 Input Features

The model takes the following inputs:

* 🌿 **Sepal Length**
* 🌿 **Sepal Width**
* 🌸 **Petal Length**
* 🌸 **Petal Width**

---

## 📤 Predicted Output

* 🌼 **Iris Flower Species**

  * Setosa
  * Versicolor
  * Virginica

---

## 🛠️ Tech Stack

| Technology        | Purpose                |
| ----------------- | ---------------------- |
| 🐍 Python         | Backend logic          |
| 🌐 Flask          | Web framework          |
| 🤖 Scikit-learn   | Machine Learning model |
| 📊 Pandas & NumPy | Data processing        |
| 🎨 HTML/CSS       | Frontend UI            |

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask numpy pandas scikit-learn joblib
```

---

## 🚀 Run Locally

```bash
# Navigate to folder
cd Task1_Iris_Classification

# Run app
python app.py
```

👉 Open in browser:
http://127.0.0.1:5000/

---

## 📁 Project Structure

```
Task1_Iris_Classification/
│
├── app.py
├── iris_model.pkl
├── requirements.txt
│
├── static/
│   ├── style.css
│   └── images/
│
├── templates/
│   └── index.html
│
├── notebook/
│
└── README.md
```

---

## 🎯 Project Objective

To build a simple and interactive Machine Learning web application that:

* Classifies Iris flower species
* Demonstrates ML model deployment using Flask
* Provides real-time predictions

---

## 🚀 Future Improvements

🔹 Deploy the application online (Render / Railway / AWS)

🔹 Add more classification models (KNN, Decision Tree, SVM)

🔹 Improve UI with better visuals and animations

🔹 Add confidence score for predictions

🔹 Convert project into REST API

---

## 👨‍💻 Author

**Sumit Tiwari**
📍 Bangalore, Karnataka
🎓 B.Tech Computer Science (2025)
📧 [sumittiwari62642004@gmail.com](mailto:sumittiwari62642004@gmail.com)

---

## 📌 Acknowledgement

This project was completed as part of the **Oasis Infobyte Data Science Internship (OIBSIP)**.

---

## ⭐ Support

If you found this project helpful, please ⭐ star the repository!


