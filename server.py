from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit_form', methods=['POST'])
def submit_form():
    session['fullName'] = request.form['fullName']
    session['dojoLocation'] = request.form['dojoLocation']
    session['favoriteLanguage'] = request.form['favoriteLanguage']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

# Create a destination Route to send the POST-ed Data


@app.route('/result')
def result():
    return render_template("result.html")

# Transfer the data using Session to the display route so it isn't lost between pages!


if __name__ == "__main__":   # Ensure this file is bxeing run directly and not from a different module
    # runs on a different port if 5000 is taken
    app.run(debug=True, host="localhost", port=8000)
