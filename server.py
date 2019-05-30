import delegate
from flask import Flask, redirect, url_for, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return "Hello, World!"


@app.route("/services", methods=['GET'])
def getServices():
    return delegate.getServices()

@app.route("/cloud-regions", methods=['GET'])
def getCloudRegions():
    return delegate.getCloudRegions()

@app.route("/cloudTypes", methods=['GET'])
def getCloudTypes():
    return delegate.getCloudTypes()


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name=user))

if __name__ == '__main__':
   app.run(debug=True)