from dotenv import load_dotenv
from os import environ

from flask import Flask


# Load environment variables from .env
load_dotenv()

# Create the flask instance
app = Flask(__name__)

# Set up the secret key for in-app encryption
app.config['SECRET_KEY'] = environ.get('APP_SECRET_KEY')

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = f'{environ.get('DB_DBMS')}://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}'

# Defining Login Manager
import login_manager

# Defining Routes
import routes

# Running the server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)