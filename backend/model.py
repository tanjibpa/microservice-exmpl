from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# image links, stock amount, title and description

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.TEXT)
    stock_amount = db.Column(db.Integer)
    image_link = db.Column(db.String(200))
