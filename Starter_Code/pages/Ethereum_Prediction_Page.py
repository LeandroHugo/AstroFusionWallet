import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Ethereum Prediction Model
def eth_prediction_model():
    return np.random.randint(2000, 4000)

# Generate mock Ethereum data for visualization
def generate_random_data():
    return pd.DataFrame({
        'Date': pd.date_range(start='1/1/2022', periods=30),
        'Price': np.random.randint(2000, 4000, size=(30)),
        'Lower_Bound': np.random.randint(1900, 3500, size=(30)),
        'Upper_Bound': np.random.randint(2100, 4100, size=(30))
    })

def dummy_predictor(model):
    if model == "Linear Regression":
        return np.random.randint(2100, 2200)
    elif model == "Decision Tree":
        return np.random.randint(2200, 2300)
    elif model == "Neural Network":
        return np.random.randint(2300, 2400)
    return np.random.randint(2000, 2500)

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
        model = st.selectbox("Choose a Prediction Model", ["Linear Regression", "Decision Tree", "Neural Network"])
        prediction = dummy_predictor(model)
        st.success(f"Predicted Ethereum Price using {model}: ${prediction}")

        # Interactive Visualization
        st.header("Ethereum Price Trends")
        df = generate_random_data()
        fig = px.line(df, x='Date', y='Price', title='Ethereum Price Over Time')
        fig.add_scatter(x=df['Date'], y=df['Lower_Bound'], mode='lines', name='Lower Bound')
        fig.add_scatter(x=df['Date'], y=df['Upper_Bound'], mode='lines', name='Upper Bound')
        st.plotly_chart(fig)

    with col2:
        st.title("Educational Content")
        st.write("""
        **Linear Regression**: A basic predictive modeling technique that establishes a relationship between two variables.
        **Decision Tree**: A decision support tool that uses a tree-like model of decisions and their possible consequences.
        **Neural Network**: Computational systems inspired by the neural networks found in brains, used to estimate functions that depend on a large amount of unknown inputs.
        """)

        st.warning("""
        The cryptocurrency market is volatile. Ensure you make informed decisions and do not solely rely on 
        one prediction model. It's recommended to cross-check with multiple sources.
        """)

if __name__ == "__main__":
    main()
