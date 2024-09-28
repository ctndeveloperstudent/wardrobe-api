from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app instance
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/wardrobe_db'

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Wardrobe API connected to DB!"

if __name__ == '__main__':
    app.run(debug=True)
