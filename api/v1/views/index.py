#!/usr/bin/python

"""
# v1/views/index.py
"""


from flask import jsonify
from . import app_views


# Create a route / status on the object app_views
# Return a JSON: "status": "OK"
@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
