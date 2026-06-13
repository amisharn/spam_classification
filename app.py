import streamlit as st
import requests

st.title("Spam Detector")

email = st.text_area("Enter email text here:")

if st.button("Predict"):
    if email.strip()=="":
        st.warning("Please enter some text!")
    else:
        response = requests.post(
           "https://spam-classification-2plh.onrender.com/predict",
           json = {"text":email} 
        )
        result = response.json()

        st.subheader("Result: ")
        label = result["prediction"].lower()
        if label == "spam":
            st.error("SPAM!")
        else:
            st.success("NOT SPAM")


        st.caption(f"Input: {result['email']}")