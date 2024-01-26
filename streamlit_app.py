import streamlit as st
import pandas as pd
import joblib

# Load the trained RandomForest model
model = joblib.load('rf_classifier.joblib')

# Function to get user input
def get_user_input():
    # Create widgets for each feature. Adjust according to your features.
    feature_1 = st.number_input('Feature 1', min_value=0.0, max_value=100.0, value=50.0)
    feature_2 = st.number_input('Feature 2', min_value=0.0, max_value=100.0, value=50.0)
    # Add more input features as needed

    # Create a DataFrame from the inputs
    features = pd.DataFrame([[feature_1, feature_2]], columns=['feature_1', 'feature_2'])
    return features

# Main function for the Streamlit app
def main():
    st.title('Random Forest Model Prediction')

    # Get user input
    input_df = get_user_input()

    # Prediction
    if st.button('Predict'):
        prediction = model.predict(input_df)
        st.write(f'Prediction: {prediction[0]}')

# Run the app
if __name__ == '__main__':
    main()
