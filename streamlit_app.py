import streamlit as st
import requests

st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detector using LSTM")
st.write("Enter news text below and click 'Predict' to check if it's fake or real.")

# Input text area
news_text = st.text_area("Enter news text here:", height=200)

# Predict button
if st.button("Predict"):
    if not news_text.strip():
        st.warning("Please enter some text before predicting.")
    else:
        try:
            # Send POST request to Flask backend
            url = "http://127.0.0.1:5000/predict"  # Your Flask backend URL
            response = requests.post(url, json={"text": news_text}, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                prediction = data.get("prediction")
                note = data.get("note", "")
                
                if prediction is not None:
                    st.success(f"Prediction score: {prediction}")
                    if prediction >= 0.5:
                        st.warning("⚠️ This news is likely **Fake**")
                    else:
                        st.info("✅ This news is likely **Real**")
                else:
                    st.info(f"Prediction not available. {note}")
            else:
                st.error(f"Error from backend: {response.text}")
        except Exception as e:
            st.error(f"Could not connect to backend. Make sure Flask is running. Details: {e}")
