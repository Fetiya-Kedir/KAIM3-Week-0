import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the dashboard
st.title("Solar Radiation Dashboard")

# File uploader for dataset
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Proceed if a file is uploaded
if uploaded_file is not None:
    # Load the uploaded dataset
    data = pd.read_csv(uploaded_file)
    
    # Dataset summary
    st.header("Dataset Summary")
    st.write(data.describe())

    # Visualize GHI over time if the column exists
    if "GHI" in data.columns:
        st.header("GHI Over Time")
        st.line_chart(data["GHI"])
    else:
        st.error("The uploaded dataset does not contain the 'GHI' column.")

    # Filter by GHI values
    if "GHI" in data.columns:
        st.sidebar.header("Filter GHI Values")
        min_val, max_val = st.sidebar.slider("Select GHI Range", int(data["GHI"].min()), int(data["GHI"].max()), 
                                             (int(data["GHI"].min()), int(data["GHI"].max())))
        filtered_data = data[(data["GHI"] >= min_val) & (data["GHI"] <= max_val)]

        st.header("Filtered Data")
        st.write(filtered_data)

        # GHI Distribution
        st.header("GHI Distribution")
        plt.hist(filtered_data["GHI"], bins=20, color="skyblue", edgecolor="black")
        st.pyplot()

    # Dynamic column visualization
    st.sidebar.header("Visualize Relationships")
    if len(data.columns) > 1:
        x_axis = st.sidebar.selectbox("Select X-axis", data.columns)
        y_axis = st.sidebar.selectbox("Select Y-axis", data.columns)
        st.header(f"Scatter Plot: {y_axis} vs {x_axis}")
        st.write(data.plot(x=x_axis, y=y_axis, kind="scatter"))
        st.pyplot()
else:
    st.warning("Please upload a dataset to proceed.")
