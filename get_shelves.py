# read in books on to-read list
# find top tags for those books
from io import BytesIO

import pandas as pd
import time
import requests
import xmltodict
import base64
import streamlit as st



def get_data_download_link(df):
    csv = df.to_csv(index=False).encode()
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="goodreads_library_to_read_shelves.csv" target="_blank">Download csv file</a>'
    return href


def make_request(book_id, key):
    try:
        r = requests.get(f"https://www.goodreads.com/book/show/{book_id}.xml?key={key}")
        as_xml = xmltodict.parse(r.content)

        return as_xml['GoodreadsResponse']

    except Exception as t:
        return t


def get_top_shelves(goodreads_response, n):

    try:
        if 'book' in goodreads_response and 'popular_shelves' in goodreads_response['book'] and 'shelf' in goodreads_response['book']['popular_shelves']:

            shelves = goodreads_response['book']['popular_shelves']['shelf']

            shelves2 = [entry for entry in shelves if not 'read' in entry['@name']]

            # TODO some fuzzy matching on shelf names (like, non-fiction vs nonfiction)
            return [entry['@name'] for entry in shelves2[:n]]

        else:
            return []
    except Exception as t:
        print(f"IT DIDN'T WORK!!! \n {goodreads_response} \n {t}")
        return []


# Press the green button in the gutter to run the script.
def get():
    # Columns to use for lookup: Book Id, Title, Author, ISBN
    try:
        my_key = st.secrets["goodreads_key"]

    except Exception as e:
        st.write("Unable to find Goodreads API key.")

    path = st.file_uploader("Upload your goodreads library file", accept_multiple_files=False)

    df = pd.read_csv(path)

    to_read_df = df[df['Read Count'] == 0]

    shelves = []
    for i, x in enumerate(to_read_df.iterrows()):
        time.sleep(1)
        print(f"On {i}/{to_read_df.shape[0]}")
        row = x[1]
        r = make_request(row['Book Id'], my_key)

        if isinstance(r, str):
            shelves.append([])
            print(f"Book {row['Title']} by {row['Author']} didn't work: \n {r}\n--")
        else:
            shelves.append(get_top_shelves(r, 10))
            
    st.write(f"Saving newly generated to read file at: to_read.csv")

    to_read_df.to_csv("to_read.csv", index=False)

    to_read_df['shelves'] = shelves

    st.markdown(get_data_download_link(to_read_df), unsafe_allow_html=True)

    st.write("You can now change the setting at the top to `to read list` "
             "and use the newly generated file.")
