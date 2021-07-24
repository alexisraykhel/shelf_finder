import streamlit as st
import pandas as pd
from ast import literal_eval
from fuzzywuzzy import process


st.title('📚 To-Read Shelves 📚')


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



@st.cache
def load_data():
    return pd.read_csv(r"C:\Users\alexi\PycharmProjects\goodreads\goodreads_library_to_read_shelves.csv")

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