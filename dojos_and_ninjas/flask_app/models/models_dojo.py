from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas_schema'

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_dojo(cls, data):
        query = """
                INSERT INTO dojos (name)
                VALUES ( %(name)s )
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s
                """
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])
