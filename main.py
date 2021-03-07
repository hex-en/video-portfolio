from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="kac_wissuwa_industries™")


@app.route('/projects')
def projects():
    return render_template('projects.html',
                           page_title="kac_wissuwa_industries™")


@app.route('/contact')
def contact():
    return render_template('contact.html',
                           page_title="kac_wissuwa_industries™")


if __name__ == "__main__":
    app.run(debug=True)
