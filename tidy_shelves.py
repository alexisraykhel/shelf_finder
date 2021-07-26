import streamlit as st
import pandas as pd
from ast import literal_eval


def tidy_by_shelves(df):
    """

    :param df: the df with shelves
    :return: new df with columns 'shelf', 'title', 'author'
    """

    new_rows = []
    for x in df.iterrows():
        row = x[1]
        shelves = literal_eval(row.shelves)
        for shelf in shelves:
            new_rows.append({'shelf': shelf, 'Title': row.Title, 'Author': row.Author})

    return pd.DataFrame(columns=['shelf', 'Title', 'Author'], data=new_rows)


def tidy(data=None):

    if not data:

        uploaded_file = st.file_uploader("Upload your to-read file", accept_multiple_files=False)

        def load_data():
            return pd.read_csv(uploaded_file)

        data = load_data()

    data = tidy_by_shelves(data)

    st.subheader('Shelf Values')

    st.write(data.shelf.value_counts())

    st.write(data)

    st.subheader('Choose filters')

    shelf_options = list(set(data.shelf))
    shelf_filter = st.multiselect('Shelves', shelf_options)

    st.subheader(f'Only books in the following shelves: {", ".join(shelf_filter)}')

    st.write(data[data.shelf.isin(shelf_filter)])
