from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
db = "dojo_survey_schema"
class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.dojo = data['dojo']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into dojo_survey_schema.surveys (name,dojo,language,comment) VALUES (%(name)s,%(dojo)s,%(language)s,%(comment)s);"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojo_survey_schema.surveys ORDER BY id DESC LIMIT 1; "
        results = connectToMySQL(db).query_db(query)
        return cls(results[0])
    

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['dojo']) < 1:
            is_valid = False
            flash("Must choose a dojo.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(survey['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid