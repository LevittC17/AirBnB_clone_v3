#!/usr/bin/python3

"""
New view of State objects
Handles all default RESTful API actions
"""


from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states(state_id):
    """Retrieve a State object"""
    state = storage.get(State, satte_id)
    if not state:
        abort(404)
        return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def delete_state(state_id):
    """Delete a state object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
        storage.delete(state)
        storage.save()
        return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Create a new State"""
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    if 'name' not in data:
        abort(400, description='Missing name')
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
