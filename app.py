import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# IMPORT ENVIRONMENT VARIABLES
if os.path.exists("env.py"):
    import env

# CALL FLASK AND DEFINE MONGODB
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'chibitales'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# GENERAL ROUTE TO OPEN WEBSITE AND ROUTE TO OPEN GAME.HTML
@app.route('/')
@app.route('/get_game')
def get_game():
    return render_template("game.html")


# OPEN FIND.HTML
@app.route('/get_find')
def get_find():
    return render_template("find.html")


# OPEN PLAY.HTML
@app.route('/get_play')
def get_play():
    return render_template("play.html")


# OPEN SETUP.HTML
@app.route('/get_setup')
def get_setup():
    return render_template("setup.html")


# OPEN TRADE.HTML
@app.route('/get_trade')
def get_trade():
    return render_template("trade.html")


# ROUTE FOR ITEMS OVERVIEW
@app.route('/get_items')
def get_items():
    return render_template("items.html", items=mongo.db.items.find())


# OPEN LOOT.HTML - OVERVIEW PAGE
@app.route('/get_loot')
def get_loot():
    return render_template("loot.html", loot=mongo.db.loot.find())


# OPEN LOOT_ADD.HTML PAGE
@app.route('/add_loot')
def add_loot():
    return render_template('loot_add.html')


# INSERT NEW LOOT NAME TO MONGODB AND RETURN TO OVERVIEW
@app.route('/insert_loot', methods=['POST'])
def insert_loot():
    loot_doc = {'loot_name': request.form.get('loot_name')}
    mongo.db.loot.insert_one(loot_doc)
    return redirect(url_for('get_loot'))


# OPEN LOOT_EDIT.HTML PAGE WITH SELECTED DATASET VALUE TO EDIT
@app.route('/edit_loot/<loot_id>')
def edit_loot(loot_id):
    return render_template('loot_edit.html',
                           loot=mongo.db.loot.find_one(
                           {'_id': ObjectId(loot_id)}))


# UPDATE MONGODB DATASET LOOT_NAME WITH NEW VALUE AFTER EDIT
@app.route('/update_loot/<loot_id>', methods=['POST'])
def update_loot(loot_id):
    mongo.db.loot.update(
        {'_id': ObjectId(loot_id)},
        {'loot_name': request.form.get('loot_name')})
    return redirect(url_for('get_loot'))


# DELETE A LOOT NAME FROM MONGODB AND RELOAD LOOT.HTML
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
