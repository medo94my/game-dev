from flask import  Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


db = MongoClient(app.config['MONGODB_URI'])['game']
print(app.config['BASE_DIR'])
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error),404
from app.modules import routes
