from flask_restful import Resource
from flask import request
from models.hero import Hero

class HeroesSearchHandler(Resource):

    def get(self):
        """Get search heroes"""

        try:
            heroes = Hero.get_search_hero(request.args.get('name').title())
            if heroes != '':
                response = {
                    'heroes': [],
                }

            for hero in heroes:
                response['heroes'].append(hero.to_dict())


            if heroes:
               return response['heroes']
            return {'message': 'Hero not found'}, 404

        except Exception as error:
                return {
                'message': 'Bad request, param name is required'
                        },400






