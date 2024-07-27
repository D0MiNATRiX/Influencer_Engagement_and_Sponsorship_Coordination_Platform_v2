from flask_restful import Resource, Api, reqparse
from .models import db, Campaign

api = Api(prefix='/api')

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name should be a string')
parser.add_argument('description', type=str, help='Description should be a string')
parser.add_argument('start_date', type=str, help='Start Date should be a string')
parser.add_argument('end_date', type=str, help='End Date should be a string')
parser.add_argument('budget', type=int, help='Budget should be a integer')
parser.add_argument('visibility', type=str, help='Visibilty should be a string')
parser.add_argument('goals', type=str, help='Goals should be a string')
class Campaign(Resource):
    def get(self):
        return {"message": "Hello from API"}
    def post(self):
        args = parser.parse_args()
        campaign = Campaign(**args)
        db.session.add(campaign)
        db.session.commit()
    
api.add_resource(Campaign, '/campaign')