from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:project2@localhost/projectdb"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://qvufzfhjnrzrne:PWKGvd6x1FghXkr90I4MXo3kUG@ec2-54-225-112-119.compute-1.amazonaws.com:5432/d4fgu381smcp9t"#app.config['HEROKU_POSTGRESQL_GRAY_URI']='postgres://ezgipufwujalnq:0a3af93bea5af0d695d9661686027753a5a3e03b6003142286da7535b4c12c29@ec2-50-19-95-47.compute-1.amazonaws.com:5432/d2o24nir14h00k'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)
db.create_all()

from app import views,models

