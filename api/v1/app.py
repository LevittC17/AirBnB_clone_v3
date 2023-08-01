#!/usr/bin/python3

"""
Register a blueprint on a Flask Instance
Returning status of the API
"""


from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)


# Register the blueprint app_views => Flask Instace app
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Handling app.teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors: return a JSON-formatted status code response"""
    return jsonify({'error': 'Not Found'}), 404


if __name__ == "__main__":
    # Get host and port from env variable
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask Server
    app.run(host=host, port=port, threaded=True)
