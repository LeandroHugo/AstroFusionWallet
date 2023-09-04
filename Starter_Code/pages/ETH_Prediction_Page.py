import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
import plost  # Import the new plotting library

# Load the trained models
decision_tree_model = joblib.load('models/decision_tree_model.joblib')
linear_regression_model = joblib.load('models/linear_regression_model.joblib')
neural_network_model = joblib.load('models/neural_network_model.joblib')
random_forest_model = joblib.load('models/random_forest_model.joblib')

# Load the historical data
data = pd.read_csv('models/ethereum_historical_data.csv')

# Get the most recent price from the dataset
current_price = data['price'].iloc[-1]

def get_predictions(features):
    dt_pred = decision_tree_model.predict(features)
    lr_pred = linear_regression_model.predict(features)
    nn_pred = neural_network_model.predict(features)
    rf_pred = random_forest_model.predict(features)

    return dt_pred, lr_pred, nn_pred, rf_pred

# Mock function for future features, replace with your real function to generate future features
def generate_future_features():
    return pd.DataFrame({
        '30_day_avg': [current_price] * 10,   # Maintain the order
        '10_day_avg': [current_price] * 10,
        'daily_return': [0.02] * 10  # Mock daily return
    })

future_features = generate_future_features()
predictions = get_predictions(future_features)

def main():
    st.set_page_config(page_title="Advanced TimeLock Wallet: ETH Prediction", layout="wide", initial_sidebar_state="collapsed")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.title('Advanced TimeLock Wallet: ETH Prediction Page')

        st.write("""
        Dive deep into Ethereum predictions. Explore various models, visualize historical data, and get insights tailored for the 
        Advanced TimeLock Wallet users.
        """)

        # Model Selection and Customization
        model = st.selectbox("Choose a Prediction Model", ["Linear Regression", "Decision Tree", "Neural Network", "Random Forest"])

        if model == "Linear Regression":
            prediction = predictions[1]
        elif model == "Decision Tree":
            prediction = predictions[0]
        elif model == "Neural Network":
            prediction = predictions[2]
        else:
            prediction = predictions[3]
        
        # Show today's price
        st.write(f"Today's Ethereum Price: ${current_price}")
        st.success(f"Predicted Ethereum Prices for the next 10 days using {model}: {prediction}")

        # Interactive Visualization using Plost
        days = list(range(1, 11))
        prediction_df = pd.DataFrame({
            'Day': days,
            'Predicted_Price': prediction
        })
        
        plost.line_chart(
            data=prediction_df,
            x='Day',
            y='Predicted_Price'
        )

    with col2:
        st.title("Educational Content")
        st.write("""
        **Linear Regression**: A basic predictive modeling technique that establishes a relationship between two variables.
        **Decision Tree**: A decision support tool that uses a tree-like model of decisions and their possible consequences.
        **Neural Network**: Computational systems inspired by the neural networks found in brains, used to estimate functions that depend on a large amount of unknown inputs.
        **Random Forest**: An ensemble learning method that operates by constructing multiple decision trees during training and outputs the average prediction of the individual trees for regression problems.
        """)

        st.warning("""
        The cryptocurrency market is volatile. Ensure you make informed decisions and do not solely rely on 
        one prediction model. It's recommended to cross-check with multiple sources.
        """)

if __name__ == "__main__":
    main()