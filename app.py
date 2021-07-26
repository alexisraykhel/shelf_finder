import streamlit as st
import pandas as pd
from ast import literal_eval
from fuzzywuzzy import process
from tidy_shelves import tidy
from get_shelves import get


st.title('📚 Book Finder 📚')

st.write("""
Welcome to shelf finder. Please choose from the following options:
""")

option = st.selectbox(
    'What file do you want to start with?',
     ["Goodreads library", "To read list"])

if option == 'Goodreads library':
    get()
elif option == 'To read list':
    tidy()

