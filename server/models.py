from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    driver = db.Column(db.String(50))
    conductor = db.Column(db.String(50))
    routes = db.relationship('Route', backref='vehicle')
    
    def __repr__(self):
      return f"<Vehicle:{self.name}>"

class Route(db.Model):
    __tablename__ = 'route'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    def __repr__(self):
      return f"<Route:{self.name}>"
