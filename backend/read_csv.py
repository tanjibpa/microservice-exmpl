import csv
import tempfile

from .model import db, Product

def read_csv(csv_file):
    print("CSV")
    with open(csv_file, newline='') as csvfile:
        product_csv = csv.DictReader(csvfile)
        for row in product_csv:
            # try:
                p = Product(
                    title=row['Title'],
                    description=row['Description'],
                    stock_amount=row['Amount'],
                    image_link=row['Image']
                )
                db.session.add(p)
            except Exception as e:
                return 0
    db.session.commit()
    return "Database updated successfully"