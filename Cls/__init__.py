from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)

def create_app():
    app.debug=True
    app.secret_key='zxcpoifgh777'
    
    #create DB data file
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Cls.sqlite'
    
    db.init_app(app)

    bootstrap = Bootstrap(app)

    from . import views
    app.register_blueprint(views.bp)

    #from . import admin     # after seeding the data, close the function
    #app.register_blueprint(admin.bp)
    
    return app

#when I have time, try to create a "underconstruction page by adding route"