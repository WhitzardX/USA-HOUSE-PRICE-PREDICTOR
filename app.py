import streamlit as st
import pandas as pd
import joblib

# we load the trained model
model = joblib.load(r"C:\Users\olami\Documents\Jupyter\MY JUPITER\Pipeline\USA_lrPipeline.pkl")

#Title
st.title('USA HOUSE PRICE PREDICTOR')
st.markdown('Enter the details of the house to get a predicted price.')

#inputed fields for features
income = st.number_input(
    'Average Area Income',
    min_value=17796.63,
    max_value=107701.75,
    value=68583.11,
    step=1000.0
)

age = st.number_input(
    'Average House Age',
    min_value=2.64,
    max_value=9.52,
    value=5.98,
    step=0.1
)

rooms = st.number_input(
    'Average Number of Rooms',
    min_value=3.24,
    max_value=10.76,
    value=6.99,
    step=0.1
)

bedrooms = st.number_input(
    'Average Number of Bedrooms',
    min_value=2.0,
    max_value=6.5,
    value=3.98,
    step=0.1
)

population = st.number_input(
    'Area Population',
    min_value=172.61,
    max_value=69621.71,
    value=36163.52,
    step=1000.0
)


# Predict effect
if st.button('Predict Price'):
    input_df = pd.DataFrame([{
        'Avg. Area Income': income,
        'Avg. Area House Age': age,
        'Avg. Area Number of Rooms': rooms,
        'Avg. Area Number of Bedrooms': bedrooms,
        'Area Population': population
    }])

    with st.spinner('Predicting...'):
        prediction = model.predict(input_df)[0]
        st.success(f'Estimated House Price: ${prediction:,.2f}')
