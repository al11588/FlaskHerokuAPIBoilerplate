from flask import Flask, render_template, url_for, request
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app = FlaskAPI(__name__)

app.debug = True

api = {
    0: 'alvinboilerplatecode',
}

def apiinformation(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('apiinformation2', key=key),
        'text': api[key]
    }



@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def apiinformation2(key):
    """
    Retrieve, update or delete apiinformation2 instances.
    """
    if request.method == 'PUT':
        apiinformation2 = str(request.data.get('text', ''))
        api[key] = apiinformation2
        return apiinformation(key)

    elif request.method == 'DELETE':
        api.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in api:
        raise exceptions.NotFound()
    return apiinformation(key)




if __name__ == '__main__':
    app.run()
