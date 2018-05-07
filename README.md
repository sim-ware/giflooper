# giflooper
A looper, for GIFs, for you.

# Git Etiquette, for Frank
To create a new branch
```
$ git checkout -b <feature_branch> master
```

# To Run
You must install the requirements!
```
$ pip install -r requirements.txt
```
```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ flask run
```

## The Concept
A search engine that uses the Giphy API to return a random loop of GIFs that fit the entered search terms.

## Techs
The server/application part will be in Python/Flask. The front-end will be done in React

# GIPHY API
https://developers.giphy.com/docs/

# GIFs to use
https://giphy.com/gifs/animated-colors-dwaeIbBnF6HBu
https://media.giphy.com/media/2FayWIH1xrdlT2wx2/giphy.gif

# Flask Guide
http://flask.pocoo.org/docs/0.12/quickstart/

## Current Goal
-Have the returned array display, rotating the images, on resultloop.html

## Feature Ideas
-Previous and Next Buttons
-Pause, display Modal that shows SearchTerms and GIF Link

## Stuff that took ages...
-Passing a List from Python to <script>tags in HTML Template using Jinja.
