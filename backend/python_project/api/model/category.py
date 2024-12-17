from sqlalchemy import Column, Integer, String, Boolean
from api.config.database import db

class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_type  = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    icon = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"<Categorie(id={self.id}, category_type={self.category_type}, title={self.title}, icon={self.icon}, active={self.active})>"

    def to_dict(self):
        return {
            "id": self.id,
            "category_type": self.category_type,
            "title": self.title,
            "icon": self.icon,
            "active": self.active
        }