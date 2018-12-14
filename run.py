import sys
from restaurant_menu_app import create_app, db


if __name__ == '__main__':
    app = create_app()
    if "--setup" in sys.argv:
        with app.app_context():
            db.create_all()
            db.session.commit()
    app.run(debug=True)
