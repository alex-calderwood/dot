from sklearn.datasets import make_classification

# Create app
from flask import Flask, jsonify, make_response, render_template
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

def make_synth(n=1000):
    synth_x, synth_y = make_classification(n_samples=n, n_features=2, n_informative=2, n_redundant=0,
        n_classes=2,  n_clusters_per_class=1, weights=[0.5, 0.5], shift=-0.5, scale=100)


    synth = []
    for x, y in zip(synth_x, synth_y):
        x0, x1 = float(x[0]), float(x[1])
        y = int(y)

        synth.append({'position': [x0, x1], 'uv': [x0, -x1], 'class': y})
    return synth

# if __name__ == '__main__':
    # print(make_synth())

# @app.route('/')
# def index():
#     return render_template('dot.html')


@app.route('/')
def synth():
    j = jsonify(make_synth())
    return make_response(j, 200)