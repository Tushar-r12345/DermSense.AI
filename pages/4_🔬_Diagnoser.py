import collections
import streamlit as st
from PIL import Image
import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from pdfdocument.document import PDFDocument
import base64
from io import BytesIO
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# Define the class labels for your model
classes = ['ekzama', 'healthy', 'pigment', 'vitiligo']

class ConvNet(nn.Module):
    def __init__(self, num_classes=4):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=12, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=12)
        self.relu1 = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2)
        self.conv2 = nn.Conv2d(in_channels=12, out_channels=20, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(num_features=20)
        self.relu2 = nn.ReLU()
        self.conv3 = nn.Conv2d(in_channels=20, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(num_features=32)
        self.relu3 = nn.ReLU()
        self.fc = nn.Linear(in_features=75 * 75 * 32, out_features=num_classes)

    def forward(self, input):
        output = self.conv1(input)
        output = self.bn1(output)
        output = self.relu1(output)
        output = self.pool(output)
        output = self.conv2(output)
        output = self.bn2(output)
        output = self.relu2(output)
        output = self.conv3(output)
        output = self.bn3(output)
        output = self.relu3(output)
        output = output.view(-1, 32 * 75 * 75)
        output = self.fc(output)
        return output

# Load the pre-trained PyTorch model
if torch.cuda.is_available():
    model = torch.load('best_checkpoint20.model')
else:
    model = torch.load('best_checkpoint20.model', map_location=torch.device('cpu'))
# Check if the model is an OrderedDict
if isinstance(model, collections.OrderedDict):
    # If it is an OrderedDict, extract the model parameters
    model_state_dict = model
    model = ConvNet()  # Replace ConvNet with your actual model class
    model.load_state_dict(model_state_dict)
else:
    # If it's already a model object, proceed as usual
    model.eval()

# Function to preprocess the image
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((150, 150))
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    image = transform(image).unsqueeze(0)
    return image

# Function to predict the disease
def predict_disease(image_path):
    image = preprocess_image(image_path)

    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        _, predicted = torch.max(outputs.data, 1)

    predicted_class = classes[predicted.item()]
    return predicted_class, probabilities.numpy()[0]

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

        # Predict the disease
        predicted_class, probabilities = predict_disease(uploaded_file)

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

    # Add a "Print as PDF" button
    if st.button("Print as PDF"):
        # Create a PDF document
        pdf_buffer = BytesIO()
        pdf = PDFDocument(pdf_buffer)

        # Add the information to the PDF document
        pdf.init_report()
        pdf.h1("Predicted Disease")
        pdf.p(predicted_class)
        pdf.h1("Entered Information")
        pdf.p(f"Name: {name}")
        pdf.p(f"Age: {age}")
        pdf.p(f"Gender: {gender}")
        pdf.p(f"Blood Group: {bg}")
        pdf.generate()

        # Save the PDF file
        pdf_buffer.seek(0)
        b64_data = base64.b64encode(pdf_buffer.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64_data}" download="prediction_report.pdf">Download PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

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