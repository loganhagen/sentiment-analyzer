"""docstring"""

from flask_restx import Namespace, Resource

api = Namespace("articles", description="Article related operations")

class ArticleList(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """
    def get(self):
        """Get a list of articles"""

    def post(self):
        """Create a new article"""

class Article(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """
    def get(self, article_id):
        """Get an article by ID"""

    def put(self, article_id):
        """Update an article by ID"""

    def delete(self, article_id):
        """Delete an article by ID"""

api.add_resource(ArticleList, "")
api.add_resource(Article, "/<int:article_id>")