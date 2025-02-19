from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.tourist_rating_service import TouristRatingService
<<<<<<< HEAD
=======
from app.models.status import Status
from app.auth.auth import token_required
>>>>>>> develop

tourist_rating_api_blueprint = Blueprint('tourist_rating_api', __name__)
api = Api(tourist_rating_api_blueprint)

class TouristRatingResource(Resource):
<<<<<<< HEAD
    def post(self, tourist_id):
=======
    @token_required
    def post(self, current_user, tourist_id):
>>>>>>> develop
        data = request.get_json()  # Obtiene los datos del cuerpo de la solicitud
        if not data:
            return jsonify({'message': 'No data provided'}), 400

        branch_id = data.get('branch_id')
        rating = data.get('rating')
        comment = data.get('comment')

        if branch_id is None or rating is None:
            return jsonify({'message': 'Missing branch_id or rating'}), 400

<<<<<<< HEAD
=======
        # Asignar status "pending" por defecto
        status_pending = Status.query.filter_by(name="pending").first()

>>>>>>> develop
        new_rating, error_message = TouristRatingService.create_rating(
            tourist_id,
            branch_id,
            rating,
<<<<<<< HEAD
            comment
=======
            comment,
            status_pending.id
>>>>>>> develop
        )
        if new_rating:
            return new_rating.serialize(), 201
        return {'message': error_message}, 409
    
class TouristRatingUpdateResource(Resource):
<<<<<<< HEAD
    def put(self, rating_id):
        data = request.get_json()
        rating = TouristRatingService.update_rating(
            rating_id,
            data['rating'],
            data.get('comment')
        )
        if rating:
            return rating.serialize(), 200
        return {'message': 'Rating not found'}, 404

    def delete(self, rating_id):
=======
    @token_required
    def put(self, current_user, rating_id):
            data = request.get_json()
            
            # Obtener los datos de la valoración a actualizar
            rating_value = data.get('rating')
            comment = data.get('comment')
            status_id = data.get('status_id')

            updated_rating = TouristRatingService.update_rating(
                rating_id,
                rating_value,
                comment,
                status_id 
            )
            
            if updated_rating:
                return updated_rating.serialize(), 200
            return {'message': 'Rating not found'}, 404

    def delete(self, current_user, rating_id):
>>>>>>> develop
        rating = TouristRatingService.delete_rating(rating_id)
        if rating:
            return rating.serialize(), 200
        return {'message': 'Rating not found'}, 404

class TouristRatingsListResource(Resource):
<<<<<<< HEAD
    def get(self, tourist_id):
=======
    @token_required
    def get(self, current_user, tourist_id):
>>>>>>> develop
        ratings = TouristRatingService.get_all_ratings_for_tourist(tourist_id)
        average_rating = TouristRatingService.get_average_rating_for_tourist(tourist_id)
        
        ratings_list = [rating.serialize() for rating in ratings]
        
        return {
            'ratings': ratings_list,
            'average_rating': average_rating
        }, 200

class TouristAverageRatingResource(Resource):
<<<<<<< HEAD
    def get(self, tourist_id):
        avg_rating = TouristRatingService.get_average_rating_for_tourist(tourist_id)
        return jsonify({'average_rating': avg_rating}), 200
=======
    @token_required
    def get(self, current_user, tourist_id):
        avg_rating = TouristRatingService.get_average_rating_for_tourist(tourist_id)
        return jsonify({'average_rating': avg_rating}), 200
    
class TouristRatingApprovalResource(Resource):
    @token_required
    def put(self, current_user, rating_id):
        updated_rating, error = TouristRatingService.approve_rating(rating_id)
        if updated_rating:
            return updated_rating.serialize(), 200
        return {'message': error}, 404  
    
class TouristRatingRejectResource(Resource):
    def put(self, rating_id):
        # Llama al servicio para aprobar la valoración
        rejected_rating = TouristRatingService.reject_rating(rating_id)
        if rejected_rating:
            return rejected_rating.serialize(), 200
        return {'message': 'Rating not found or already approved'}, 404     
    
class TouristRatingsLast4WeeksResource(Resource):
    def get(self):
        ratings = TouristRatingService.get_ratings_last_4_weeks()
        if not ratings:
            return {'message': 'No ratings found'}, 404
        return ratings, 200    
>>>>>>> develop

api.add_resource(TouristRatingResource, '/tourists/<int:tourist_id>/ratings')
api.add_resource(TouristRatingUpdateResource, '/tourists/ratings/<int:rating_id>')
api.add_resource(TouristRatingsListResource, '/tourists/<int:tourist_id>/ratings/all')
api.add_resource(TouristAverageRatingResource, '/tourists/<int:tourist_id>/average_rating')
<<<<<<< HEAD
=======
api.add_resource(TouristRatingApprovalResource, '/tourists/ratings/approve/<int:rating_id>')
api.add_resource(TouristRatingsLast4WeeksResource, '/tourists/ratings/last-4-weeks')
api.add_resource(TouristRatingRejectResource, '/tourists/ratings/reject/<int:rating_id>')
>>>>>>> develop
