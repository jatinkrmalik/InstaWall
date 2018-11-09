from flask import Flask
from models import LowPolyGenerator
import json
from flask import Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/generate')
def generate_default():
    points = LowPolyGenerator(center_cords=(1920//2,1080//2)).generate()
    return json.dumps(points)

@app.route('/generate/<int:width>/<int:height>')
def generate_shape(width, height):
    try:
        points = LowPolyGenerator(center_cords=(width//2,height//2)).generate()
    except ValueError as e:
        response_json = json.dumps({
            'error': e.args,
            'message': 'Mininum height/width should be > 200 for pattern to work.'
        })
    else:
        response_json = json.dumps({'plotMe': points})

    return Response(
        response=response_json,
        status=200,
        content_type='application/json'
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
