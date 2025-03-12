import streamlit as st
import pickle

# Load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

# Set the title of the app
st.title('Iris Species Prediction')

# Create input fields for user data
sepal_length = st.number_input('Sepal Length', min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input('Sepal Width', min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input('Petal Length', min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input('Petal Width', min_value=0.0, max_value=10.0, step=0.1)

# Initialize the result variable
result = ''

# Create a button for prediction
if st.button('Predict'):
    # Make a prediction
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    # Display the result
    st.success(f'The predicted species is: {result}')
