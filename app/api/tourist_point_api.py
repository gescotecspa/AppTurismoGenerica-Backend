from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
<<<<<<< HEAD
from app.services import tourist_point_service
=======
from app.services.tourist_point_service import TouristPointService
from app.auth.auth import token_required
>>>>>>> develop

tourist_point_api_blueprint = Blueprint('tourist_point_api', __name__)
api = Api(tourist_point_api_blueprint)

class TouristPointResource(Resource):
<<<<<<< HEAD
    def get(self, id):
        tourist_point = tourist_point_service.get_tourist_point_by_id(id)
=======
    @token_required
    def get(self, current_user, id):
        tourist_point = TouristPointService.get_tourist_point_by_id(id)
>>>>>>> develop
        if tourist_point:
            return tourist_point  # El objeto ya está serializado
        return {'message': 'Tourist point not found'}, 404

<<<<<<< HEAD
    def put(self, id):
=======
    @token_required
    def put(self, current_user, id):
>>>>>>> develop
        data = request.get_json()
        # Extraer datos de las imágenes si existen
        # images = data.pop('images', [])
        # for image in images:
        #     image['data'] = image.get('data')
        #     image['filename'] = image.get('filename')

<<<<<<< HEAD
        updated_tourist_point = tourist_point_service.update_tourist_point(id, data)
=======
        updated_tourist_point = TouristPointService.update_tourist_point(id, data)
>>>>>>> develop
        if updated_tourist_point:
            return updated_tourist_point  # El objeto ya está serializado
        return {'message': 'Tourist point not found'}, 404
    
<<<<<<< HEAD
    def delete(self, id):
        """Realiza un borrado lógico del punto turístico"""
        deleted_tourist_point = tourist_point_service.delete_tourist_point(id)
=======
    @token_required
    def delete(self, current_user, id):
        """Realiza un borrado lógico del punto turístico"""
        deleted_tourist_point = TouristPointService.delete_tourist_point(id)
>>>>>>> develop
        if deleted_tourist_point:
            return {'message': 'Tourist point deleted (logical delete)'}, 200
        return {'message': 'Tourist point not found'}, 404

class TouristPointListResource(Resource):
<<<<<<< HEAD
    def get(self):
        tourist_points = tourist_point_service.get_all_tourist_points()
        return tourist_points

    def post(self):
=======
    @token_required
    def get(self, current_user):
        tourist_points = TouristPointService.get_all_tourist_points()
        return tourist_points

    @token_required
    def post(self, current_user):
>>>>>>> develop
        data = request.get_json()
        # Extraer datos de las imágenes si existen
        # images = data.pop('images', [])
        # for image in images:
        #     image['data'] = image.get('data')
        #     image['filename'] = image.get('filename')
        
<<<<<<< HEAD
        tourist_point = tourist_point_service.create_tourist_point(data)
        return tourist_point.serialize(), 201  

class ImageResource(Resource):
    def post(self, id):
        data = request.get_json()
        # Manejo de la imagen usando ImageManager
        image = tourist_point_service.add_image(id, data['image'])
        return image, 201 

class RatingResource(Resource):
    
    def get(self, id):
        """
        Obtener todas las valoraciones de un punto turístico específico.
        """
        ratings = tourist_point_service.get_ratings_by_tourist_point(id)
        if not ratings:
            return {'message': 'No ratings found for this tourist point.'}, 404
        return jsonify([rating.serialize() for rating in ratings])
    
    def post(self, id):
        data = request.get_json()
        rating = tourist_point_service.add_rating(id, data['tourist_id'], data['rating'], data.get('comment'))
        return rating

class RatingDetailResource(Resource):
    def delete(self, rating_id):
        success = tourist_point_service.delete_rating(rating_id)
=======
        tourist_point = TouristPointService.create_tourist_point(data)
        return tourist_point.serialize(), 201  

class ImageResource(Resource):
    @token_required
    def post(self, current_user, id):
        data = request.get_json()
        # Manejo de la imagen usando ImageManager
        image = TouristPointService.add_image(id, data['image'])
        return image, 201 

class RatingResource(Resource):
    @token_required
    def get(self, current_user, id):
        """
        Obtener todas las valoraciones de un punto turístico específico.
        """
        ratings = TouristPointService.get_ratings_by_tourist_point(id)
        if not ratings:
            return {'message': 'No ratings found for this tourist point.'}, 404
        return jsonify([rating.serialize() for rating in ratings])

    @token_required 
    def post(self, current_user, id):
        data = request.get_json()
        rating = TouristPointService.add_rating(id, data['tourist_id'], data['rating'], data.get('comment'))
        return rating

class RatingVersionedResource(Resource):
    @token_required
    def get(self, current_user, id, version):
        """
        Obtener todas las valoraciones de un punto turístico específico.
        """
        if version == 'v2':
            ratings = TouristPointService.get_ratings_by_tourist_point(id)
            if not ratings:
                response = {
                            'ratings': [],
                            'average_rating': 0
                            }
                return response, 200
            
            average_rating = TouristPointService.get_average_rating(id)
            
            response = {
            'ratings': [rating.serialize() for rating in ratings],
            'average_rating': average_rating['average_rating']
            }
            return response, 200
        else:
            return {'message': 'API version not supported'}, 400

class AllTouristPointListResource(Resource):
    @token_required
    def get(self, current_user):
        """
        Obtener todos los puntos turísticos excepto aquellos con estado 'deleted'.
        """
        tourist_points = TouristPointService.get_all_except_deleted()
        return tourist_points, 200
    
class RatingDetailResource(Resource):
    @token_required
    def delete(self, current_user, rating_id):
        success = TouristPointService.delete_rating(rating_id)
>>>>>>> develop
        if success is None:
            return {'message': 'Rating not found'}, 404
        return {'message': 'Rating deleted successfully'}, 200  # Mensaje de confirmación

<<<<<<< HEAD
    def put(self, rating_id):
        data = request.get_json()
        rating = tourist_point_service.update_rating(rating_id, data)
=======
    @token_required
    def put(self, current_user, rating_id):
        data = request.get_json()
        rating = TouristPointService.update_rating(rating_id, data)
>>>>>>> develop
        if rating is None:
            return {'message': 'Rating not found'}, 404
        return rating

class AverageRatingResource(Resource):
<<<<<<< HEAD
    def get(self, id):
        avg_rating = tourist_point_service.get_average_rating(id)
        return avg_rating, 200

class ImageDeleteResource(Resource):
    def post(self, id):
=======
    @token_required
    def get(self, current_user, id):
        avg_rating = TouristPointService.get_average_rating(id)
        return avg_rating, 200

class ImageDeleteResource(Resource):
    @token_required
    def post(self, current_user, id):
>>>>>>> develop
        data = request.get_json()
        image_ids = data.get('image_ids', [])
        
        if not image_ids:
            return {'message': 'No image IDs provided'}, 400

<<<<<<< HEAD
        success = tourist_point_service.delete_images(image_ids)
=======
        success = TouristPointService.delete_tourist_point_images(image_ids)
>>>>>>> develop
        
        if success:
            return {'message': 'Images deleted successfully'}, 200
        else:
            return {'message': 'Failed to delete images'}, 500
        
<<<<<<< HEAD
=======
class TouristPointCommentsLastWeekResource(Resource):
    def get(self):
        """
        Obtiene los comentarios de los puntos turísticos de la última semana.
        """
        ratings = TouristPointService.get_comments_last_4_weeks()
        return ratings, 200
    
class TouristPointRatingApprovalResource(Resource):
    def put(self, rating_id):
        updated_rating, error = TouristPointService.approve_rating(rating_id)
        if updated_rating:
            return updated_rating.serialize(), 200
        return {'message': error}, 404    
    
class TouristRatingRejectResource(Resource):
    def put(self, rating_id):
        rejected_rating = TouristPointService.reject_rating(rating_id)
        if rejected_rating:
            return rejected_rating.serialize(), 200
        return {'message': 'Rating not found or already approved'}, 404  
          
>>>>>>> develop
api.add_resource(TouristPointResource, '/tourist_points/<int:id>')
api.add_resource(TouristPointListResource, '/tourist_points')
api.add_resource(ImageResource, '/tourist_points/<int:id>/images')
api.add_resource(RatingResource, '/tourist_points/<int:id>/ratings')
api.add_resource(RatingDetailResource, '/ratings/<int:rating_id>')
api.add_resource(AverageRatingResource, '/tourist_points/<int:id>/average_rating')
<<<<<<< HEAD
api.add_resource(ImageDeleteResource, '/tourist_points/<int:id>/images/delete')
=======
api.add_resource(ImageDeleteResource, '/tourist_points/<int:id>/images/delete')
api.add_resource(AllTouristPointListResource, '/tourist_points/active-inactive')
api.add_resource(RatingVersionedResource, '/<string:version>/tourist_points/<int:id>/ratings')
api.add_resource(TouristPointCommentsLastWeekResource, '/tourist_points/ratings/last_week')
api.add_resource(TouristPointRatingApprovalResource, '/tourist_points/ratings/approve/<int:rating_id>')
api.add_resource(TouristRatingRejectResource, '/tourist_points/ratings/reject/<int:rating_id>')
>>>>>>> develop
