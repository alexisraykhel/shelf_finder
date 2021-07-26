# Shelf Finder

This streamlit app allows you to filter
your unread goodreads books by genre.

I made it because often I want to read
a book on my to-read list, but it is
ridiculously long and not easily navigable.
And sometimes I just want to read "horror" 
but don't remember what books on my list 
are in that category!

## How it works

If you have used this app before, you can use your previously generated
shelves file with the option "To read list". If not, follow these steps:

* Select "Goodreads library" in the selection box after these instructions
* Provide your goodreads library export csv,
downloadable from your account
[here](https://www.goodreads.com/review/import).
* I'll get the top shelves for each book (this takes
  1 second per book, thanks to API rate limiting)
* Download the output
* Select "To read list" in the selection box
* Provide the newly downloaded csv
* You then select which shelf/shelves you are
interested in
* BOOM! I'll filter to just those books in the genre(s) you are interested in

## Resources

* Streamlit
* Pandas
* Goodreads API
* Fuzzywuzzy