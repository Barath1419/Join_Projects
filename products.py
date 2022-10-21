import config as server
from flask import jsonify , request
from main import app
from flask import render_template as home_page
from werkzeug.utils import secure_filename

data_base = server.data_base_connection()

def index():
    return "Products Details"

def get_all_products():
    """
    get all products lists
    takes 0 parameter
    return details of all products
    """
    cursor = data_base.cursor(dictionary=True)
    cursor.execute("SELECT id,productName,productPrice,productRating FROM productdb.products")
    product_details = cursor.fetchall()
    cursor.close()
    return jsonify({'products':product_details})


def create_new_product():
    '''
    Create a new product
    takes 0 argument
    return the details of the new product
    '''
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
    '''
    delete a single product from data base
    takes the product id as argument
    return a message for deletion of the product details
    '''
    cursor = data_base.cursor(dictionary=True)
    cursor.execute(f'delete from products where id={id}')
    data_base.commit()
    cursor.close()
    return ("Product deleted successfully")

def update_product(id):
    '''
    update the details of a product
    takes the product id as argument
    return the updated product details
    '''
    if request.method == 'PUT':
        updated_product = request.json
        cursor = data_base.cursor(dictionary=True)
        cursor.execute(f"update products set ProductName = '%s', ProductPrice = '%s', ProductRating = '%s' WHERE id ={id}" %(updated_product['Name'],updated_product['Price'],updated_product['Rating']))
        data_base.commit()
        cursor.close()
        return jsonify({'updated_product' : updated_product})

def get_Products(id):
    '''
    get the details of a single product
    takes the product id as argument
    return a single product details
    '''
    cursor = data_base.cursor(dictionary=True)
    cursor.execute(f"SELECT id,productName,productPrice,productRating FROM products WHERE id= {id}")
    single_product=cursor.fetchone()
    cursor.close()
    return jsonify({'product' : single_product})

def upload_product_images(id):
    '''
    upload an image for a product
    takes the product id as argument
    returns an acknowlegment message for image uploaded
    '''
    if request.method == 'POST':
        image = request.files['file']
        image.save(app.config['IMAGE_FOLDER']+secure_filename(image.filename))
        image_path = app.config['IMAGE_FOLDER']+secure_filename(image.filename)
        cursor = data_base.cursor(dictionary=True)
        image_data = open(image_path, 'rb').read()
        sql = f"update products set productImage=%s where id={id}"
        cursor.execute(sql, (image_data,))
        data_base.commit()
        cursor.close()
        return "Image Uploaded"
    return home_page('home.html')
