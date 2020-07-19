def init_app(app):
    @app.before_first_request
    def init_everything():
        print("Isto roda sempre que iniciar a app")
