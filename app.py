import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Stats 21 Discussion Project")
st.subheader("William Sun, 805949205")

# File uploader
file = st.file_uploader("Upload a CSV file", type="csv")

# Check if a file is uploaded
if file is not None:
    # Read the CSV file
    df = pd.read_csv(file)

    # Display the DataFrame
    st.dataframe(df)

    # Basic statistics
    st.header("Basic Statistics")
    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape[1])

    # Variable Types
    st.header("Variable Types")
    st.write("Categorical Variables:", df.select_dtypes(include="object").columns.tolist())
    st.write("Numerical Variables:", df.select_dtypes(include=["int", "float"]).columns.tolist())
    st.write("Boolean Variables:", df.select_dtypes(include="bool").columns.tolist())

    # Column Selection
    st.header("Column Selection")
    selected_column = st.selectbox("Select a column", df.columns)
    st.write("Selected Column:", selected_column)

    # Perform analysis based on column type
    if df[selected_column].dtype == "object":
        # Categorical column analysis
        st.subheader("Categorical Column Analysis")

        # Calculate proportions of each category level
        category_proportions = df[selected_column].value_counts(normalize=True)

        # Display proportions in a table
        st.write("Proportions of each category level:")
        st.table(category_proportions)

        # Create a customized barplot
        st.subheader("Customized Barplot")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x=selected_column)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        # Numerical column analysis
        st.subheader("Numerical Column Analysis")

        # Calculate the five-number summary
        five_num_summary = df[selected_column].describe().loc[['min', '25%', '50%', '75%', 'max']]

        # Display the five-number summary in a table
        st.write("Five-number Summary:")
        st.table(five_num_summary)

        # Create a customized distribution plot
        st.subheader("Customized Distribution Plot")
        fig, ax = plt.subplots()
        sns.histplot(data=df, x=selected_column, kde=True)
        plt.xlabel(selected_column)
        plt.ylabel("Density")
        plt.title("Distribution Plot")
        st.pyplot(fig)