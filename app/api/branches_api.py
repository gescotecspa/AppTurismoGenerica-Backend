<<<<<<< HEAD
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.branch_service import BranchService
=======
from flask import Blueprint, abort, request, jsonify
from flask_restful import Api, Resource
from app.services.branch_service import BranchService
from app.auth.auth import token_required
>>>>>>> develop

branch_api_blueprint = Blueprint('branch_api', __name__)
api = Api(branch_api_blueprint)

class BranchResource(Resource):
<<<<<<< HEAD
    def get(self, branch_id):
=======
    @token_required
    def get(self, current_user, branch_id):
>>>>>>> develop
        branch = BranchService.get_branch_by_id(branch_id)
        if branch:
            return jsonify(branch.serialize())
        return {'message': 'Branch not found'}, 404
<<<<<<< HEAD

    def put(self, branch_id):
=======
    
    @token_required
    def put(self, current_user, branch_id):
>>>>>>> develop
        data = request.get_json()
        # Extraer datos de la imagen si existen
        image_data = data.pop('image_data', None)

        branch = BranchService.update_branch(branch_id, **data, image_data=image_data)
        if branch:
            return jsonify(branch.serialize())
        return {'message': 'Branch not found'}, 404

<<<<<<< HEAD
    def delete(self, branch_id):
=======
    @token_required
    def delete(self, current_user, branch_id):
>>>>>>> develop
        if BranchService.delete_branch(branch_id):
            return {'message': 'Branch deleted'}, 200
        return {'message': 'Branch not found'}, 404

class BranchListResource(Resource):
<<<<<<< HEAD
    def get(self):
        branches = BranchService.get_all_branches()
        return jsonify([branch.serialize() for branch in branches])

    def post(self):
=======
    @token_required
    def get(self, current_user):
        branches = BranchService.get_all_branches()
        return jsonify([branch.serialize() for branch in branches])
    
    @token_required
    def post(self, current_user):
>>>>>>> develop
        data = request.get_json()
        # Extraer datos de la imagen si existen
        image_data = data.pop('image_data', None)

        branch = BranchService.create_branch(**data, image_data=image_data)
        return jsonify(branch.serialize())
<<<<<<< HEAD
class PartnerBranchesResource(Resource):
    def get(self, partner_id):
        branches = BranchService.get_branches_by_partner_id(partner_id)
=======

class PartnerBranchesResource(Resource):
    @token_required
    def get(self, current_user, partnerId):
        # if isinstance(current_user, dict):
        #     # Verifica si es un invitado
        #     if current_user.get("is_guest"):
        #         print("Es invitado primer ingreso?", current_user.get("is_guest"))
        #         return {"message": "Acceso denegado: solo usuarios registrados pueden acceder a esta ruta."}, 403
        # else:
        #     # Verifica si el usuario registrado es un invitado
        #     if hasattr(current_user, "is_guest") and current_user.is_guest:
        #         print("Es invitado segundo?", current_user.is_guest)
        #         return {"message": "Acceso denegado: solo usuarios registrados pueden acceder a esta ruta."}, 403

        branches = BranchService.get_branches_by_partner_id(partnerId)
>>>>>>> develop
        if branches:
            return jsonify([branch.serialize() for branch in branches])
        return branches, 200
    
api.add_resource(BranchResource, '/branches/<int:branch_id>')
api.add_resource(BranchListResource, '/branches')
<<<<<<< HEAD
api.add_resource(PartnerBranchesResource, '/partners/<int:partner_id>/branches')
=======
api.add_resource(PartnerBranchesResource, '/partners/<int:partnerId>/branches')
>>>>>>> develop
