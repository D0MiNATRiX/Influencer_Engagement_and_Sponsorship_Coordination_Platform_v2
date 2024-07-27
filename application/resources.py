from flask_restful import Resource, Api, reqparse
from .models import db, Campaign

api = Api(prefix='/api')

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name is required and should be a string', required=True)
parser.add_argument('description', type=str, help='Description is required and should be a string', required=True)
parser.add_argument('start_date', type=str, help='Start Date is required and should be a string', required=True)
parser.add_argument('end_date', type=str, help='End Date is required and should be a string', required=True)
parser.add_argument('budget', type=int, help='Budget is required and should be a integer', required=True)
parser.add_argument('visibility', type=str, help='Visibilty is required and should be a string', required=True)
parser.add_argument('goals', type=str, help='Goals is required and should be a string', required=True)
class Campaigns(Resource):
    def get(self):
        return {"message": "Hello from API"}
    def post(self):
        args = parser.parse_args()
        campaign = Campaign(name=args.get("name"), description=args.get("description"), start_date=args.get("start_date"), end_date=args.get("end_date"), budget=args.get("budget"), visibility=args.get("visibility"), goals=args.get("goals"))
        db.session.add(campaign)
        db.session.commit()
        return {"message": "Campaign Created"}
    
api.add_resource(Campaigns, '/campaign')