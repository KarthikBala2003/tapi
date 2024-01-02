from functools import wraps
from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

samples_path = os.path.join(os.path.dirname(__file__), 'samples')

print("Samples Path:", samples_path)


authenticated_user = False

def authentication_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        global authenticated_user
        if request.endpoint not in ['home', 'login'] and not authenticated_user:
            return redirect(url_for('home'))
        return route_function(*args, **kwargs)
    return wrapper

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    global authenticated_user

    username = request.form.get('username')
    password = request.form.get('password')

    user_enc_file = os.path.join(samples_path, f"{username}.enc")

    print("User Enc File:", user_enc_file)

    if os.path.exists(user_enc_file):
        pytosh2_path = os.path.join(samples_path, 'pytosh2.py')
        
        
        input_param3 = 'Encrypt'
        
        result = subprocess.run(['python', pytosh2_path, username, password, input_param3], capture_output=True, text=True, cwd=samples_path)

        print("Terminal Output:", result.stdout)

        encrypted_password_index = result.stdout.find("Encrypted password is: ")
        if encrypted_password_index != -1:
            expected_password = result.stdout[encrypted_password_index + len("Encrypted password is: "):].strip()

            if password == expected_password:
                authenticated_user = True
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
    output = request.args.get('output', '')
    return render_template('index.html', output=output)

@app.route('/about')
@authentication_required
def about():
    return render_template('about.html')

@app.route('/reference/<item>')
@authentication_required
def reference(item):
    return render_template('reference_template.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
