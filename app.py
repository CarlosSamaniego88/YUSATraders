from flask import Flask, render_template
from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = 'development key'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ =='__main__':
    app.run(debug=True)
