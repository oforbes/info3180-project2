from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:project2@localhost/projectdb"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ppbtfcrjasdzzf:c46ece106f6383251e05184dd6993b541f32098b49feea373767e8724905a249@ec2-54-225-182-108.compute-1.amazonaws.com:5432/d36pnsfrqlt0in'
app.config['HEROKU_POSTGRESQL_GRAY_URI']='postgres://ezgipufwujalnq:0a3af93bea5af0d695d9661686027753a5a3e03b6003142286da7535b4c12c29@ec2-50-19-95-47.compute-1.amazonaws.com:5432/d2o24nir14h00k'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)
db.create_all()

from app import views,models

