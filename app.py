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


# OPEN ITEMS.HTML - OVERVIEW PAGE
@app.route('/get_items')
def get_items():
    return render_template("items.html", items=mongo.db.items.find().sort([("item_name", 1), ("item_source", 1), ("item_unit", 1)]),
                            floot=mongo.db.loot.find().sort("loot_name", 1),
                            fcategory=mongo.db.category.find().sort("name_category", 1),
                            fsource=mongo.db.sources.find().sort("source_name", 1))


# FILTER ITEMS.HTML - OVERVIEW PAGE
@app.route('/filter_items/<filter_name>')
def filter_items(filter_name):
    the_items = mongo.db.items.find({"item_name": ObjectId(filter_name)})
    return render_template("items.html", items=mongo.db.items.find().sort([("item_name", 1), ("item_source", 1), ("item_unit", 1)]),
                            floot=mongo.db.loot.find().sort("loot_name", 1),
                            fcategory=mongo.db.category.find().sort("name_category", 1),
                            fsource=mongo.db.sources.find().sort("source_name", 1))


# OPEN ITEMS_ADD.HTML PAGE
@app.route('/add_items')
def add_items():
    return render_template('items_add.html',
                           loot=mongo.db.loot.find().sort("loot_name", 1),
                           category=mongo.db.category.find().sort("name_category", 1),
                           source=mongo.db.sources.find().sort("source_name", 1))


# INSERT NEW ITEM TO MONGODB AND RETURN TO ITEMS OVERVIEW
@app.route('/insert_item', methods=['POST'])
def insert_item():
    item = mongo.db.items
    item.insert_one(request.form.to_dict())
    return redirect(url_for('get_items'))


# OPEN ITEMS_EDIT.HTML PAGE WITH SELECTED DATASET VALUE TO EDIT
@app.route('/edit_item/<item_id>')
def edit_item(item_id):
    the_item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    all_names = mongo.db.loot.find().sort("loot_name", 1)
    all_sources = mongo.db.sources.find().sort("source_name", 1)
    all_categories = mongo.db.category.find().sort("name_category", 1)
    return render_template('items_edit.html', 
                            item=the_item,
                            names=all_names,
                            sources=all_sources,
                            categories=all_categories,)


# UPDATE MONGODB COLLECTION ITEMS WITH NEW VALUES AFTER EDIT
@app.route('/update_item/<item_id>', methods=["POST"])
def update_item(item_id):
    items = mongo.db.items
    items.update({'_id': ObjectId(item_id)},
        {
        'item_name': request.form.get('item_name'),
        'item_category': request.form.get('item_category'),
        'item_source': request.form.get('item_source'),
        'item_chance': request.form.get('item_chance'),
        'item_unit': request.form.get('item_unit'),
        'item_price': request.form.get('item_price'),
        'item_time': request.form.get('item_time'),
        })
    return redirect(url_for('get_items'))


# DELETE AN ITEM FROM MONGODB AND RELOAD ITEMS.HTML
@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    mongo.db.items.remove({'_id': ObjectId(item_id)})
    return redirect(url_for('get_items'))


# OPEN LOOT.HTML - OVERVIEW PAGE
@app.route('/get_loot')
def get_loot():
    return render_template("loot.html", loot=mongo.db.loot.find().sort("loot_name", 1))


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


# OPEN SOURCE.HTML - OVERVIEW PAGE
@app.route('/get_source')
def get_source():
    return render_template("source.html", source=mongo.db.sources.find().sort("source_name", 1))


# OPEN SOURCE_ADD.HTML PAGE
@app.route('/add_source')
def add_source():
    return render_template('source_add.html')


# INSERT NEW SOURCE NAME TO MONGODB AND RETURN TO OVERVIEW
@app.route('/insert_source', methods=['POST'])
def insert_source():
    source_doc = {'source_name': request.form.get('source_name')}
    mongo.db.sources.insert_one(source_doc)
    return redirect(url_for('get_source'))


# OPEN SOURCE_EDIT.HTML PAGE WITH SELECTED DATASET VALUE TO EDIT
@app.route('/edit_source/<source_id>')
def edit_source(source_id):
    return render_template('source_edit.html',
                           source=mongo.db.sources.find_one(
                           {'_id': ObjectId(source_id)}))


# UPDATE MONGODB DATASET SOURCE_NAME WITH NEW VALUE AFTER EDIT
@app.route('/update_source/<source_id>', methods=['POST'])
def update_source(source_id):
    mongo.db.sources.update(
        {'_id': ObjectId(source_id)},
        {'source_name': request.form.get('source_name')})
    return redirect(url_for('get_source'))


# DELETE A SOURCE NAME FROM MONGODB AND RELOAD SOURCE.HTML
@app.route('/delete_source/<source_id>')
def delete_source(source_id):
    mongo.db.sources.remove({'_id': ObjectId(source_id)})
    return redirect(url_for('get_source'))


# OPEN CATEGORY.HTML - OVERVIEW PAGE
@app.route('/get_category')
def get_category():
    return render_template("category.html", category=mongo.db.category.find().sort("name_category", 1))


# OPEN CATEGORY_ADD.HTML PAGE
@app.route('/add_category')
def add_category():
    return render_template('category_add.html')


# INSERT NEW CATEGORY NAME TO MONGODB AND RETURN TO OVERVIEW
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'name_category': request.form.get('name_category')}
    mongo.db.category.insert_one(category_doc)
    return redirect(url_for('get_category'))


# OPEN CATEGORY_EDIT.HTML PAGE WITH SELECTED DATASET VALUE TO EDIT
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('category_edit.html',
                           category=mongo.db.category.find_one(
                           {'_id': ObjectId(category_id)}))


# UPDATE MONGODB DATASET name_category WITH NEW VALUE AFTER EDIT
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.category.update(
        {'_id': ObjectId(category_id)},
        {'name_category': request.form.get('name_category')})
    return redirect(url_for('get_category'))


# DELETE A CATEGORY NAME FROM MONGODB AND RELOAD CATEGORY.HTML
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.category.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_category'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
