import streamlit as st
import pandas as pd
import joblib
import random

def get_user_input():
    # Create two columns for inputs
    col1, col2 = st.columns(2)

    with col1:
        st.header('Polymer Properties')
        polymer_repeating_unit_mw = st.number_input('Polymer Repeating Unit Molecular Weight')
        polymer_mw = st.number_input('Polymer Molecular Weight')
        polymer_logp = st.number_input('Polymer LogP')
        tpsa = st.number_input('TPSA')
        num_h_donor = st.number_input('Number of H Donor')

    with col2:
        st.header('Solvent Properties')
        solvent_mw = st.number_input('Solvent Molecular Weight')
        solvent_logp = st.number_input('Solvent LogP')
        solvent_dielectric_constant = st.number_input('Solvent Dielectric Constant')
        solvent_dipole_moments = st.number_input('Solvent Dipole Moments')
        solvent_viscosity = st.number_input('Solvent Viscosity')
        solvent_dd = st.number_input('Solvent δD')
        solvent_dp = st.number_input('Solvent δP')
        solvent_dh = st.number_input('Solvent δH')

    # Create a DataFrame from the inputs (if you need to use these inputs)
    # features = pd.DataFrame([[...]], columns=[...])

    # For now, we're not using these inputs, so just return an empty DataFrame
    return pd.DataFrame()

def main():
    st.title('Solubility Prediction App')

    input_df = get_user_input()

    # Create a 'Predict' button
    if st.button('Predict'):
        # Generate a random prediction when the button is clicked
        prediction = random.choice(["Soluble", "Insoluble"])
        st.write(f'Prediction: {prediction}')

if __name__ == "__main__":
    main()
# Main function for the Streamlit app
# def main():
#    st.title('Predicting if a Solvent Dissolves a Polymer')
#
#    # Get user input
#    input_df = get_user_input()
#
#    # Prediction
#    if st.button('Predict'):
#        prediction = model.predict(input_df)
#        st.write(f'Prediction: {prediction[0]}')
