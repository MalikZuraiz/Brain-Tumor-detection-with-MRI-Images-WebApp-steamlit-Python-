import streamlit as st
import cv2
import tensorflow as tf
import numpy as np
import pyttsx3

#passed

def preprocess_image(image):
    speak_text("Preprocessing the Image, Please Wait")
    pred_img = cv2.resize(image, (224, 224))
    pred_img = pred_img.reshape(1, 224, 224, 3)
    pred_img = pred_img.astype("float32") / 255.0
    return pred_img

def load_model():
    loaded_model = tf.keras.models.load_model('BrainTumor.h5')
    return loaded_model

def predict_tumor(image):
    speak_text("Predicting")
    pred_img = preprocess_image(image)
    loaded_model = load_model()
    output = loaded_model.predict(pred_img)
    return output

def display_result(image, output,name):
    st.image(image, caption='Uploaded Image', use_column_width=True)
    if output[0][0] >= 0.5:
        st.write('Brain Tumor Detected')
        st.write(name +' Please consult a doctor for further evaluation.')
        speak_text(name +' I am sad to say but Brain Tumor Detected. Please consult a doctor for further evaluation.')
    else:
        st.write('No Brain Tumor Detected '+ name )
        st.write(name +' Congratulations! Your brain appears to be healthy.')
        speak_text(name +' Congratualations! No Brain Tumor Detected. Your brain appears to be healthy.')

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()

def app():
    st.title('Brain Tumor Detection Using MRI Images')
    #speak_text("A Web Application For Diagnostics using AI Models")

    # Add input fields for name and details
    name = st.text_input("Name:")
    age = st.number_input("Age:", min_value=0, max_value=150)
    gender = st.radio("Gender:", ("Male", "Female", "Other"))
    phone_number = st.text_input("Phone Number:")
    st.markdown('### Upload an MRI Image')
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png"])

    if uploaded_file is not None:
        # Add a button to initiate the prediction
        if st.button("Predict"):
            speak_text("Image Uploaded, Sending for Prediction")
            image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
            output = predict_tumor(image)
            display_result(image, output,name)

            # Calculate and display the model accuracy
            model_accuracy = output
            st.write(f"Model Accuracy: {model_accuracy}")
    

if __name__ == '__main__':
    app()
