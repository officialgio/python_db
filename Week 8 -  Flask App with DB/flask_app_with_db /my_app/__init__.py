from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)
app.app_context().push()

from my_app.catalog.routes import catalog
app.register_blueprint(catalog)

db.create_all()
