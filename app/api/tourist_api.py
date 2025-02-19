from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.tourist_service import TouristService
<<<<<<< HEAD
=======
from app.auth.auth import token_required
>>>>>>> develop

tourist_api_blueprint = Blueprint('tourist_api', __name__)
api = Api(tourist_api_blueprint)

class TouristResource(Resource):
<<<<<<< HEAD
    def get(self, user_id):
=======
    @token_required
    def get(self, current_user, user_id):
>>>>>>> develop
        tourist = TouristService.get_tourist_by_user_id(user_id)
        if tourist:
            return jsonify(tourist.serialize())
        return {'message': 'Tourist not found'}, 404

<<<<<<< HEAD
    def put(self, user_id):
=======
    @token_required
    def put(self, current_user, user_id):
>>>>>>> develop
        data = request.get_json()
        tourist = TouristService.update_tourist(user_id, **data)
        if tourist:
            return jsonify(tourist.serialize())
        return {'message': 'Tourist not found'}, 404

<<<<<<< HEAD
    def delete(self, user_id):
=======
    @token_required
    def delete(self, current_user, user_id):
>>>>>>> develop
        if TouristService.delete_tourist(user_id):
            return {'message': 'Tourist deleted'}, 200
        return {'message': 'Tourist not found'}, 404

class TouristListResource(Resource):
<<<<<<< HEAD
    def get(self):
        tourists = TouristService.get_all_tourists()
        return jsonify([tourist.serialize() for tourist in tourists])
        
=======
    @token_required
    def get(self, current_user):
        tourists = TouristService.get_all_tourists()
        return jsonify([tourist.serialize() for tourist in tourists])


>>>>>>> develop
    def post(self):
        data = request.get_json()
        tourist = TouristService.create_tourist(**data)
        return jsonify(tourist.serialize())

api.add_resource(TouristResource, '/tourists/<int:user_id>')
api.add_resource(TouristListResource, '/tourists')