import uuid
from modules.main import MainModule


class Hero(object):

    _collection_name = 'Hero'

     #O método init é sempre chamado após uma instanciação da classe
    def __init__(self, **args):
        # Aqui vamos já deixar os campos
        self.id = args.get('id', uuid.uuid4().hex)
        self.name = args.get('name')
        self.description = args.get('description')
        self.universe = args.get('universe')
        self.imageUrl = args.get('imageUrl')

    def save(self):
        """Save hero"""
        MainModule.get_firestore_db().collection(
            self._collection_name).document(self.id).set(self.to_dict())

    def to_dict(self):
        """Transform hero in dict format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'universe': self.universe,
            'imageUrl': self.imageUrl
        }

    @classmethod
    def get_hero(cls, hero_id):
        """Get hero"""
        hero = MainModule.get_firestore_db().collection(
            cls._collection_name).document(hero_id).get()
        if hero.exists:
            return Hero(**hero.to_dict())
        return None

    @classmethod
    def get_heroes(cls, cursor = None):
        """Get heroes"""
        # Logo de inicio vamos deixar a consulta pronta com o order_by
        query = MainModule.get_firestore_db().collection(
            cls._collection_name).order_by('id').limit(16)

        # Se tiver o cursor vamos atualizar a consulta com o start_after
        if cursor:
            query = query.start_after({
                'id': cursor
            })
        # No final realizamos a consulta e retornamos ela
        return query.stream()

    @classmethod
    def delete(cls, hero_id):
        """Delete a hero by id"""
        hero = MainModule.get_firestore_db().collection(
            cls._collection_name).document(hero_id).delete()

    @classmethod
    def get_top_heroes(cls):
        """Get top heroes"""
        return MainModule.get_firestore_db().collection(
            cls._collection_name).limit(20).stream()

    @classmethod
    def get_search_hero(cls,hero_name):
        heroes= MainModule.get_firestore_db().collection(
              cls._collection_name).where('name', '==',hero_name).limit(10).stream()

        if hero_name:
            return heroes
        return None


