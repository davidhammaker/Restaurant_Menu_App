# Restaurant Menu App

This application accompanies the Udacity 'Iterative Development' Lesson. The application is a Flask web-app featuring a list of restaurants and menus. A user may select any restaurant from the list to view the menu. Each item on the menu includes a price, course, and description.

## Dependencies

Until this app can be deployed (if ever), the dependencies are very involved. Nevertheless, if you would like to see this app work, follow these steps carefully to run the app locally on your own machine.

You will need access to a shell terminal (I am using [GitBash](https://git-scm.com/downloads) for Windows). You will also need to install the latest version of [Python 3](https://www.python.org/downloads/), which must be Python 3.6 or later. This app is incompatible with Python 2 and Python 3.5 or older.

Clone this repository and create a Python [virtual environment](https://docs.python.org/3/library/venv.html). Inside your shell terminal, activate the virtual environment and install Flask, Flask-WTF (for forms), Flask-SQLAlchemy (for databases), Flask-Login (for login sessions), Flask-Dance (for 3rd party OAuth providers), and Blinker (for signals associated with Flask-Dance):

```
$ pip install flask
$ pip install flask-wtf
$ pip install flask-sqlalchemy
$ pip install flask-login
$ pip install flask-dance
$ pip install blinker
```

You will be required to set up a few environment variables. If you would like to learn how to set up environment variables, Corey Schafer has brief videos that explain the process for [Windows](https://www.youtube.com/watch?v=IolxqkL7cD8) and [Mac and Linux](https://www.youtube.com/watch?v=5iWhQWVXosU). (Note: I was only successful when I followed the "Mac and Linux" tutorial using GitBash for Windows.) The first two environment variables must be named "RESTAURANT_SECRET_KEY" and "RESTAURANT_DB", and their values are as follows:
* Obtain a value for "RESTAURANT_SECRET_KEY" by opening a Python REPL and entering the following:
```
>>> import secrets
>>> secrets.token_hex(16)
```
The result should be a long string of characters. Set your environment variable to this result.

* The value you choose for "RESTAURANT_DB" is somewhat arbitrary. Just make sure you prefix your value with something like `sqlite:///`, and add the `.db` file extension. For example, `sqlite:///example.db` would work well.

For the remaining environment variables, you must create an OAuth App in GitHub. You may create an app [here](https://github.com/settings/applications/new). Set "Homepage URL" to "http://localhost:5000", and "Authorization callback URL" to "http://localhost:5000/login/github/authorized". The other fields maybe filled in however you want. Register your app and find values for "Client ID" and "Client Secret". Create environment variables with these values, named "GH_CLIENT_ID" and "GH_CLIENT_SECRET" respectively.

* If setting the environment variables is unsuccessful, you may insert the values directly into your code for demonstration purposes only. Note that this is an insecure means of incorporating these values in your code.

## Running the App

When you have acquired/installed all the dependencies, you can run the app from the shell terminal. Once again, ensure that your virtual environment is active. If you are running your app for the first time, run the following:

```
$ export OAUTHLIB_INSECURE_TRANSPORT=1
$ python run.py --setup
```

* The first of these commands sets an environment variable that permits your app to work without HTTPS, which is not recommended for development. However, HTTP (not HTTPS) is required for running the app locally, so this environment variable must be set _every time you open your terminal_ before you run the app. The variable only needs to be set again if you close and reopen your terminal.
* The second command initializes your database.

If you see no errors, open an internet browser and navigate to `localhost:5000`. The app should be running at that address.

You should only need to run `$ python run.py --setup` one time. After that, the databases will be initialized, and you may run the app with the following:

```
$ python run.py
```

Remember to set OAUTHLIB_INSECURE_TRANSPORT each time you close and reopen your terminal.

The app uses GitHub as an OAuth2 provider. You will be able to use your GitHub account to log into the app.
