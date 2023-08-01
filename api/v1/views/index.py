#!/usr/bin/python

"""
Create a route / status on the object app_views
Return a JSON: "status": "OK"
"""


from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """jsonify status response"""
    return jsonify({"status": "OK"})


def db_status():
    """Retrieve the number of each object type"""
    obj_types = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
    obj_count = {obj_type.lower(): storage.count(obj_type)
                 for obj_t in obj_type}
    return jsonify(obj_count)
