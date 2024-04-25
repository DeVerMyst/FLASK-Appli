# routes/routes.py 
from flask import render_template
from modules.create_session import create_db
from models.model_blog import ModelBlog

session = create_db()


def routes_setup(app):
    @app.route('/')
    def index():
        return "Hello ! hello pas hello"

    @app.route('/about')
    def about():
        return "Il fait beau et il n'y a pas trop de vent"

    @app.route('/template')
    def template():
        return render_template("toto.html")

    @app.route('/template/motif')
    def motif():
        return render_template("index.html")
    
    @app.route('/template/joli')
    def joli():
        return render_template("page2.html")    
    
    @app.route('/template/demain')
    def demain():
        
        # créer ou vérifier que la base de données existe
        req = session.query(ModelBlog).all()
        return render_template("page3.html", comments=req)
        
