from flask import Flask, render_template, request, redirect, url_for
import sys
import os

# Import SweetShop from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sweetshop import SweetShop

app = Flask(__name__)
shop = SweetShop()

@app.route('/')
def index():
    name = request.args.get('name')
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    sort_by = request.args.get('sort_by')

    if name or category or min_price is not None or max_price is not None:
        sweets = shop.search_sweets(name, category, min_price, max_price)
    elif sort_by:
        sweets = [{"id": id, **data} for id, data in shop.sort_sweets(sort_by).items()]
    else:
        sweets = shop.view_all_sweets()

    return render_template('index.html', sweets=sweets)

@app.route('/add', methods=['POST'])
def add():
    id = int(request.form['id'])
    name = request.form['name']
    category = request.form['category']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    shop.add_sweet(id, name, category, price, quantity)
    return redirect(url_for('index'))

@app.route('/delete/<int:sweet_id>')
def delete(sweet_id):
    shop.delete_sweet(sweet_id)
    return redirect(url_for('index'))

@app.route('/purchase/<int:sweet_id>', methods=['POST'])
def purchase(sweet_id):
    qty = int(request.form['purchase_qty'])
    try:
        shop.purchase_sweet(sweet_id, qty)
    except ValueError:
        pass  # Optionally flash a message
    return redirect(url_for('index'))

@app.route('/restock/<int:sweet_id>', methods=['POST'])
def restock(sweet_id):
    qty = int(request.form['restock_qty'])
    shop.restock_sweet(sweet_id, qty)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
