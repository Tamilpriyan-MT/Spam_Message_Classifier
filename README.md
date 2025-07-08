## 🚨 Building a Real-Time Spam Message Classifier Using Python, Streamlit & ML ##
By Tamilpriyan M— AI & DS Student

📌 Introduction
In a world full of messages, not all of them are safe or useful. From promotional offers to phishing attempts, spam messages continue to be a growing problem. So I decided to build something simple, yet smart — a Spam Message Classifier that can detect not only spam messages but also phishing links, multilingual content, and provide confidence scores in real time.

This blog shares my journey of building this AI-based tool using Python, Streamlit, and machine learning.

🧠 What the Project Does
My app is a web-based tool that:

✅ Detects whether a message is Spam or Ham (not spam)
✅ Supports multilingual text using Google Translate
✅ Detects phishing URLs (like fake login/update links)
✅ Shows a confidence score for predictions
✅ Allows users to upload a CSV of messages for batch classification
✅ Offers a clean mobile-friendly interface using Streamlit

🧰 Tools & Technologies Used
Python
Scikit-learn (Naive Bayes + TF-IDF)
Streamlit — For real-time web interface
Googletrans — To auto-translate non-English messages
Pandas — For CSV handling and preprocessing
Regex & urlparse — For phishing URL detection
🏗 How It Works — Behind the Scenes
1.Model Training
I trained a Multinomial Naive Bayes model using the popular UCI SMS Spam dataset. It uses TF-IDF Vectorizer to extract features from text.

2.Real-time Input
Users can type a message or upload a CSV file.

3.Multilingual Handling
If the message isn’t in English, it’s auto-translated using Google Translate API before classification.

4.Phishing URL Detection
Using regex and a list of keywords (like login, verify, account), the app flags suspicious links inside messages.

5.Confidence Score
The model also returns the probability of a message being spam — shown as a percentage for transparency.

💡 Unique Features
🌐 Multilingual Support: Messages in any language are auto-detected and translated.
🔐 Phishing URL Detection: Adds an extra layer of security beyond spam.
📊 Confidence Score: Shows how sure the model is in its prediction.
📂 Batch Prediction via CSV Upload: Ideal for testing large datasets.
🎯 Fast & Simple UI with Streamlit


🚀 How to Run It Locally
Install dependencies:bash
pip install streamlit scikit-learn pandas googletrans==4.0.0-rc1
2.Run the app:

streamlit run spam_streamlit_app.py
3.Upload your message or CSV and get instant results!

🙌 Final Thoughts
This project helped me explore the real-world application of NLP and machine learning in a useful way. Streamlit made the UI simple, and the multilingual and phishing features added practical value.

If you’re interested in making the internet a safer place — even in small ways — projects like these are a great starting point.
