import products
from flask import Flask

app=Flask(__name__)
app.config['IMAGE_FOLDER'] = 'Images/'

@app.route('/')
def index():
    return products.index()

@app.route("/products" , methods = ['GET'])
def get_all_products():
    return products.get_all_products()

@app.route("/products/create" , methods = ['POST' , 'GET'])
def create_product():
    return products.create_new_product()

@app.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    return products.delete_product(id)

@app.route('/products/update/<int:id>', methods=['PUT', 'GET'])
def update_product(id):
    return products.update_product(id)

@app.route("/products/<int:id>",methods=['GET'])
def get_Products(id):
    return products.get_Products(id)

@app.route("/products/images/<int:id>" , methods = ['GET' , 'POST'])
def upload_product_images(id):
    return products.upload_product_images(id)

if __name__=="__main__":
   app.run(debug=True)

