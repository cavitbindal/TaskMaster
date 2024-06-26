from flask import Flask
from taskmaster.routes import configure_routes
from taskmaster.db import DB, Todo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def main():
    with app.app_context():
        # instantiate db
        db_instance = DB(app)

        # configure endpoints
        configure_routes(app, db_instance)

        db_instance.db.create_all()
        
        
        
        app.run(debug=True)

if __name__ == "__main__":
    main()
   