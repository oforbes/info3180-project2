from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:project2@localhost/projectdb"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://qvufzfhjnrzrne:PWKGvd6x1FghXkr90I4MXo3kUG@ec2-54-225-112-119.compute-1.amazonaws.com:5432/d4fgu381smcp9t"


app.config['SQLALCHEMY_DATABASE_URI']="postgres://jafjvfoqyvkcvh:f2abecd9ce49271e14852830cd622274d963366ce08fcda4a4ffcaaa401af06c@ec2-23-23-222-147.compute-1.amazonaws.com:5432/d3ifkrashmfqee"
HEROKU_POSTGRESQL_BLUE_URL='postgres://mxjglmlbwltozv:d4c7a5a519cde8e5ec0f6234e8906ed0a4aa43fa691868177e91b0bbb03ccc98@ec2-54-225-71-119.compute-1.amazonaws.com:5432/d5ucjg4u4dcpt'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)
db.create_all()

from app import views,models