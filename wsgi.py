#!/usr/bin/env python3
"""
WSGI entry point for the JR Management App
"""
import os
import sys

# Add the project directory to the Python path
project_home = '/home/deploy/jrmanagement'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables if needed
os.environ.setdefault('FLASK_ENV', 'production')

# Import the Flask app
from auth import app

# This is what Gunicorn will use
application = app

if __name__ == "__main__":
    # This only runs when called directly, not through Gunicorn
    app.run(debug=False, host='0.0.0.0', port=5000)
