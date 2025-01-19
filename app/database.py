from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server import app

# Initialize the database
db = SQLAlchemy(app)

migrate = Migrate(app, db)