import streamlit as st
import pickle

# Load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

# Set the title of the app
st.title('Iris Species Prediction')

# Create input fields for user data
sepal_length = st.number_input('Sepal Length', min_value=0.1, max_value=10.0)
sepal_width = st.number_input('Sepal Width', min_value=0.1, max_value=10.0)
petal_length = st.number_input('Petal Length', min_value=0.1, max_value=10.0)
petal_width = st.number_input('Petal Width', min_value=0.1, max_value=10.0)

# Initialize the result variable
result = ''

# Create a button for prediction
if st.button('Predict'):
    # Check if all inputs are within the valid range
    if (0.1 <= sepal_length <= 10.0) and (0.1 <= sepal_width <= 10.0) and \
       (0.1 <= petal_length <= 10.0) and (0.1 <= petal_width <= 10.0):
        # Make a prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        # Display the result
        st.success(f'The predicted species is: {result}')
    else:
        st.error('Please enter values between 0.1 and 10 for all parameters.')
