from flask_restx import Namespace, Resource

api = Namespace("articles", description="Article related operations")

class ArticleList(Resource):
    def get(self):
        """Get a list of articles"""
        pass

    def post(self):
        """Create a new article"""
        pass

class Article(Resource):
    def get(self, article_id):
        """Get an article by ID"""
        pass

    def put(self, article_id):
        """Update an article by ID"""
        pass

    def delete(self, article_id):
        """Delete an article by ID"""
        pass

api.add_resource(ArticleList, "")
api.add_resource(Article, "/<int:article_id>")