from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define a simple model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Define the RESTful API resource.
class ItemResource(Resource):
    def get(self, item_id):
        item = Item.query.get(item_id)
        if item:
            return {'id': item.id, 'name': item.name}
        return {'message': 'Item not found'}, 404

    def put(self, item_id):
        data = request.get_json()
        item = Item.query.get(item_id)
        if item:
            item.name = data['name']
            db.session.commit()
            return {'message': 'Item updated successfully'}
        return {'message': 'Item not found'}, 404

    def delete(self, item_id):
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return {'message': 'Item deleted successfully'}
        return {'message': 'Item not found'}, 404

