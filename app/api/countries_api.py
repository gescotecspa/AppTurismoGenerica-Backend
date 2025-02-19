from flask import Blueprint, jsonify
from flask_restful import Api, Resource
<<<<<<< HEAD
from app.services.country_service import CountryService
=======
from app.services.country_city_service import CountryCityService
>>>>>>> develop

countries_api_blueprint = Blueprint('countries_api', __name__)
api = Api(countries_api_blueprint)

class CountryListResource(Resource):
    def get(self):
<<<<<<< HEAD
        countries = CountryService.get_all_countries()
=======
        countries = CountryCityService.get_all_countries()
>>>>>>> develop
        return jsonify([country.serialize() for country in countries])

api.add_resource(CountryListResource, '/countries')
