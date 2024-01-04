from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
import subprocess
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'abcd1234efg789hijk456' #will be made dynamic later 

src_path = os.path.join(os.path.dirname(__file__), 'src')

def authentication_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'authenticated_user' not in session and request.endpoint not in ['home', 'login']:
            return redirect(url_for('home'))
        return route_function(*args, **kwargs)
    return wrapper

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user_enc_file = os.path.join(src_path, f"{username}.enc")

    if os.path.exists(user_enc_file):
        pytosh2_path = os.path.join(src_path, 'tapi_encry_decry.py')
        input_param3 = 'Encrypt'
        
        result = subprocess.run(['python3', pytosh2_path, username, password, input_param3], capture_output=True, text=True, cwd=src_path)

        print("Terminal Output:", result.stdout)

        encrypted_password_index = result.stdout.find("Encrypted password is: ")
        if encrypted_password_index != -1:
            expected_password = result.stdout[encrypted_password_index + len("Encrypted password is: "):].strip()

            if password == expected_password:
                session['authenticated_user'] = True
                return redirect(url_for('index'))
            else:
                return "Access Denied"
        else:
            return "Unexpected output from pytosh2.py"
    else:
        return "User not found"

@app.route('/index')
@authentication_required
def index():
    if request.method != 'GET':
        return redirect(url_for('home'))
    output = request.args.get('output', '')
    return render_template('index.html', output=output)

@app.route('/about')
@authentication_required
def about():
    return render_template('about.html')

@app.route('/reference/<item>')
@authentication_required
def reference(item):
    if request.method != 'GET':
        return redirect(url_for('home'))
    return render_template('reference_template.html', item=item)
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('authenticated_user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
