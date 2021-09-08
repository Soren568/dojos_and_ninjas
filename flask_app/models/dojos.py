from flask_app.models.ninjas import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos

# ! ===================================  STUDY  ==========================================
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s "
        result= connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)
        dojo = cls(result[0])
        dojo.ninjas = []
        for ninja in result:
            ninja_data = {
                **ninja,
                "id": ninja["ninjas.id"],
                "created_at": ninja["ninjas.created_at"],
                "updated_at": ninja['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo
# ! ===================================  STUDY  ==========================================

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)
        return result

    def ninja_count():
        pass
