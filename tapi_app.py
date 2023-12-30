from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
import json

app = Flask(__name__, template_folder='templates', static_folder='static')


samples_path = os.path.join(os.path.dirname(__file__), 'samples')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    
    user_enc_file = os.path.join(samples_path, f"{username}.enc")

    if os.path.exists(user_enc_file):
        
        pytosh2_path = os.path.join(samples_path, 'pytosh2.py')
        result = subprocess.run(['python3', pytosh2_path], capture_output=True, text=True, cwd=samples_path)

        if "Encrypted password is:" in result.stdout:
            return redirect(url_for('index', output=result.stdout))
        else:
            return "Access Denied"
    else:
        return "User not found"

@app.route('/index')
def index():
    output = request.args.get('output', '')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)