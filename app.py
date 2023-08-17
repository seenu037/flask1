from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_database.db'  # SQLite URI

db = SQLAlchemy(app)

class LocalTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return "Connected to local database table"

if __name__ == '__main__':
    app.run(debug=True)
