from flask import Flask
import delegate

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route("/services", methods=['GET'])
def getServices():
    return delegate.getServices()

@app.route("/cloud-regions", methods=['GET'])
def getCloudRegions():
    return delegate.getCloudRegions()

if __name__ == '__main__':
    app.run(debug=True)
