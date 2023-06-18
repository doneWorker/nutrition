import json
import os
import sys

# Get the root directory of the project
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Add the project's root directory to the system path
sys.path.append(project_root)

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.product import Product

max_product_count = 20_000
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'openfoodfacts-products.jsonl')


def add_product_to_db(product: dict):
    db: Session = SessionLocal()

    if 'product_name' not in product or 'product_name_en' not in product or 'nutriments' not in product:
        return

    if 'fat_value' not in product['nutriments'] or 'energy-kcal' not in product['nutriments'] or 'carbohydrates' not in \
            product['nutriments']:
        return

    new_product = Product(name=product['product_name'], total_fat=product['nutriments']['fat_value'],
                          calories=product['nutriments']['energy-kcal'],
                          total_carbohydrates=product['nutriments']['carbohydrates'])

    db.add(new_product)
    db.commit()


def run_feed():
    index = 0
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            add_product_to_db(data)
            if index == max_product_count:
                break
            index += 1


run_feed()
