# Restaurant Menu App

This application accompanies the Udacity 'Iterative Development' Lesson. The application is a Flask web-app featuring a list of restaurants and menus. A user may select any restaurant from the list to view the menu. Each item on the menu includes a price, course, and description.

## Dependencies

You will need access to a shell terminal (I am using [GitBash](https://git-scm.com/downloads) for Windows). You will also need to install the latest version of [Python 3](https://www.python.org/downloads/), which must be Python 3.6 or later. This app is incompatible with Python 2 and Python 3.5 or older.

Clone this repository and create a Python [virtual environment](https://docs.python.org/3/library/venv.html). Inside your shell terminal, activate the virtual environment and install Flask, Flask-WTF (for forms), and Flask-SQLAlchemy (for databases):

```
$ pip install flask
$ pip install flask-wtf
$ pip install flask-sqlalchemy
```

Additionally, you will need to download the database and add it to the `restaurant_menu_app` package directory. The database may be obtained [here](https://github.com/davidhammaker/Restaurant_Database_Server/raw/master/restaurantmenu.db).

## Running the App

When you have acquired/installed all the dependencies, you can run the app from the shell terminal. Once again, ensure that your virtual environment is active, then run the following:

`$ python run.py`

If you see no errors, open an internet browser and navigate to `localhost:5000`. The app should be running at that address.

## Future features:

* Adding new restaurants
* Editing existing restaurants
* Deleting restaurants
* Adding new menu items
* Editing existing menu items
* Deleting menu items
