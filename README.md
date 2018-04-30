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

# Flask Guide
http://flask.pocoo.org/docs/0.12/quickstart/

## Current Goal
-Have the returned array display, rotating the images, on resultloop.html
