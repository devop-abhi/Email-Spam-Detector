import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Configure the webpage
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

# Application heading
st.title("📧 Email Spam Detector")

st.write(
    "Enter a message below to check whether "
    "it is Spam or Not Spam."
)

# Input area
message = st.text_area(
    "Enter your message:",
    placeholder="Type or paste your message here..."
)

# Prediction button
if st.button("Check Message"):

    if message.strip() == "":
        st.warning("Please enter a message first.")

    else:
        # Convert message into numerical features
        message_tfidf = vectorizer.transform([message])

        # Predict the message category
        prediction = model.predict(message_tfidf)[0]

        # Display the result
        if prediction == "spam":
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is NOT SPAM.")

st.divider()

st.caption("Basic Machine Learning Project | Python + Scikit-learn")
