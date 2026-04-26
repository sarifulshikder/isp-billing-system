from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Register blueprints
    from app.routes import customer, billing, payment, dashboard
    app.register_blueprint(customer.bp)
    app.register_blueprint(billing.bp)
    app.register_blueprint(payment.bp)
    app.register_blueprint(dashboard.bp)
    
    return app