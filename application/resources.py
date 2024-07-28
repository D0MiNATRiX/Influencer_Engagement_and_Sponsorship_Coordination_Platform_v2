from flask_restful import Resource, Api, reqparse, marshal_with, fields
from .models import db, Campaign

api = Api(prefix='/api')

campaign_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'start_date': fields.String,
    'end_date': fields.String,
    'budget': fields.Integer,
    'visibility': fields.String,
    'goals': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name is required and should be a string', required=True)
parser.add_argument('description', type=str, help='Description is required and should be a string', required=True)
parser.add_argument('start_date', type=str, help='Start Date is required and should be a string', required=True)
parser.add_argument('end_date', type=str, help='End Date is required and should be a string', required=True)
parser.add_argument('budget', type=int, help='Budget is required and should be a integer', required=True)
parser.add_argument('visibility', type=str, help='Visibilty is required and should be a string', required=True)
parser.add_argument('goals', type=str, help='Goals is required and should be a string', required=True)

class Campaigns(Resource):
    @marshal_with(campaign_fields)
    def get(self):
        all_campaigns = Campaign.query.all()
        return all_campaigns
    
    def post(self):
        args = parser.parse_args()
        campaign = Campaign(**args)
        db.session.add(campaign)
        db.session.commit()
        return {"message": "Campaign Created"}
    
api.add_resource(Campaigns, '/campaign')