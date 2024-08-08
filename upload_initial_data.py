from main import app, datastore
from application.models import db, Role
from flask_security import hash_password

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="admin", description="User is an admin")
    datastore.find_or_create_role(name="sponsor", description="User is a sponsor")
    datastore.find_or_create_role(name="influencer", description="User is an influencer")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com", password=hash_password("admin"), roles=["admin"])
    if not datastore.find_user(email="sponsor1@email.com"):
        datastore.create_user(email="sponsor1@email.com", password=hash_password("sponsor1"), roles=["sponsor"], active=False)
    if not datastore.find_user(email="influencer1@email.com"):
        datastore.create_user(email="influencer1@email.com", password=hash_password("influencer1"), roles=["influencer"])
    db.session.commit()