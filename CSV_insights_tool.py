#LCAVE practice

#1 L = load
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CSV insights tool")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Dataset shape:", df.shape)
    st.write("Total missing values:", df.isnull().sum().sum())
    column = st.selectbox("Select a column to analyze", df.columns)
    

#C = Clean
    st.subheader("Handle Missing Values")

    clean_option = st.selectbox(
        "How do you want to handle missing values?",
        ["Do nothing", "Drop rows with missing values", "Fill missing values with 0"]
    )

    if clean_option == "Drop rows with missing values":
        df = df.dropna(subset=[column])
    elif clean_option == "Fill missing values with 0":
        df = df.fillna(0)
    
    st.write("Dataset shape after cleaning:", df.shape)

#A = Analyze
    st.subheader("Column Analysis")

    st.write(df[column].describe())

#V = Visualize
    st.subheader("Visualize")

    if pd.api.types.is_numeric_dtype(df[column]):
        fig, ax = plt.subplots()
        sns.histplot(df[column], ax=ax)
        st.pyplot(fig)
    else:
        st.write("Chart not available for non-numeric columns.")

#E = Export
    st.subheader("Export")

    csv_data = df.to_csv(index=False)

    st.download_button(
        label="Download cleaned CSV",
        data=csv_data,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
    