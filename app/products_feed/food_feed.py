import json
import os
import sys

from utils.get_product_image import get_product_image

# Get the root directory of the project
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Add the project's root directory to the system path
sys.path.append(project_root)

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.product import Product

max_product_count = 30000
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'openfoodfacts-products.jsonl')


def add_product_to_db(product: dict):
    db: Session = SessionLocal()

    required_fields = ['product_name', 'nutriments']
    required_nutriments = ['fat_value', 'energy-kcal', 'carbohydrates', 'proteins_value']
    all_fields_present = all(field in product for field in required_fields)

    if not all_fields_present:
        return

    all_nutriments_present = all(field in product['nutriments'] for field in required_nutriments)

    if not all_nutriments_present:
        return

    new_product = Product(name=product['product_name'], total_fat=product['nutriments']['fat_value'],
                          calories=product['nutriments']['energy-kcal'],
                          protein=product['nutriments']['proteins_value'],
                          image_url=get_product_image(product),
                          total_carbohydrates=product['nutriments']['carbohydrates'])

    db.add(new_product)
    db.commit()


def run_feed():
    index = 0
    with open(file_path, 'r') as file, open('example.json', 'w') as example_file:
        for line in file:
            data = json.loads(line)
            add_product_to_db(data)
            if index == max_product_count:
                break
            index += 1


run_feed()
