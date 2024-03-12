from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission for both home and results
@app.route('/results', methods=['POST'])
def handle_form():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']
        matched_strings = re.findall(regex_pattern, test_string)
        return render_template('index.html', matched_strings=matched_strings)

# Route to validate email ID
@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.json['email']
    # Regular expression for email validation
    regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid = bool(re.match(regex_pattern, email))
    return jsonify({'is_valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)
