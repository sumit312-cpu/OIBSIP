from flask import Flask, render_template, request, session
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)
app.secret_key = "secret123"

# load model
model = pickle.load(open("model/spam_model.pkl", "rb"))
tfidf = pickle.load(open("model/vectorizer.pkl", "rb"))

ps = PorterStemmer()

# ---------------- TEXT PREPROCESS ----------------
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    y = [i for i in y if i not in stopwords.words('english')]
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# ---------------- KEYWORD CHECK ----------------
def is_spam_keyword(text):
    spam_keywords = ["win", "lottery", "prize", "free", "cash"]
    text = text.lower()
    return any(word in text for word in spam_keywords)

# ---------------- HOME ----------------
@app.route('/')
def home():
    if "inbox" not in session:
        session["inbox"] = []
        session["spam"] = []
    return render_template("index.html", inbox=session["inbox"], spam=session["spam"])

# ---------------- PREDICT ----------------
@app.route('/predict', methods=['POST'])
def predict():
    msg = request.form['message']

    transformed = transform_text(msg)
    vector = tfidf.transform([transformed])
    result = model.predict(vector)[0]

    # FINAL LOGIC
    if result == 1 or is_spam_keyword(msg):
        session["spam"].append(msg)
    else:
        session["inbox"].append(msg)

    return render_template("index.html",
                           inbox=session["inbox"],
                           spam=session["spam"])

# ---------------- CLEAR ----------------
@app.route('/clear')
def clear():
    session["inbox"] = []
    session["spam"] = []
    return render_template("index.html", inbox=[], spam=[])

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)