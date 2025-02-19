from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.branch_rating_service import BranchRatingService
<<<<<<< HEAD
=======
from app.auth.auth import token_required
>>>>>>> develop

branch_rating_api_blueprint = Blueprint('branch_rating_api', __name__)
api = Api(branch_rating_api_blueprint)

class BranchRatingResource(Resource):
<<<<<<< HEAD
    def post(self, branch_id):
=======
    @token_required
    def post(self, current_user, branchId):
>>>>>>> develop
        data = request.get_json()
        user_id = data.get('user_id')
        rating = data.get('rating')
        comment = data.get('comment')

        if not user_id or not rating:
            return {'message': 'user_id and rating are required'}, 400

<<<<<<< HEAD
        rating = BranchRatingService.create_rating(branch_id, user_id, rating, comment)
=======
        rating = BranchRatingService.create_rating(branchId, user_id, rating, comment)
>>>>>>> develop
        if rating:
            return rating.serialize(), 201
        return {'message': 'Rating already exists for this branch and user'}, 400

class BranchRatingUpdateResource(Resource):
<<<<<<< HEAD
    def put(self, rating_id):
=======
    @token_required
    def put(self, current_user, rating_id):
>>>>>>> develop
        data = request.get_json()
        rating = data.get('rating')
        comment = data.get('comment')

        if rating is None:
            return {'message': 'Rating is required'}, 400

        updated_rating = BranchRatingService.update_rating(rating_id, rating, comment)
        if updated_rating:
            return updated_rating.serialize(), 200
        return {'message': 'Rating not found'}, 404

<<<<<<< HEAD
    def delete(self, rating_id):
=======
    def delete(self, current_user, rating_id):
>>>>>>> develop
        deleted_rating = BranchRatingService.delete_rating(rating_id)
        if deleted_rating:
            return {'message': 'Rating deleted'}, 200
        return {'message': 'Rating not found'}, 404
<<<<<<< HEAD

class BranchRatingsListResource(Resource):
    def get(self, branch_id):
        ratings_with_names = BranchRatingService.get_all_ratings_for_branch(branch_id)
        if not ratings_with_names:
            return {'message': 'No ratings found for this branch'}, 404

        avg_rating = BranchRatingService.get_average_rating_for_branch(branch_id)
=======
    
class BranchRatingSoftDeleteResource(Resource):
    @token_required
    def delete(self, current_user, rating_id):
        deleted_rating = BranchRatingService.soft_delete_rating(rating_id)
        if deleted_rating:
            return {'message': 'Rating logically deleted'}, 200
        return {'message': 'Rating not found'}, 404
    
class BranchRatingApproveResource(Resource):
    @token_required
    def put(self, current_user, rating_id):
        # Llama al servicio para aprobar la valoración
        approved_rating = BranchRatingService.approve_rating(rating_id)
        if approved_rating:
            return approved_rating.serialize(), 200
        return {'message': 'Rating not found or already approved'}, 404

class BranchRatingRejectResource(Resource):
    def put(self, rating_id):
        # Llama al servicio para aprobar la valoración
        rejected_rating = BranchRatingService.reject_rating(rating_id)
        if rejected_rating:
            return rejected_rating.serialize(), 200
        return {'message': 'Rating not found or already approved'}, 404    
 

class BranchRatingsListResource(Resource):

    @token_required
    def get(self, current_user, branchId):
        ratings_with_names = BranchRatingService.get_all_ratings_for_branch(branchId)

        if not ratings_with_names:
            response = {
            'ratings': ratings_with_names,
            'average_rating': 0
        }
            return response, 200

        avg_rating = BranchRatingService.get_average_rating_for_branch(branchId)
>>>>>>> develop
        
        response = {
            'ratings': [rating.serialize(first_name) for rating, first_name in ratings_with_names],
            'average_rating': avg_rating
        }
        return response, 200

<<<<<<< HEAD
class BranchAverageRatingResource(Resource):
    def get(self, branch_id):
        avg_rating = BranchRatingService.get_average_rating_for_branch(branch_id)
        return jsonify({'average_rating': avg_rating}), 200

api.add_resource(BranchRatingResource, '/branches/<int:branch_id>/ratings')
api.add_resource(BranchRatingUpdateResource, '/branches/ratings/<int:rating_id>')
api.add_resource(BranchRatingsListResource, '/branches/<int:branch_id>/ratings/all')
api.add_resource(BranchAverageRatingResource, '/branches/<int:branch_id>/average_rating')

=======
class BranchRatingsListAdminResource(Resource):
    def get(self, branch_id):
        ratings_with_names = BranchRatingService.get_all_ratings_for_branch_include_rejected(branch_id)
        print(ratings_with_names)
        if not ratings_with_names:
            response = {
            'ratings': ratings_with_names,
            'average_rating': 0
        }
            return response, 200

        avg_rating = BranchRatingService.get_average_rating_for_branch(branch_id)
        response = {
            'ratings': [rating.serialize(first_name) for rating, first_name in ratings_with_names],
            'average_rating': avg_rating
        }
        return response, 200
    

class BranchAverageRatingResource(Resource):
    @token_required
    def get(self, current_user, branchId):
        avg_rating = BranchRatingService.get_average_rating_for_branch(branchId)
        return jsonify({'average_rating': avg_rating}), 200
    
class BranchRatingsLast4WeeksResource(Resource):
    def get(self):
        """
        Obtiene las valoraciones de una sucursal de las últimas 4 semanas.
        """
        ratings = BranchRatingService.get_ratings_last_4_weeks()
        if not ratings:
            return {'message': 'No ratings found for this branch in the last 4 weeks'}, 404
        
        return ratings, 200

api.add_resource(BranchRatingResource, '/branches/<int:branchId>/ratings')
api.add_resource(BranchRatingUpdateResource, '/branches/ratings/<int:rating_id>')
api.add_resource(BranchRatingsListResource, '/branches/<int:branchId>/ratings/all')
api.add_resource(BranchRatingsListAdminResource, '/branches/admin/<int:branch_id>/ratings/all')
api.add_resource(BranchAverageRatingResource, '/branches/<int:branchId>/average_rating')
api.add_resource(BranchRatingSoftDeleteResource, '/branches/ratings/soft_delete/<int:rating_id>')
api.add_resource(BranchRatingApproveResource, '/branches/ratings/approve/<int:rating_id>')
api.add_resource(BranchRatingRejectResource, '/branches/ratings/reject/<int:rating_id>')
api.add_resource(BranchRatingsLast4WeeksResource, '/branches/ratings/last_4_weeks')
>>>>>>> develop
