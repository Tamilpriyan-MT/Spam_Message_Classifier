import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from googletrans import Translator
from urllib.parse import urlparse

# === Load or train model ===
@st.cache_resource
def load_model():
    df = pd.read_csv("dataset/spam.csv", encoding='latin-1')[["v1", "v2"]]
    df.columns = ["label", "text"]
    df["label_num"] = df.label.map({"ham": 0, "spam": 1})
    
    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("clf", MultinomialNB())
    ])
    model.fit(df["text"], df["label_num"])
    return model

model = load_model()
translator = Translator()

# === Helper: Translate non-English to English ===
def translate_to_english(text):
    try:
        detected = translator.detect(text)
        if detected.lang != "en":
            return translator.translate(text, dest="en").text
        return text
    except:
        return text

# === Helper: Phishing detection ===
def has_phishing_url(text):
    urls = re.findall(r'(https?://\\S+)', text)
    keywords = ["login", "verify", "update", "account", "secure", "bank"]
    for url in urls:
        parsed = urlparse(url)
        for word in keywords:
            if word in parsed.netloc or word in parsed.path:
                return True
    return False

# === Streamlit UI ===
st.title("🚨 Spam Message Classifier")
st.markdown("Supports multilingual text, phishing detection, confidence score, and batch classification.")

# === Single Message Classification ===
message = st.text_area("Type a message to classify:")

if st.button("Classify Single Message"):
    if not message.strip():
        st.warning("Please type something.")
    else:
        translated = translate_to_english(message)
        proba = model.predict_proba([translated])[0]
        pred = model.predict([translated])[0]
        label = "Spam" if pred == 1 else "Ham"
        conf = round(proba[pred] * 100, 2)

        st.markdown(f"**🧠 Prediction:** `{label}`")
        st.markdown(f"**Confidence Score:** {conf}%")
        if has_phishing_url(translated):
            st.error("⚠️ Phishing link detected!")

# === CSV Upload & Batch Classification ===
st.subheader("📤 Upload CSV of messages (with message column)")

file = st.file_uploader("Upload a CSV file (Max 200MB)", type=["csv"])

if file is not None:
    try:
        df = pd.read_csv(file, on_bad_lines='skip')
        st.success("CSV loaded successfully!")

        column = st.selectbox("Select message column", df.columns)

        if st.button("Classify Uploaded Data"):
            with st.spinner("🔄 Classifying messages... Please wait..."):
                df["Translated"] = df[column].astype(str).apply(translate_to_english)
                df["Prediction"] = model.predict(df["Translated"])
                df["Prediction"] = df["Prediction"].map({1: "Spam", 0: "Ham"})
                df["Confidence (%)"] = model.predict_proba(df["Translated"]).max(axis=1) * 100
                df["Phishing Detected"] = df[column].apply(has_phishing_url)

            st.success("✅ Classification complete!")
            st.dataframe(df)
            csv_out = df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Classified CSV", csv_out, file_name="classified_spam.csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
