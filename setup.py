from setuptools import setup

setup(name='shelf_finder',
      version='0.1',
      description='Find books on specific shelves from your goodreads to-read list',
      url='http://github.com/alexisraykhel/shelf_finder',
      author='Alexis Raykhel',
      author_email='alexisizatt@gmail.com',
      packages=[
          'ast',
          'fuzzywuzzy',
          'json',
          'pandas',
          'requests',
          'streamlit',
          'xmltodict'
      ])
