def create_module(app, **kwargs):
    
    from .controllers import app_bp
    app.register_blueprint(app_bp)
