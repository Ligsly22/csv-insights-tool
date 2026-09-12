#LCAVE practice

#1 L = load
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import numpy as np

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
        percent_unique = df[column].nunique() / len(df)

        if percent_unique < 0.15:
            counts = df[column].value_counts()
            st.bar_chart(counts)
        else:
            fig, ax = plt.subplots()
            sns.histplot(df[column], ax=ax)
            st.pyplot(fig)
    else:
        st.write("Chart not available for non-numeric columns.")


# Database
    st.subheader("Save to Database")
#Show top 10 in ranking based on category
    conn = sqlite3.connect("data.db")
    df.to_sql("uploaded_data", conn, if_exists="replace", index=False)
    preview = pd.read_sql(f"SELECT * FROM uploaded_data ORDER BY {column} DESC LIMIT 10", conn)
    st.write(preview)

# Correlation
    st.subheader("Correlation Analysis")

    numeric_df = df.select_dtypes(include='number')
    correlation_matrix = numeric_df.corr()
    st.write(correlation_matrix)
# Heatmap- with column selection
    st.subheader("Correlation Heatmap")
    st.write("Correlation shows how strongly two stats move together — values near 1 mean they rise and fall together, values near -1 mean one rises as the other falls, and values near 0 mean there's little relationship between them.")
    st.write("Note: correlation shows that two stats move together, not which one causes the other, or which one matters more.")
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    selected_columns = st.multiselect("Choose columns to compare", numeric_columns)

    if selected_columns:
        correlation_matrix = df[selected_columns].corr()

        fig, ax = plt.subplots()
        mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax, vmin=-1, vmax=1, mask=mask)
        st.pyplot(fig)

        st.write(correlation_matrix)
    else:
        st.write("Select at least one column above to see correlations.")

#E = Export
    st.subheader("Export")

    csv_data = df.to_csv(index=False)

    st.download_button(
        label="Download cleaned CSV",
        data=csv_data,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
    