import streamlit as st
import pyttsx3

#passed

st.set_page_config(page_title='Diagnostics Website', page_icon=':brain:', layout='wide', initial_sidebar_state='expanded')


def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()


def main():
    st.title('Diagnostics Web Application')
    st.write('Welcome to our Diagnostics Website Powered by AI Models')
    st.write('We offer a wide range of medical tests and diagnostics to help you monitor your health and detect potential conditions early. Our advanced technology and expert professionals ensure accurate results and reliable services.')
     # Add a video
    st.image('images/Capture.png', use_column_width=True )
    
    st.markdown('## Brain Tumor Detection Using MRI Images')
    st.write('Our diagnostics website provides a specialized service for brain tumor detection using MRI images. We utilize deep learning algorithms and advanced image processing techniques to analyze MRI scans and identify potential brain tumors.')
    st.write('Key Features:')
    st.write('- Accurate and reliable detection of brain tumors')
    st.write('- Quick and efficient analysis of MRI images')
    st.write('- Expert evaluation by medical professionals')
    st.write('- Prompt notifications and recommendations for further evaluation')

    # Add an image
    st.image('images/braintumorimage.jpg', use_column_width=True )

    st.markdown('### Model Summary')
    st.code('''
    Model: "sequential"
    _________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================
     conv2d (Conv2D)             (None, 222, 222, 64)      1792     
                                                                 
     conv2d_1 (Conv2D)           (None, 220, 220, 32)      18464    
                                                                 
     max_pooling2d (MaxPooling2D  (None, 110, 110, 32)     0        
     )                                                               
                                                                 
     conv2d_2 (Conv2D)           (None, 108, 108, 32)      9248     
                                                                 
     conv2d_3 (Conv2D)           (None, 106, 106, 32)      9248     
                                                                 
     max_pooling2d_1 (MaxPooling  (None, 53, 53, 32)       0        
     2D)                                                             
                                                                 
     flatten (Flatten)           (None, 89888)             0        
                                                                 
     dense (Dense)               (None, 256)               23011584 
                                                                 
     dense_1 (Dense)             (None, 128)               32896    
                                                                 
     dense_2 (Dense)             (None, 64)                8256     
                                                                 
     dense_3 (Dense)             (None, 32)                2080     
                                                                 
     dense_4 (Dense)             (None, 1)                 33       
    ''')

    st.markdown('## Diabetes Tests')
    st.write('We also offer comprehensive diabetes tests to assess your blood glucose levels and monitor your diabetes management. Our tests provide valuable insights into your condition and help guide treatment decisions.')
    st.write('Key Features:')
    st.write('- Blood glucose testing and monitoring')
    st.write('- HbA1c measurement for long-term glucose control assessment')
    st.write('- Diabetes risk assessment and screening')
    st.write('- Personalized diabetes management recommendations')
    st.image('images/diabetesImage.jpg', use_column_width=True)

   

    st.markdown('### Our Commitment to Accuracy')
    st.write('At our diagnostics website, we prioritize accuracy and reliability in all our tests and services. Our advanced technologies and rigorous quality control measures ensure highly precise results.')
    st.write('We continuously strive for excellence and have achieved a remarkable accuracy rate of 98% in our diagnostic tests.')

    st.markdown('## Book an Appointment')
    st.write('Ready to take control of your health? Book an appointment with us today and experience our top-quality diagnostics services.')
    st.button('Book Appointment')

    st.markdown('## Contact Us')
    st.write('If you have any questions or need further information, our dedicated customer support team is available to assist you. Get in touch with us via the contact details provided below:')
    st.write('- Phone: 0344-2607654')
    st.write('- Email: malikzuraiz1214@gmail.com')
    st.write('- Address: Bahria University E-8 Islamabad, Pakistan')
    speak_text("Diagnostics Web Application")
    speak_text("Welcome to our Diagnostics Website Powered by AI Models")
if __name__ == '__main__':
    main()
