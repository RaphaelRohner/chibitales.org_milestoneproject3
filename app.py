import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'chibitales'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_game')
def get_game():
    return render_template("game.html")


@app.route('/get_find')
def get_find():
    return render_template("find.html")


@app.route('/get_play')
def get_play():
    return render_template("play.html")


@app.route('/get_setup')
def get_setup():
    return render_template("setup.html")


@app.route('/get_trade')
def get_trade():
    return render_template("trade.html")


@app.route('/get_items')
def get_items():
    return render_template("items.html", items=mongo.db.items.find())


@app.route('/get_loot')
def get_loot():
    return render_template("loot.html", loot=mongo.db.loot.find())    


@app.route('/delete_loot/<loot_id>')
def delete_loot(loot_id):
    mongo.db.loot.remove({'_id': ObjectId(loot_id)})
    return redirect(url_for('get_loot'))


@app.route('/get_source')
def get_source():
    return render_template("source.html", source=mongo.db.sources.find())


@app.route('/get_category')
def get_category():
    return render_template("category.html", category=mongo.db.category.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
