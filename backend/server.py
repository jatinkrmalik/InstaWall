import json

from flask import Flask, Response
from flask_cors import CORS
import random
from models import LowPolyGenerator, HorizontalLineGenerator

app = Flask(__name__)
CORS(app)

klass_list = [LowPolyGenerator, HorizontalLineGenerator]


@app.route('/generate')
def generate_default():
    klass = random.choice(klass_list)
    shape_type, shape_points = klass(
        dimensions=(1920, 1080)).generate()
    return Response(
        response=json.dumps({
            'type': shape_type,
            'plotMe':  shape_points
        }),
        status=200,
        content_type='application/json'
    )


@app.route('/generate/<int:width>/<int:height>')
def generate_shape(width, height):
    try:
        klass = random.choice(klass_list)
        shape_type, shape_points = klass(
            dimensions=(width, height)).generate()
    except ValueError as e:
        response_json = json.dumps({
            'error': e.args,
            'message': 'Mininum height/width should be > 200 for pattern to work.'
        })
        status_code = 400
    else:
        response_json = json.dumps({
            'type': shape_type,
            'plotMe': shape_points
        })
        status_code = 200

    return Response(
        response=response_json,
        status=status_code,
        content_type='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
