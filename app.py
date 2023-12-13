# app.py
from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()

@app.route('/')
def index():
    return render_template('testing.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    nmap_result = run_command(f"nmap {target}")
    nikto_result = run_command(f"nikto -h {target}")

    # Redirect to the home page with a thank-you message
    return render_template('testing.html', thanks=True)
def submit():
    if request.method == 'POST':
        # Access form data using request.form['input_name']
        # Perform your Python logic here
        return 'Python code executed successfully'
if __name__ == "__main__":
    app.run(debug=True)
