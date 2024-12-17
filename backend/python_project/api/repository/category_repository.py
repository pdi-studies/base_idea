import os
from api.model.category import Category
from api.config.database import db

class CategoryRepository:
                    
    def get_all_active_categories(self):
        with db.session.begin():
            result = (
                db.session.query(Category)
                .filter(Category.active == True)  
                .all()
            )
            return result
    