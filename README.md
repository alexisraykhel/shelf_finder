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

* Provide your goodreads library export csv,
downloadable from your account
[here](https://www.goodreads.com/review/import).
* I'll get the top shelves for each book (this takes
  1 second per book, thanks to API rate limiting)
* You then select which shelf/shelves you are
interested in
* BOOM! All the books on those shelves!!

## Resources

* Streamlit
* Pandas
* Goodreads API
* Fuzzywuzzy