from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints
    from app.api.v1.system import system_bp
    from app.api.v1.device import device_bp
    from app.api.v1.auth import auth_bp
    
    app.register_blueprint(system_bp, url_prefix='/api/v1/system')
    app.register_blueprint(device_bp, url_prefix='/api/v1/device')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    
    return app
