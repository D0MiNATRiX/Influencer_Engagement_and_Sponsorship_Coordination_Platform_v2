from main import app
from application.models import db,Role

with app.app_context():
    db.create_all()
    admin = Role(id='admin', name='Admin', description='Admin Description')
    db.session.add(admin)
    sponsor = Role(id='sponsor', name='Sponsor', description='Sponsor Description')
    db.session.add(sponsor)
    influencer = Role(id='influencer', name='Influencer', description='Influencer Description')
    db.session.add(influencer)
    try:
        db.session.commit()
    except:
        pass