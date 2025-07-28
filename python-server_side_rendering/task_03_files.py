from flask import Flask, render_template, request
import json
import csv



# Helper function

def read_json(filepath):
    with open(filepath) as f:
        return json.load(f)

def read_csv(filepath):
    products = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

#  Routes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def show_items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except Exception as e:
        print("Error loading items:", e)
        items_list = []

    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        error = "Wrong source"
        return render_template('product_display.html', products=[], error=error)

    if product_id:
        filtered = [p for p in products if p['id'] == product_id]
        if not filtered:
            error = "Product not found"
        products = filtered

    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
       app.run(debug=True, port=5000)

