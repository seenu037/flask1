from flask import Flask, render_template, jsonify

app = Flask(__name__)


# import sqlite3

# conn = sqlite3.connect('database.db')
# print("Connected to database successfully")

# conn.execute('CREATE TABLE parking (flat_name TEXT, availability TEXT)')
# print("Created table successfully!")

# conn.close()
import pandas as pd
df=pd.read_csv('sample.csv')
parking_data=df.to_dict(orient='records')
# Simulated parking data (replace with actual data from the database)
# parking_data = [
#     {'id': 1, 'status': 'available'},
#     {'id': 2, 'status': 'available'},
#     # ... more parking spaces
# ]

@app.route('/')
def index():
    return render_template('index.html', parking_data=parking_data)

@app.route('/get_parking_data')
def get_parking_data():
    return jsonify(parking_data)

if __name__ == '__main__':
    app.run(debug=True)
