from flask import Flask, send_file, jsonify, make_response, request
import os


app = Flask(__name__)


@app.route('/<int:id>')
def home(id):
  if id == 1:
    filename = 'download.png'
  else:
    filename = 'download (2).jpeg'
    
  resp = make_response(open(filename,'rb').read())
  resp.content_type = "image/jpeg"
  return resp
  # return render_template('test.html',name = filename)
  return send_file(filename, mimetype='image/jpeg',download_name='1.jpg',as_attachment=True)


@app.route('/upload', methods=['POST'])
def upload():
  file = request.files['file'].read()
  res = make_response(file)
  res.content_type = "image/jpeg"
  return res


@app.route('/image/<name>')
def home_(name):
  
  resp = make_response(open(name,'rb').read())
  resp.content_type = "image/jpeg"
  return resp

  # return render_template('test.html',name = filename)
  return send_file(name, mimetype='image/jpeg',download_name='1.jpeg')


@app.route('/multi', methods=['POST'])
def multi():
  for file in request.files.getlist('file'):
    file.save('static/'+file.filename)
    print(file.filename)
  return 'success'


@app.route('/all')
def all():
  images = [open('static/'+name,'rb').read() for name in os.listdir('static')]
  resp = make_response(images)
  resp.content_type = "image/jpeg"
  return resp



if __name__=='__main__':
  app.run(debug=True)
