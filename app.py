import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Enhanced Streamlit App")
    
    # Sidebar
    st.sidebar.title("Settings")
    show_data = st.sidebar.checkbox("Show Sample Data")
    
    # Sample data
    df = generate_sample_data()
    
    # Show/hide sample data
    if show_data:
        st.subheader("Sample Data")
        st.write(df)
    
    # Plot histogram
    st.subheader("Histogram of Random Data")
    num_bins = st.slider("Number of Bins", min_value=5, max_value=50, value=20)
    fig, ax = plot_histogram(df, num_bins)
    st.pyplot(fig)  # Pass the figure explicitly to st.pyplot()
    
    # Generate random numbers
    st.subheader("Generate Random Numbers")
    num_points = st.number_input("Number of Points", min_value=10, max_value=1000, value=100)
    min_value = st.number_input("Minimum Value", value=0.0)
    max_value = st.number_input("Maximum Value", value=100.0)
    generate_button = st.button("Generate Random Data")
    if generate_button:
        random_data = generate_random_data(num_points, min_value, max_value)
        st.write("Random Data:")
        st.write(random_data)

def generate_sample_data():
    # Generate sample data
    np.random.seed(0)
    data = np.random.normal(loc=0, scale=1, size=1000)
    df = pd.DataFrame(data, columns=["Value"])
    return df

def plot_histogram(df, num_bins):
    # Plot histogram
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df["Value"], bins=num_bins, kde=True, ax=ax)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Random Data")
    return fig, ax  # Return the figure and axes objects

def generate_random_data(num_points, min_value, max_value):
    # Generate random data
    random_data = np.random.uniform(low=min_value, high=max_value, size=num_points)
    return random_data

if __name__ == "__main__":
    main()
