import collections
import streamlit as st
from PIL import Image
import numpy as np
import base64
from io import BytesIO
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# Define the class labels for your model
classes = ['ekzama', 'healthy', 'pigment', 'vitiligo']


def main():
    # Set the title and layout of the app
    st.title("Disease Prediction")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    # Create input fields for name, age, gender, and blood group
    name = st.text_input("Name")
    age = st.text_input("Age")
    gender = st.text_input("Gender")
    bg = st.text_input("Blood Group")

    if uploaded_file is not None:
        # Display the selected image
        image = Image.open(uploaded_file)
        image = image.resize((300, 300))
        st.image(image, caption='Selected Image', use_column_width=True)


        # Display the confidence scores in a table
        st.subheader("Confidence Scores")
        confidence_data = {'Class': classes, 'Confidence': probabilities}
        confidence_table = st.table(confidence_data)

        # Find and display the predicted class
        predicted_index = np.argmax(probabilities)
        predicted_class = classes[predicted_index]
        st.subheader("Predicted Disease: {}".format(predicted_class))

    st.subheader("Enter Information")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Blood Group:", bg)

    # Footer text and links
    footer_text = "copyright © 2023, All rights reserved.Created by Tushar Pal (iam#11) ! This is prototype only"
    footer_text2= "Follow us on : "
    twitter_link = "https://twitter.com/Tushar48923527"
    github_link = "https://github.com/Tushar-r12345"

    # Display footer
    st.write(footer_text)
    st.write(f"{footer_text2}\n[Twitter]({twitter_link})  |  [Github]({github_link})")

if __name__ == '__main__':
    main()
