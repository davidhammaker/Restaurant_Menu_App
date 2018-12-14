from restaurant_menu_app import create_app, db


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
