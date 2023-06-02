import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Stats 21 Discussion Project")
st.subheader("William Sun, 805949205")

file = st.file_uploader("Upload a CSV file", type="csv")

if file is not None:
    df = pd.read_csv(file)

    st.dataframe(df)

    st.header("Basic Statistics")
    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape[1])

    st.header("Variable Types")
    st.write("Categorical Variables:", df.select_dtypes(include="object").columns.tolist())
    st.write("Numerical Variables:", df.select_dtypes(include=["int", "float"]).columns.tolist())
    st.write("Boolean Variables:", df.select_dtypes(include="bool").columns.tolist())

    st.header("Column Selection")
    selected_column = st.selectbox("Select a column", df.columns)
    st.write("Selected Column:", selected_column)

    if df[selected_column].dtype == "object":
        st.subheader("Categorical Column Analysis")

        category_proportions = df[selected_column].value_counts(normalize=True)

        st.write("Proportions of each category level:")
        st.table(category_proportions)

        st.subheader("Customized Barplot")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x=selected_column)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        st.subheader("Numerical Column Analysis")

        five_num_summary = df[selected_column].describe().loc[['min', '25%', '50%', '75%', 'max']]

        st.write("Five-number Summary:")
        st.table(five_num_summary)

        st.subheader("Customized Distribution Plot")
        fig, ax = plt.subplots()
        sns.histplot(data=df, x=selected_column, kde=True)
        plt.xlabel(selected_column)
        plt.ylabel("Density")
        plt.title("Distribution Plot")
        st.pyplot(fig)
