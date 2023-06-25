from flask import Flask, render_template, request,jsonify,redirect,url_for
from models import db, Vehicle, Route
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        vehicles = Vehicle.query.all()
        return render_template('index.html', vehicles=vehicles)
    elif request.method == 'POST':
        new_vehicle = Vehicle(**request.form)
        db.session.add(new_vehicle)
        db.session.commit()
        vehicles = Vehicle.query.all()  
        return render_template('index.html', vehicles=vehicles)

# @app.route('/vehicles/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
# def vehicle_by_id():
#   if request.method == 'GET':
    
#     render_template('single.html',id=id)
#   # if request.method == 'PATCH':
#   # if request.method == 'DELETE':
@app.route('/vehicles/<int:id>', methods=['GET', 'PATCH'])
def vehicle_by_id(id):
    if request.method == 'GET':

        vehicle = Vehicle.query.filter_by(id=id).first()
        routings = Route.query.filter_by(vehicle_id=id)
      
        if vehicle:
            return render_template('single.html', id=id, vehicle=vehicle, routings=routings)
        else:
            return "Vehicle not found"
          
@app.route('/delete<int:id>')
def delete_vehicle(id):
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return redirect(url_for('index'))
    
  

    

if __name__ == '__main__':
    app.run(port=5455)
