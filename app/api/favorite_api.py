from flask import Blueprint, request, jsonify
<<<<<<< HEAD
from flask_restful import Api, Resource
from app.services.favorite_service import FavoriteService
=======
from flask_restful import Resource, Api
from ..services.favorite_service import FavoriteService
from ..auth.auth import token_required  # Asegúrate de importar el decorador
>>>>>>> develop

favorite_api_blueprint = Blueprint('favorite_api', __name__)
api = Api(favorite_api_blueprint)

class FavoriteResource(Resource):
<<<<<<< HEAD
    def post(self):
=======
    @token_required
    def post(self, current_user):
>>>>>>> develop
        data = request.get_json()
        favorite = FavoriteService.add_favorite(data['user_id'], data['promotion_id'])
        if favorite is None:
            return jsonify({'message': 'Favorite already exists'})
        return jsonify(favorite.serialize())

<<<<<<< HEAD
    def delete(self):
=======

    @token_required
    def delete(self, current_user):
>>>>>>> develop
        data = request.get_json()
        success = FavoriteService.remove_favorite(data['user_id'], data['promotion_id'])
        if success:
            return jsonify({'message': 'Favorite removed'})
        return jsonify({'message': 'Favorite not found'})

class TouristFavoritesResource(Resource):
<<<<<<< HEAD
    def get(self, user_id):
=======
    @token_required
    def get(self, current_user, user_id):
>>>>>>> develop
        favorites = FavoriteService.get_favorites_by_tourist(user_id)
        return jsonify([fav.serialize() for fav in favorites])

class PromotionFavoritesResource(Resource):
<<<<<<< HEAD
    def get(self, promotion_id):
=======
    @token_required
    def get(self, current_user, promotion_id):
>>>>>>> develop
        favorites = FavoriteService.get_favorites_by_promotion(promotion_id)
        return jsonify([fav.serialize() for fav in favorites])

api.add_resource(FavoriteResource, '/favorites')
api.add_resource(TouristFavoritesResource, '/users/<int:user_id>/favorites')
api.add_resource(PromotionFavoritesResource, '/promotions/<int:promotion_id>/favorites')