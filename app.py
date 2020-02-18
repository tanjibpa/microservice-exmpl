import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate

from backend import read_csv, db, Product

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jarvis:password@localhost:5432/micro"
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + '/files'

db.init_app(app)

migrate = Migrate(app, db)

@app.route('/', methods=['POST', 'GET'])
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash("File not found")
    csv_file = request.files['file']
    csv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename))
    res = read_csv(os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename))
    if not res:
        flash("Unsuccessful")
    else:
        flash(res)
    return redirect(url_for('index'))

if __name__ == "__main__":
    # read_csv('demo.csv')
    app.run(debug=True)