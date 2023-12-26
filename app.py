import os
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Get the path to the JSON file within the 'data' folder
json_file_path = os.path.join(os.path.dirname(__file__), 'data', 'menu_data.json')

# Load the JSON data
with open(json_file_path) as f:
    menu_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', menu_data=menu_data)

@app.route('/menu_data')
def get_menu_data():
    return jsonify(menu_data)

if __name__ == '__main__':
    app.run(debug=True)