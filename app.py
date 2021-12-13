from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)


if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return render_template('index.html')
