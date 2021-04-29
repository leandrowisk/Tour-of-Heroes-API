from models.hero import Hero
import re

class HeroModule(object):
    """Hero module"""

    @staticmethod
    def create(params):
        """
        Create a new hero
        :param dict params: Request dict params
        :return Hero: Hero created
        """
        hero = Hero()
        hero.name = params['name']
        hero.description = params['description']
        hero.imageUrl = params['imageUrl']
        hero.universe = params['universe']
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        hero.save()
        return hero

    @staticmethod
    def update(hero,params):
        """ update a hero"""

        hero.name = params['name']
        hero.description = params['description']
        hero.imageUrl = params['imageUrl']
        hero.universe = params['universe']
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        hero.save()


    @staticmethod
    def valid_hero_params(hero):
        """Valid hero params"""
        if not hero.name:
            raise Exception('Bad request, name is required')

        if hero.universe!='marvel' and hero.universe!='dc':
            raise Exception('Bad request, invalid universe')


        pattern=re.compile('(https?://)?([\\da-z.-]+)\\.([a-z.]{2,6})[/\\w .-]*/?')

        if not pattern.match(hero.imageUrl):
           raise Exception('Bad request, invalid url')


    @staticmethod
    def format_hero_params(hero):
        """Format hero params"""
        hero.name = hero.name.title().strip()
        hero.description = hero.description.title().strip()