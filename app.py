from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os  # Add this import for secret key generation

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/rrtables.db?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
    'connect_args': {'timeout': 30}  # Increase timeout
}
# Generate a secure secret key (or use a fixed one in production)
app.config['SECRET_KEY'] = os.urandom(24).hex()  # Generates a random 24-byte key
# Alternatively for development, you can use a fixed string:
# app.config['SECRET_KEY'] = "your-secret-key-here-make-it-long-and-random"

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()  # This will NOT delete existing data


@app.route('/')
def home():
    return "Welcome to R&R Time Clock System"

if __name__ == "__main__":
    app.run(debug=True)