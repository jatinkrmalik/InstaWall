import json

from flask import Flask, Response
from flask_cors import CORS
import random
from models import LowPolyGenerator

app = Flask(__name__)
CORS(app)


@app.route('/generate')
def generate_default():
    points = LowPolyGenerator(center_cords=(1920//2, 1080//2)).generate()
    return Response(
        response=json.dumps({'plotMe': points}),
        status=200,
        content_type='application/json'
    )


@app.route('/generate/<int:width>/<int:height>')
def generate_shape(width, height):
    try:
        w  = width//random.randint(1,4)
        h  = height//random.randint(1,4)
        points = LowPolyGenerator(
            center_cords=(w, h)).generate()
    except ValueError as e:
        response_json = json.dumps({
            'error': e.args,
            'message': 'Mininum height/width should be > 200 for pattern to work.'
        })
        status_code = 400
    else:
        response_json = json.dumps({'plotMe': points})
        status_code = 200

    return Response(
        response=response_json,
        status=status_code,
        content_type='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
