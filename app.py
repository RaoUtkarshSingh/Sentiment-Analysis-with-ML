import sys
import os

# Set base directory to the folder containing app.py
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import streamlit as st
import pickle
import re
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

nltk.download('stopwords', quiet=True)

# ------------------ SETUP ------------------
st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

# Load stopwords (preserve negation words)
stop_words = set(stopwords.words('english'))
stop_words = stop_words - {'not', 'no', 'never'}

# ------------------ LOAD MODEL ------------------
MODEL_PATH      = os.path.join(BASE_DIR, "ML", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "ML", "vectorizer.pkl")

try:
    model      = pickle.load(open(MODEL_PATH, "rb"))
    vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))
except FileNotFoundError as e:
    st.error(
        f"**Model files not found.**\n\n"
        f"`{e}`\n\n"
        f"Please ensure `model.pkl` and `vectorizer.pkl` are located at:\n"
        f"- `{MODEL_PATH}`\n"
        f"- `{VECTORIZER_PATH}`"
    )
    st.stop()

# ------------------ DATABASE ------------------
def safe_insert(review, cleaned, prediction, confidence):
    try:
        from Database.db import insert_prediction
        insert_prediction(review, cleaned, prediction, confidence)
    except Exception as e:
        st.warning(f"Could not save to database. Please check your MySQL connection. Error: {e}")

# Session history
if "history" not in st.session_state:
    st.session_state.history = []

# ------------------ TEXT CLEANING ------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'not\s+bad', 'good', text)
    text = re.sub(r'not\s+good', 'bad', text)
    text = re.sub('<.*?>', ' ', text)
    text = re.sub('[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# ------------------ PREDICTION ------------------
def predict(text):
    cleaned = clean_text(text)
    vec     = vectorizer.transform([cleaned])
    pred    = model.predict(vec)[0]
    probs   = model.predict_proba(vec)[0]
    return pred, probs, cleaned

# ------------------ SIDEBAR ------------------
st.sidebar.title("Settings")

theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])

page = st.sidebar.radio("Navigate", [
    "Home",
    "Model Comparison",
    "History"
])

# Apply dark theme
if theme == "Dark":
    st.markdown(
        """
        <style>
        body {background-color: #0E1117; color: white;}
        </style>
        """,
        unsafe_allow_html=True
    )

# ------------------ HOME ------------------
if page == "Home":
    st.title("Sentiment Analysis Dashboard")
    st.write("Analyze movie reviews using a trained Machine Learning model.")

    user_input = st.text_area("Enter your review:")

    if st.button("Analyze"):
        if user_input.strip() == "":
            st.warning("Please enter a review before analyzing.")
        else:
            pred, probs, cleaned = predict(user_input)

            st.subheader("Cleaned Text")
            st.write(cleaned)

            st.subheader("Prediction Result")

            if pred == "positive":
                confidence = probs[1]
                st.success(f"Positive ({confidence*100:.2f}%)")
                st.progress(int(confidence * 100))
            else:
                confidence = probs[0]
                st.error(f"Negative ({confidence*100:.2f}%)")
                st.progress(int(confidence * 100))

            # Save to database
            safe_insert(user_input, cleaned, pred, float(confidence))

            # Save to session history
            st.session_state.history.append({
                "text":       user_input,
                "cleaned":    cleaned,
                "prediction": pred,
                "confidence": round(confidence * 100, 2)
            })

            # Word Cloud
            if cleaned.strip():
                st.subheader("Word Cloud")
                wc = WordCloud(background_color='black').generate(cleaned)
                fig, ax = plt.subplots()
                ax.imshow(wc)
                ax.axis("off")
                st.pyplot(fig)

# ------------------ MODEL COMPARISON ------------------
elif page == "Model Comparison":
    st.title("Model Comparison")

    data = pd.DataFrame({
        "Model":    ["Logistic Regression", "Naive Bayes", "SVM"],
        "Accuracy": [0.898, 0.868, 0.895],
        "F1 Score": [0.900, 0.868, 0.896]
    })

    st.dataframe(data)
    st.bar_chart(data.set_index("Model"))

# ------------------ HISTORY ------------------
elif page == "History":
    st.title("Prediction History")

    if len(st.session_state.history) == 0:
        st.info("No predictions made yet.")
    else:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download History as CSV",
            csv,
            "history.csv",
            "text/csv"
        )
