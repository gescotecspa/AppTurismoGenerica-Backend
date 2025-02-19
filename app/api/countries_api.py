from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from app.services.country_city_service import CountryCityService
from app.models import City

countries_api_blueprint = Blueprint('countries_api', __name__)
api = Api(countries_api_blueprint)

class CountryListResource(Resource):
    def get(self):
        countries = CountryCityService.get_all_countries()
        return jsonify([country.serialize() for country in countries])

class CityListByCountryResource(Resource):
    def get(self, country_id):
        cities = City.query.filter_by(country_id=country_id).all()
        if not cities:
            return jsonify({"error": "No cities found for this country"}), 404
        return jsonify([{
            "id": c.id,
            "name": c.name,
            "latitude": c.latitude,
            "longitude": c.longitude
        } for c in cities])

# Agregar las rutas
api.add_resource(CountryListResource, '/countries')
api.add_resource(CityListByCountryResource, '/countries/<int:country_id>/cities')
