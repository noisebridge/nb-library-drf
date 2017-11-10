# nb-library-drf

Noisebridge library Django REST Framework

We will be using SQLite as a database.

To start the server from scratch:

```
git clone git@github.com:nb-library-wg/nb-library-drf.git
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

###Email From Mek Karpeles - Jul 2017
Gio (bcc'd) forwarded me your message -- thanks for writing us!

- The Books and Search APIs ([https://openlibrary.org/developers/api](https://openlibrary.org/developers/api)) are most reliable.
- Any Open Library work or edition page can be turned into json by removing adding .json after it's ID
        e.g. [https://openlibrary.org/books/OL7910663M/Moo](https://openlibrary.org/books/OL7910663M/Moo) becomes
        [https://openlibrary.org/books/OL7910663M.json](https://openlibrary.org/books/OL7910663M.json)
- We have an availability API which is in progress
    There's a python openlibrary-client library ([https://github.com/internetarchive/openlibrary-client](https://github.com/internetarchive/openlibrary-client)) which is still early stages but de-mystifies / obviates a lot of our APIs

Questions for you:

- Which APIs are you hoping to be unified?
- And which APIs once worked that are no longer working for your use case?
