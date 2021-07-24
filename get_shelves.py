# read in books on to-read list
# find top 5 tags for those books

import pandas as pd
import json
import requests
import xmltodict


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
if __name__ == '__main__':
    # Columns to use for lookup: Book Id, Title, Author, ISBN

    with open("goodreads_keys.json", "r") as f:
        my_file = json.load(f)

    df = pd.read_csv("goodreads_library_export.csv")

    to_read_df = df[df['Read Count'] == 0]

    shelves = []
    import time
    for i, x in enumerate(to_read_df.iterrows()):
        time.sleep(1)
        print(f"On {i}/{to_read_df.shape[0]}")
        row = x[1]
        r = make_request(row['Book Id'], my_file['key'])

        if isinstance(r, str):
            shelves.append([])
            print(f"Book {row['Title']} by {row['Author']} didn't work: \n {r}\n--")
        else:
            shelves.append(get_top_shelves(r, 5))

    to_read_df['shelves'] = shelves

    to_read_df.to_csv("goodreads_library_to_read_shelves.csv", index=False)