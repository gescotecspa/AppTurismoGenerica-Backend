from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.funcionality_service import FunctionalityService
<<<<<<< HEAD
=======
from app.auth.auth import token_required 
>>>>>>> develop

functionality_api_blueprint = Blueprint('functionality_api', __name__)
api = Api(functionality_api_blueprint)

class FunctionalityResource(Resource):
<<<<<<< HEAD
    def get(self, functionality_id):
=======
    @token_required
    def get(self, functionality_id, current_user):
>>>>>>> develop
        functionality = FunctionalityService.get_functionality_by_id(functionality_id)
        if functionality:
            return jsonify(functionality.serialize())
        return {'message': 'Functionality not found'}, 404

<<<<<<< HEAD
    def put(self, functionality_id):
=======
    def put(self, functionality_id, current_user):
>>>>>>> develop
        data = request.get_json()
        functionality = FunctionalityService.update_functionality(functionality_id, **data)
        if functionality:
            return jsonify(functionality.serialize())
        return {'message': 'Functionality not found'}, 404

<<<<<<< HEAD
    def delete(self, functionality_id):
=======
    def delete(self, functionality_id, current_user):
>>>>>>> develop
        if FunctionalityService.delete_functionality(functionality_id):
            return {'message': 'Functionality deleted'}, 200
        return {'message': 'Functionality not found'}, 404


class FunctionalityListResource(Resource):
<<<<<<< HEAD
    def get(self):
        functionalities = FunctionalityService.get_all_functionalities()
        return jsonify([functionality.serialize() for functionality in functionalities])
        
    def post(self):
=======
    @token_required
    def get(self, current_user):
        functionalities = FunctionalityService.get_all_functionalities()
        return jsonify([functionality.serialize() for functionality in functionalities])
        
    def post(self, current_user):
>>>>>>> develop
        data = request.get_json()
        functionality = FunctionalityService.create_functionality(**data)
        return jsonify(functionality.serialize())

api.add_resource(FunctionalityResource, '/functionalities/<int:functionality_id>')
api.add_resource(FunctionalityListResource, '/functionalities')