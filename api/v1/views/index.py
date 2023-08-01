#!/usr/bin/python

"""
Create a route / status on the object app_views
Return a JSON: "status": "OK"
"""


from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """jsonify status response"""
    return jsonify({"status": "OK"})
