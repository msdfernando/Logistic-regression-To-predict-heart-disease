import os
import joblib
import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Set page configuration
st.set_page_config(page_title="Heart Assistant",
                   layout="wide",
                   page_icon="🫀")

# Function to load an image and convert it to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to the background image
background_image_path = 'C:/xampp/htdocs/Logistic regression To predict heart disease/images/background6.jpg'
background_image_base64 = get_base64_image(background_image_path)

# Add custom CSS for background image with adjusted brightness
brightness = 100 # Adjust this value to change the brightness (0 for completely black, 100 for original brightness)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        filter: brightness({brightness}%);  /* Adjust brightness here */
    }}
    .stButton > button {{
        font-size: 2em;
        font-weight: bold;
        padding: 0.5em 0.5em;
    }}
    .stTextInput > div > div > input {{
        color: black !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Define the full path to the heart disease model
model_path = 'C:/xampp/htdocs/Logistic regression To predict heart disease/saved_models/heart_disease_model.joblib'

# loading the saved heart disease model
heart_disease_model = joblib.load(model_path)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('NIA Project Prediction System',
                           ['Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0,
                           styles={
                               "nav-link": {"--hover-color": "#f3f702"},
                               "nav-link-selected": {"background-color": "#f71302", "color": "white"},
                           })

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('**Age**')

    with col2:
        sex = st.text_input('**Sex**')

    with col3:
        cp = st.text_input('**Chest Pain types**')

    with col1:
        trestbps = st.text_input('**Resting Blood Pressure**')

    with col2:
        chol = st.text_input('**Serum Cholestoral in mg/dl**')

    with col3:
        fbs = st.text_input('**Fasting Blood Sugar > 120 mg/dl**')

    with col1:
        restecg = st.text_input('**Resting Electrocardiographic results**')

    with col2:
        thalach = st.text_input('**Maximum Heart Rate achieved**')

    with col3:
        exang = st.text_input('**Exercise Induced Angina**')

    with col1:
        oldpeak = st.text_input('**ST depression induced by exercise**')

    with col2:
        slope = st.text_input('**Slope of the peak exercise ST segment**')

    with col3:
        ca = st.text_input('**Major vessels colored by flourosopy**')

    with col1:
        thal = st.text_input('**thal: 0 = normal; 1 = fixed defect; 2 = reversable defect**')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numerical inputs for all fields.'

    st.success(heart_diagnosis)
