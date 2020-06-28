def init_app(app):
    """Inicializador de extensões"""

    @app.route("/")
    def index():
        return render_template('home.html')