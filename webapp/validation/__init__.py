def create_module(app, **kwargs):
    from .controllers import validation_bp
    app.register_blueprint(validation_bp)
    