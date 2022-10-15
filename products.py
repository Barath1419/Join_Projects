import config as server
from flask import jsonify , request

data_base = server.data_base_connection()

def index():
    return "Products Details"

def get_all_products():
    """
    get all products lists
    """
    cursor = data_base.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productdb.products")
    product_details = cursor.fetchall()
    cursor.close()
    return jsonify({'products':product_details})

def create_new_product():
    if request.method == "POST":
        new_product=request.json
        query="INSERT INTO products(ProductName, ProductPrice, ProductRating) VALUES ('%s','%s','%s')"
        query_val = (new_product["Name"] , 
                     new_product["Price"] , 
                     new_product["Rating"])
        cursor = data_base.cursor(dictionary=True)
        cursor.execute(query%query_val)
        data_base.commit()
        cursor.close()
        return jsonify({'new_product' : new_product})

def delete_product(id):
    cursor = data_base.cursor(dictionary=True)
    cursor.execute(f'delete from products where id={id}')
    data_base.commit()
    cursor.close()
    return ("Product deleted successfully")

def update_product(id):
    if request.method == 'PUT':
        updated_product = request.json
        cursor = data_base.cursor(dictionary=True)
        cursor.execute(f"update products set ProductName = '%s', ProductPrice = '%s', ProductRating = '%s' WHERE id ={id}" %(updated_product['Name'],updated_product['Price'],updated_product['Rating']))
        data_base.commit()
        cursor.close()
        return jsonify({'updated_product' : updated_product})

def get_Products(id):
    cursor = data_base.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM products WHERE id= {id}")
    single_product=cursor.fetchone()
    cursor.close()
    return jsonify({'product' : single_product})


