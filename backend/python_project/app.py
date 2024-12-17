from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from api.routes.category_router import category_router
from api.utils.spec import spec
from api.config.database import init_app, db
from api.config.db_initializer import initialize_database

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
    init_app(app)
    app.register_blueprint(category_router)
    
    spec.register(app)
    
    with app.app_context():
        base = initialize_database(db)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=5000)
