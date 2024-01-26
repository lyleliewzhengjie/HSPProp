import streamlit as st
import pandas as pd
import joblib

def random_prediction():
    # Randomly choose between "Soluble" and "Insoluble"
    return random.choice(["Soluble", "Insoluble"])

def get_user_input():
    # Create widgets for each feature
    polymer_repeating_unit_mw = st.number_input('Polymer Repeating Unit Molecular Weight', min_value=0.0, max_value=10000.0, value=500.0)
    polymer_mw = st.number_input('Polymer Molecular Weight', min_value=0.0, max_value=100000.0, value=10000.0)
    polymer_logp = st.number_input('Polymer LogP', min_value=-10.0, max_value=10.0, value=0.0)
    tpsa = st.number_input('TPSA', min_value=0.0, max_value=1000.0, value=100.0)
    num_h_donor = st.number_input('Number of H Donor', min_value=0, max_value=10, value=1)
    solvent_mw = st.number_input('Solvent Molecular Weight', min_value=0.0, max_value=1000.0, value=100.0)
    solvent_logp = st.number_input('Solvent LogP', min_value=-10.0, max_value=10.0, value=0.0)
    solvent_dielectric_const = st.number_input('Solvent Dielectric Constant', min_value=0.0, max_value=100.0, value=10.0)
    solvent_dipole_moments = st.number_input('Solvent Dipole Moments', min_value=0.0, max_value=10.0, value=1.0)
    solvent_viscosity = st.number_input('Solvent Viscosity', min_value=0.0, max_value=1000.0, value=10.0)
    solvent_d_d = st.number_input('Solvent δD', min_value=0.0, max_value=100.0, value=10.0)
    solvent_d_p = st.number_input('Solvent δP', min_value=0.0, max_value=100.0, value=10.0)
    solvent_d_h = st.number_input('Solvent δH', min_value=0.0, max_value=100.0, value=10.0)

    # Create a DataFrame from the inputs
    features = pd.DataFrame([[polymer_repeating_unit_mw, polymer_mw, polymer_logp, tpsa, num_h_donor, 
                              solvent_mw, solvent_logp, solvent_dielectric_const, solvent_dipole_moments, 
                              solvent_viscosity, solvent_d_d, solvent_d_p, solvent_d_h]], 
                            columns=['Polymer Repeating Unit MW', 'Polymer MW', 'Polymer LogP', 'TPSA', 'Number of H Donor', 
                                     'Solvent MW', 'Solvent LogP', 'Solvent Dielectric Constant', 'Solvent Dipole Moments', 
                                     'Solvent Viscosity', 'Solvent δD', 'Solvent δP', 'Solvent δH'])
    return features

def main():
    # Other parts of your app, including get_user_input()
    # ...

    # Get user input
    input_df = get_user_input()

    # Randomly predict output
    prediction = random_prediction()

    # Display the prediction
    st.write(f"The prediction is: {prediction}")

# Run the app
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

# Run the app
if __name__ == '__main__':
    main()
