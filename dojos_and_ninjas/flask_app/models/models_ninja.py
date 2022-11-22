from flask_app import app
from flask_app.models.models_dojo import Dojo
from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas_schema'

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.dojo = []

    @classmethod
    def create_ninja(cls, data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age)
                VALUES ( %(first_name)s, %(last_name)s, %(age)s )
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def all_ninjas_dojo(cls, data):
        query = """
                SELECT * FROM ninjas
                LEFT JOIN dojos
                ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        ninjas = []
        for ninja in results:
            ninja_dojo = cls(ninja)
            dojo_data = {
                'id' : ninja['dojos.id'],
                'first_name' : ninja['first_name'],
                'last_name' : ninja['last_name'],
                'age' : ninja['age'],
                'created_at' : ninja['dojos.created_at'],
                'updated_at' : ninja['dojos.updated_at']
            }
            ninja_dojo.dojo = Dojo(dojo_data)
            ninjas.append(ninja_dojo)
        return ninjas

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM ninjas
                WHERE id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, form_data):
        query = """
                UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
                WHERE id = %(id)s
                """
        return connectToMySQL(db).query_db(query, form_data)

    @classmethod
    def destroy(cls, data):
        query = """
                DELETE FROM ninjas
                WHERE id = %(id)s
                """
        return connectToMySQL(db).query_db(query, data)