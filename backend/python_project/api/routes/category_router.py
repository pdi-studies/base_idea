from flask import Blueprint, Response
from api.repository.category_repository import CategoryRepository
from api.utils.logger import logger
import json

category_router = Blueprint('category', __name__)

@category_router.route('/api/categories', methods=['GET'])
def get_cagetories():
    try:
        category_repo = CategoryRepository()
        categories = category_repo.get_all_active_categories()
        json_return = [category.to_dict() for category in categories]
    
    except Exception as exception:
        logger.error(exception)
        return {'message': 'Verifique os logs!', 'status': 'erro'}, 500

    return Response(
        json.dumps(json_return),
        mimetype='application/json',
        status=200
    )
