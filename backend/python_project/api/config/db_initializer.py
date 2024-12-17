import csv
import os
from flask import current_app
from sqlalchemy import inspect
from api.config.database import db
from flask_sqlalchemy import SQLAlchemy
from api.model.category import Category
from api.utils.logger import logger

def initialize_database(db):
    logger.info("Initializing database...")

    with current_app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('categories'):
            logger.info("Creating tables...")
            db.create_all()

        with db.session.begin():
            if db.session.query(Category).count() == 0:
                logger.info("No categories found in the database. Importing CSV data...")
                import_csv_data(db)
            else:
                logger.info("Database already populated. Skipping CSV import.")
                
    return db

def import_csv_data(db):
    csv_file_categories = os.environ.get('CSV_FILE_CATEGORIES')
    if not csv_file_categories or not os.path.exists(csv_file_categories):
        logger.error(f"CSV file not found: {csv_file_categories}")
        return

    try:
        with open(csv_file_categories, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            categories = []
            for row in reader:
                active = row['active'].strip().lower() == 'true'

                category = Category(
                    category_type=row['category_type'],
                    title=row['title'],
                    icon=row['icon'],
                    active=active
                )
                categories.append(category)

            db.session.bulk_save_objects(categories)
            db.session.commit()
            logger.info(f"Imported {len(categories)} categories into the database.")
    except Exception as e:
        logger.error(f"Error importing CSV data: {e}")
