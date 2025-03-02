from flask import Flask, request, url_for, redirect, render_template,jsonify
import pickle
from preprocessor import preprocess_text


model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer_model.pkl", "rb"))

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        news_text = request.form.get("news", "")

        # Preprocess text
        processed_text = preprocess_text(news_text)

        # Convert to TF-IDF vector
        text_vector = vectorizer.transform([processed_text])

        # Predict
        prediction = model.predict(text_vector)[0]

        # Map prediction to label
        result = "Not Fake News" if prediction == 1 else "Fake News"

        return jsonify({"prediction": result}) 

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
