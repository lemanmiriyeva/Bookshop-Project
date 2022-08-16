from pickle import TRUE
from flask import Flask

app = Flask(__name__, template_folder='template',static_folder='assets')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/products_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config["SECRET_KEY"] = "Products"
from extensions import *
from models import *
from controllers import *
if __name__=='__main__':
    app.run(port=5000,debug=True)